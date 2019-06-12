name = "sammi"

import numpy as np
import os

#Define sammiparser class
class parser:
    """
    Data to be used in parsing the model into subgraphs. Inputs:
    name: name of the subgraph.
    reactions: reactions to be included in given subgraph.
    flux: Optional flux values matching reactions. Plotted as reaction color if given.
    """
    def __init__(self,name,reactions,flux = None):
        self.reactions = reactions
        self.name = name
        self.flux = flux if flux is not None else np.repeat(float('nan'),len(reactions))

#Define SAMMI data class
class data:
    """
    Data to be used to modify the model. Inputs:
    -group: one of three choices: 'reactions', 'metabolites', or 'links'. Indicated which part of the visualization to map the data onto.
    -kind: one of two choices: 'color' or 'size'. The only combination not possible is 'links' and 'color', since link colors are the same as reaction colors.
    -data: vector of values matching ids.
    -ids: vector of reaction or metabolite IDs.
    -conditions: name of the conditions to use in labeling the data mapped
    """
    def __init__(self,group,kind,data,ids,conditions):
        if group not in ['reactions','metabolites','links']:
            raise Exception('Sammidata first argument must be \'reactions\', \'metabolites\', or \'links\'')
        if kind not in ['color','size']:
            raise Exception('Sammidata second argument must be \'color\' or \'size\'')
        if group == 'links' and kind == 'color':
            raise Exception('Link data does not work with color (link colors are based on reactions node)')
        if data.shape[0] != len(ids):
            raise Exception('Number of ' + group + ' do not match data size')
        if data.shape[1] != len(conditions):
            raise Exception('Number of conditions do not match data size')
        self.group = group
        self.kind = kind
        self.data = data
        self.ids = ids
        self.conditions = conditions

#Define default options
class options:
    """
    class with three fields for additional options upon loading SAMMI model. Inputs:
    -htmlName: name of html file to write the visualization to. Default 'index_load.html'. If a previous file with a given name exists overwrites the previous file.
    -load: Boolean. Wheter to open the model on a new browser window or not. If false, use sammi.open to open the file or reload a previously openend window.
    -jscode: Additional javascript code to be run upon loading the model.
    """
    def __init__(self,htmlName = None,load = None,jscode = None):
        if htmlName == 'index.html' or htmlName == 'index':
            raise Exception('Output file cannot be named index.html')
        self.htmlName = htmlName if htmlName is not None else 'index_load.html'
        self.load = load if load is not None else True
        self.jscode = jscode if jscode is not None else ''

#Converts the model to a JSON string to be interpreted by SAMMI
def makeJson (model):
    #Get reaction fields to include
    rxnfields = []
    for rx in model.reactions:
        for f in dir(rx):
            try:
                if isinstance(getattr(model.reactions[0],f),(str,bool,float,int)) and not f.startswith('_') and not f == 'id' and f not in rxnfields:
                    rxnfields.append(f)
            except:
                pass
    #Get metabolite fields to include
    metfields = []
    for me in model.metabolites:
        for f in dir(me):
            try:
                if isinstance(getattr(model.metabolites[0],f),(str,bool,float,int)) and not f.startswith('_') and not f == 'id' and f not in metfields:
                    metfields.append(f)
            except:
                pass
    #make metabolite fields
    fd = ['{"id":"' + f.id + '",' for f in model.metabolites]
    sep = ','
    for f in metfields:
        if isinstance(getattr(model.metabolites[0],f),str):
            fd = [x + '"' + f + '":"' + y + '"' + sep for x,y in zip(fd,[getattr(g,f) for g in model.metabolites])]
        elif isinstance(getattr(model.metabolites[0],f),bool):
            fd = [x + '"' + f + '":' + y + sep for x,y in zip(fd,[str(getattr(g,f)).lower() for g in model.metabolites])]
        else:
            fd = [x + '"' + f + '":' + y + sep for x,y in zip(fd,[str(getattr(g,f)) for g in model.metabolites])]
        if metfields.index(f) == len(metfields)-2:
            sep = '}'
    fd = [f.replace("\":None,\"","\":NaN,\"") for f in fd]
    #Make JSON string
    jsonstr = '{"metabolites":[' + ','.join(fd) + '],"reactions":['
    #make reaction fields
    fd = ['{"id":"' + f.id + '",' for f in model.reactions]
    for f in rxnfields:
        if isinstance(getattr(model.reactions[0],f),str):
            fd = [x + '"' + f + '":"' + y + '",' for x,y in zip(fd,[getattr(g,f) for g in model.reactions])]
        elif isinstance(getattr(model.reactions[0],f),bool):
            fd = [x + '"' + f + '":' + y + ',' for x,y in zip(fd,[str(getattr(g,f)).lower() for g in model.reactions])]
        else:
            fd = [x + '"' + f + '":' + y + ',' for x,y in zip(fd,[str(getattr(g,f)) for g in model.reactions])]
    fd = [f.replace("\":None,\"","\":NaN,\"") for f in fd]
    #Make metabolites fields
    metarr = [','.join(['"' + str(x) + '":' + str(y) for x,y in zip(z.metabolites.keys(),z.metabolites.values())]) for z in model.reactions ]
    fd = ','.join([x + '"metabolites":{' + y + '}}' for x,y, in zip(fd,metarr)])
    #Finalize JSON string
    jsonstr = jsonstr + fd + ']}'
    return jsonstr

