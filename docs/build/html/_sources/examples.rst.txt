Examples
==============
Here we provide several simple examples for the use of SAMMIpy. Each example is supposed to be more complex than the next, and is intended to exemplify as many different functionalities of SAMMIpy as possible. Each example can be run using :code:`sammi.test(n)`, where :code:`n` refers to the example number provided here.

To start, load the following libraries:

.. code-block:: python

    import cobra
    import cobra.test
    import numpy as np
    import sammi

0. Plot entire model
-------------------------
To plot the entire model simply call :code:`sammi.plot()` on the COBRA model. This is not advisable for medium to large models as the visualization may be too large to render.

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("textbook")
    #Plot file to default index_load.html
    sammi.plot(model)

1-2. Divide the model into subgraphs using model annotation
---------------------------------------------------------------------------
1. Maps can be divided into subgraphs using model annotation. For instance, users can plot a subgraph for each annotated reaction subsystem:

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("salmonella")
    #Plot
    sammi.plot(model,'subsystem')

2. Or plot a map for each cellular compartment:

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("textbook")
    #Plot
    sammi.plot(model,'compartment')

3. Plot and visualize multiple maps
----------------------------------------
By default, SAMMI outputs the visualization to a file names :code:`index.load.html` in the package folder. Therefore, by default, every time a new visualization is generated this file is overwritten. The name of the output file can be changed, however, in order to not overwrite files. For instance:

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("salmonella")
    #Generate options. This will not load a new tab upon generating the visualization
    opts = sammi.options(load = False)
    #Plot file to default index_load.html
    sammi.plot(model,'subsystem',opts = opts)
    #Generate option for new name
    opts = sammi.options(htmlName = 'index_load2.html',load = False)
    #Plot file to default index_load.html
    sammi.plot(model,'compartment',opts = opts)
    #Open files in new tabs
    sammi.openmap('index_load.html')
    sammi.openmap('index_load2.html')

4. Plot only user-defined reactions
-------------------------------------------
For a quick visualization of a given group of reactions users can plot only certain reactions in a single graph.

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("textbook")

    #Define reactions
    tca = ['ACONTa','ACONTb','AKGDH','CS','FUM','ICDHyr','MDH','SUCOAS']
    gly = ['ENO','FBA','FBP','GAPD','PDH','PFK','PGI','PGK','PGM','PPS','PYK','TPI']
    ppp = ['G6PDH2r','GND','PGL','RPE','RPI','TALA','TKT1','TKT2']
    dat = tca + gly + ppp

    #Plot
    sammi.plot(model,dat)

5. Shelve secondary metabolites on load
--------------------------------------------
In order to shelve secondary metabolites upon rendering the model, define the :code:`secondaries` input to the plot function. If this argument is defined, any metabolite, matching any of the defined regular expressions, will be shelved. These metabolites can be returned to the graph using the floating menu window.

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("textbook")

    #Define reactions
    tca = ['ACONTa','ACONTb','AKGDH','CS','FUM','ICDHyr','MDH','SUCOAS']
    gly = ['ENO','FBA','FBP','GAPD','PDH','PFK','PGI','PGK','PGM','PPS','PYK','TPI']
    ppp = ['G6PDH2r','GND','PGL','RPE','RPI','TALA','TKT1','TKT2']
    dat = tca + gly + ppp

    #Define secondaries
    secondaries = ['^h_.$','^h2o_.$','^atp_.$','^adp_.','^pi_.','^o2_.','^co2_.','^nad_.','^nadh_.','^nadp_.','^nadph_.']

    #Plot
    sammi.plot(model,dat,secondaries = secondaries)

6. Plot multiple user-defined subgraphs
-----------------------------------------------
Users can also plot multiple subgraphs with their defined reactions. To do so, define an instance of :code:`sammi.parser()` for each subgraph:

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("textbook")

    #Define reactions
    tca = ['ACONTa','ACONTb','AKGDH','CS','FUM','ICDHyr','MDH','SUCOAS']
    gly = ['ENO','FBA','FBP','GAPD','PDH','PFK','PGI','PGK','PGM','PPS','PYK','TPI']
    ppp = ['G6PDH2r','GND','PGL','RPE','RPI','TALA','TKT1','TKT2']

    #Initialize class
    dat = [sammi.parser('TCA cycle',tca),
        sammi.parser('Glycolysis/Gluconeogenesis',gly),
        sammi.parser('Pentose Phosphate Pathway',ppp)]
    #Plot
    sammi.plot(model,dat)

7-8. Data mapping
-----------------------
7. Add data to plotted subgraphs. In this example we are generating random data and mapping it onto the desired reactions. Using :code:`sammi.parser()` users can directly map data as reaction colors:

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("textbook")

    #Define reactions
    tca = ['ACONTa','ACONTb','AKGDH','CS','FUM','ICDHyr','MDH','SUCOAS']
    gly = ['ENO','FBA','FBP','GAPD','PDH','PFK','PGI','PGK','PGM','PPS','PYK','TPI']
    ppp = ['G6PDH2r','GND','PGL','RPE','RPI','TALA','TKT1','TKT2']

    #Initialize class
    dat = [sammi.parser('TCA cycle',tca,np.random.rand(len(tca))),
        sammi.parser('Glycolysis/Gluconeogenesis',gly,np.random.rand(len(gly))),
        sammi.parser('Pentose Phosphate Pathway',ppp,np.random.rand(len(ppp)))]
    #Plot
    sammi.plot(model,dat)