#Parse model with struct
def structParse(model,parser):
    #Get unique reactions in parser
    rx = []
    for f in parser:
        rx = rx + f.reactions
    rx = list(set(rx))
    #Remove unwanted reactions
    tormrx = [f.id for f in model.reactions if f.id not in rx]
    model.remove_reactions(tormrx)
    #Remove blocked metabolites
    tormmet = [m for m in model.metabolites if len(m.reactions) == 0]
    model.remove_metabolites(tormmet)
    #Convert model to Json string
    jsonstr = 'graph = ' + makeJson(model)
    #Make conversion vector
    convvec = makeParseVector(parser)
    #Add parsing line
    jsonstr = jsonstr + ';\ne = ' + convvec + ';\nfilterWrapper(e)'
    return jsonstr

#Converts data class to vector
def makeParseVector(dat):
    parsevec = '[' + ','.join(['["' + cond.name + '",' + ','.join(['["' + x + '","' + str(y) + '"]' 
        for x,y in zip(cond.reactions,cond.flux)]) + ']' 
        for cond in dat]) + ']'
    return parsevec

#Convert data class to vector
def makeDataVector(dat):
    datavec = '[["' + '","'.join(dat.conditions) + '"],' + ','.join(['["' + rm + '","' + '","'.join(map(str,d)) + '"]' for rm,d in zip(dat.ids,dat.data)]) + ']'
    return datavec

def plot(model,parsert = [],datat = [],secondaries = [],opts = options()):
    """
    Plot model using SAMMI. Inputs:
    -model: COBRA model to be plotted
    -parsert: data used to parse the model into subgraphs. Can be one of:
        -empty vector (default): plots the whole model.
        -string: One of two options. (1) The name of a file pointing to a SAMMI map json file, which plots the given map. (2) The name of a reaction or metabolite field, plots one subgraph for each unique identifier in the field.
        -list of strings: list of reaction IDs to plot. Plot only those reactions.
        -list of parser objects: list of parser objects (sammi.parser). Plots one subgraph for each element.
    -datat: data to be plotted onto the model. List of data objects (sammi.data).
    -secondaries: list of regular expressions. Any metabolite matching any of the regular expressions will be shelved uppon loading.
    -opts: options object (sammi.options) for additional loading options:
    """

    #Define options. If a given file load the file
    if isinstance(parsert,str) and os.path.isfile(parsert):
        jsonstr = 'e = ' + open(parsert).read() + ';\nreceivedTextSammi(JSON.stringify(e));'
    #If a reactions or metabolite field
    elif isinstance(parsert,str) and not os.path.isfile(parsert):
        dat = []
        if parsert in dir(model.reactions[0]):
            categ = model.reactions
            ss = list(set([getattr(f,parsert) for f in categ]))
            ss.sort()
            for tmp in ss:
                dat.append(parser(tmp,[f.id for f in categ if getattr(f,parsert) == tmp]))
        elif parsert in dir(model.metabolites[0]):
            categ = model.metabolites
            ss = list(set([getattr(f,parsert) for f in categ]))
            ss.sort()
            for tmp in ss:
                rxns = []
                for f in categ:
                    if getattr(f,parsert) == tmp:
                        rxns = rxns + [g.id for g in list(f.reactions)]
                dat.append(parser(tmp,list(set(rxns))))
        else:
            pass #return
        jsonstr = structParse(model,dat)
    #If we are loading the whole model as one thing
    elif isinstance(parsert,list) and len(parsert) == 0:
        jsonstr = 'e = ' + makeJson(model) + ';\nreceivedJSONwrapper(e);'
    elif isinstance(parsert,list) and isinstance(parsert[0],parser):
        jsonstr = structParse(model,parsert)
    elif isinstance(parsert,list):
        if len(parsert) > 0:
            #Remove unwanted reactions
            tormrx = [f.id for f in model.reactions if f.id not in parsert]
            model.remove_reactions(tormrx)
            #Remove blocked metabolites
            tormmet = [m for m in model.metabolites if len(m.reactions) == 0]
            model.remove_metabolites(tormmet)
        #Plot remaining
        jsonstr = 'e = ' + makeJson(model) + ';\nreceivedJSONwrapper(e);'
    #Add data
    if isinstance(datat,data) or (isinstance(datat,list) and len(datat) > 0):
        if isinstance(datat,data):
            datat = [datat]
        for dat in datat:
            jsonstr = jsonstr + ';\ndat = ' + makeDataVector(dat)
            if dat.group == 'reactions':
                if dat.kind == 'color':
                    jsonstr = jsonstr + ';\nreceivedTextFlux(dat)'
                elif dat.kind == 'size':
                    jsonstr = jsonstr + ';\nreceivedTextSizeRxn(dat)'
            elif dat.group == 'metabolites':
                if dat.kind == 'color':
                    jsonstr = jsonstr + ';\nreceivedTextConcentration(dat)'
                elif dat.kind == 'size':
                    jsonstr = jsonstr + ';\nreceivedTextSizeMet(dat)'
            elif dat.group == 'links':
                if dat.kind == 'size':
                    jsonstr = jsonstr +  ';\nreceivedTextWidth(dat)'
    #Shelve secondaries
    if len(secondaries) > 0:
        jsonstr = jsonstr + ';\nshelveList("(?:' + ')|(?:'.join(secondaries) + ')");'
    #Add last bit of code
    jsonstr = jsonstr + opts.jscode
    #Read in template
    folder = __path__[0]
    index = open(folder + '\\browser\\index.html').read()
    #Write code in appropriate place
    index = index.replace('//MATLAB_CODE_HERE//',jsonstr)
    #Write to file
    open(folder + '\\browser\\' + opts.htmlName,'w').write(index)
    #Open
    if opts.load:
        os.system("start \"\" \"" + os.path.dirname(os.path.realpath(__file__)) + "\\browser\\" + opts.htmlName)

def openmap(htmlName):
    os.system("start \"\" \"" + os.path.dirname(os.path.realpath(__file__)) + "\\browser\\" + htmlName)
    return