8. Alternatively, users can map data onto the map using :code:`sammi.data()`. The following example maps five sets of random data, each in a different way, with three conditions each.

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("salmonella")

    #Get reactions and metabolites
    rx = [f.id for f in model.reactions]
    met = [m.id for m in model.metabolites]

    #Generate random data to plot
    datat = [sammi.data('reactions','color',np.random.rand(len(rx),3),rx,['c1','c2','c3']),
            sammi.data('reactions','size',np.random.rand(len(rx),3),rx,['c1','c2','c3']),
            sammi.data('metabolites','color',np.random.rand(len(met),3),met,['c1','c2','c3']),
            sammi.data('metabolites','size',np.random.rand(len(met),3),met,['c1','c2','c3']),
            sammi.data('links','size',np.random.rand(len(rx),3),rx,['c1','c2','c3'])]

    #Introduce NAs
    for k in range(len(datat)):
        for i in range(datat[k].data.shape[0]):
            for j in range(datat[k].data.shape[1]):
                if np.random.rand(1)[0] < 0.1:
                    datat[k].data[i,j] = float('nan')

    #Define secondaries
    secondaries = ['^h_.$','^h2o_.$','^atp_.$','^adp_.','^pi_.','^o2_.','^co2_.','^nad_.','^nadh_.','^ndap_.','^ndaph_.']

    #Plot
    sammi.plot(model,'subsystem',datat = datat,secondaries = secondaries,opts = sammi.options(load=True))

9. Change map upon load
-----------------------------
SAMMI options also allow users to change visualization parameters upon loading the model. This can be done by adding JavaScript code to the end of the visualization. To use this advanced feature users need to be familiar with JavaScript and need to familiarize themselves with the SAMMI visualization html layout. The following code loads the previous map, changes the visualization to the Citric Acid Cycle subgraph, and changes the colorscale upon loading.

.. code-block:: python

    #Get sample model to plot
    model = cobra.test.create_test_model("salmonella")

    #Get reactions and metabolites
    rx = [f.id for f in model.reactions]
    met = [m.id for m in model.metabolites]

    #Generate random data to plot
    datat = [sammi.data('reactions','color',np.random.rand(len(rx),3),rx,['c1','c2','c3']),
            sammi.data('reactions','size',np.random.rand(len(rx),3),rx,['c1','c2','c3']),
            sammi.data('metabolites','color',np.random.rand(len(met),3),met,['c1','c2','c3']),
            sammi.data('metabolites','size',np.random.rand(len(met),3),met,['c1','c2','c3']),
            sammi.data('links','size',np.random.rand(len(rx),3),rx,['c1','c2','c3'])]

    #Introduce NAs
    for k in range(len(datat)):
        for i in range(datat[k].data.shape[0]):
            for j in range(datat[k].data.shape[1]):
                if np.random.rand(1)[0] < 0.1:
                    datat[k].data[i,j] = float('nan')

    #Define secondaries
    secondaries = ['^h_.$','^h2o_.$','^atp_.$','^adp_.','^pi_.','^o2_.','^co2_.','^nad_.','^nadh_.','^ndap_.','^ndaph_.']

    #Generate javascript
    jscode = 'x = document.getElementById("onloadf1");' + \
    'x.value = "Citric Acid Cycle";' + \
    'onLoadSwitch(x);' + \
    'document.getElementById("fluxmin").valueAsNumber = -0.1;' + \
    'document.getElementById("fluxmax").valueAsNumber = 0.1;' + \
    'fluxmin = -0.1; fluxmax = 0.1;' + \
    'document.getElementById("edgemin").value = "#ff0000";' + \
    'document.getElementById("edgemax").value = "#0000ff";' + \
    'document.getElementById("addrxnbreak").click();' + \
    'document.getElementsByClassName("rxnbreakval")[0].value = 0;' + \
    'document.getElementsByClassName("rxnbreakcol")[0].value = "#c0c0c0";' + \
    'defineFluxColorVectors();'

    #Plot
    sammi.plot(model,'subsystem',datat = datat,secondaries = secondaries,opts = sammi.options(load=True,jscode=jscode))

10. Type-III Pathways
-------------------------

Type-III pathways are thermodynamically infeasible loops within the model that do not involve exchange reactions. Here we visualize some of these pathways. We first block all exchange reactions and perform FVA to determine reactions still able to carry flux. Next, we optimize each of these reactions using pFBA to determine the smallest possible Type-III pathway involving the reaction. This example might take a couple of minutes to run.

.. code-block:: python

    #Import
    from cobra.flux_analysis import flux_variability_analysis
    from cobra.flux_analysis.loopless import add_loopless, loopless_solution
    #Get model and tailor
    model = cobra.test.create_test_model("salmonella")
    model.reactions.get_by_id('ATPM').lower_bound = 0
    model.reactions.get_by_id('ATPM').upper_bound = 1000
    rxns = [r.id for r in model.reactions]
    #Close exchange reactions
    medium = model.medium
    for i in model.medium:
        medium[i] = 0.0
    model.medium = medium
    #Perform FVA on the model
    fva = flux_variability_analysis(model,fraction_of_optimum = 0)
    fva.maximum[fva.maximum < 1e-03] = 0
    fva.minimum[fva.minimum > -1e-03] = 0
    #Initialize
    dat = []
    #Parse through positive reactions
    for i in range(len(fva.maximum)):
        if fva.maximum[i] != 0:
            model.objective = model.reactions[i]
            model.optimize()
            flux = cobra.flux_analysis.pfba(model)
            flux.fluxes[abs(flux.fluxes) < 1e-3] = 0
            tmp = abs(flux.fluxes) >= 1e-3
            dat.append(sammi.parser(model.reactions[i].id + ' positive',list(flux.fluxes[tmp].index),list(flux.fluxes[tmp].values)))
    #Parse through negative reactions
    for i in range(len(fva.minimum)):
        if fva.minimum[i] != 0:
            model.objective = model.reactions[i]
            model.reactions[i].objective_coefficient = -1
            flux = model.optimize()
            flux = cobra.flux_analysis.pfba(model)
            flux.fluxes[abs(flux.fluxes) < 1e-3] = 0
            tmp = abs(flux.fluxes) >= 1e-3
            dat.append(sammi.parser(model.reactions[i].id + ' negative',list(flux.fluxes[tmp].index),list(flux.fluxes[tmp].values)))
    #Plot
    sammi.plot(model,dat)

11. Metabolic Adaptation
------------------------
Visualize adaptation to gene knockout. In short, the following code performs the following steps for each reaction we wish to simulate.

1. Simulate reaction knockout and get maximum growth rate on KO model.
2. Set upper and lower bound growth rate on wild-type model to KO growth rate and calculate a loopless flux distribution.
3. Using MOMA, calculate a flux distribution in the knockout strain that closely matches the flux distribution in the previous step.
4. Find the difference in flux distributions in steps two and three and plot them.

This process allows users to visualize how the flux was rewired in the knockout strain. This example may take a couple of minutes to run.

.. code-block:: python

    from cobra.flux_analysis import single_reaction_deletion, moma
    from cobra.flux_analysis.loopless import add_loopless, loopless_solution

    #Get model
    model = cobra.test.create_test_model("ecoli")
    #Set objective
    model.objective = "Ec_biomass_iJO1366_core_53p95M"
    #Initialize parsing list
    dat = []
    #Define reactions to simulate knockout
    korxns = ['ENO','FBA','TKT2','TALA','FUM','MDH','GAPD','TPI']
    #Simulate reaction knockout
    for r in korxns:
        with model:
            #Save original bounds
            lb = model.reactions.get_by_id(r).lower_bound
            ub = model.reactions.get_by_id(r).upper_bound
            #Set objective to KO
            model.reactions.get_by_id(r).knock_out()
            objval = model.optimize().objective_value
            model.reactions.get_by_id("Ec_biomass_iJO1366_core_53p95M").upper_bound = objval
            model.reactions.get_by_id("Ec_biomass_iJO1366_core_53p95M").lower_bound = objval
            #Restore bounds
            model.reactions.get_by_id(r).lower_bound = lb
            model.reactions.get_by_id(r).upper_bound = ub
            #Calculate objective
            model.optimize()
            flux = loopless_solution(model)
            #Calculate adaptation
            model.reactions.get_by_id(r).knock_out()
            koflux = cobra.flux_analysis.moma(model,solution=flux)
            #Save
            tmp = flux.fluxes - koflux.fluxes
            bol = abs(tmp) > 1e-7
            x = tmp[bol]
            dat.append(sammi.parser(r + ' - ' + str(round(objval,4)),list(x.index),list(x)))
            #Restore bounds again
            model.reactions.get_by_id(r).lower_bound = lb
            model.reactions.get_by_id(r).upper_bound = ub
            model.reactions.get_by_id("Ec_biomass_iJO1366_core_53p95M").upper_bound = 1000
            model.reactions.get_by_id("Ec_biomass_iJO1366_core_53p95M").lower_bound = 0
    #Define secondaries
    secondaries = ['^h_.$','^h2o_.$','^atp_.$','^adp_.','^pi_.','^o2_.','^co2_.','^nad_.','^nadh_.','^ndap_.','^ndaph_.',\
                '^q8_.$','^q8h2_.$','^nadp_.','^nadph_.']
    #Plot difference in scatterplot
    sammi.plot(model,dat,secondaries = secondaries)