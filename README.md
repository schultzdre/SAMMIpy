# SAMMIpy

This package provides a wrapper for running the Semi-Automated Metabolic Map Illustrator (SAMMI) from Python scripts and the Python command line. The SAMMI tool can be found at [www.sammitool.com](https://www.sammitool.com). The package works with the [COBRApy](https://opencobra.github.io/cobrapy/) toolbox and requires an internet connection to render maps. For more complex, up-to-date examples and to learn how to use the tool please check out the examples in the Jupyter Notebook file.

## Documentation
The SAMMIpy documentation can be found [here](https://sammipy.readthedocs.io/en/latest/).

## Installation

To install the package run ```pip install sammi``` from the Python command line.

## Usage

To use the SAMMI package run ```import sammi``` from within your python code. The function ```sammi.plot``` reads the template file ```index.html``` located at ```sammi.__path__[0] + '\\browser'```, and and outputs the generated map to the same folder in the file defined within the function (defaulting to ```index_load.html```). 

To open previously generated maps use ```sammi.openmap(htmlName)```. Once maps are generated they can be exported in the SAMMI specific format to be shared and saved.

## Help

For help using the function check ```help(sammi.plot)```.

## Examples
Load the following libraries to get started:
```Python
import cobra
import cobra.test
import numpy as np
import sammi
```

Plot entire model (not advisable for large models):
```Python
#Get sample model to plot
model = cobra.test.create_test_model("textbook")
#Plot
sammi.plot(model)
```

Plot a map for each subsytem:
```Python
#Get sample model to plot
model = cobra.test.create_test_model("salmonella")
#Plot
sammi.plot(model,'subsystem')
```

Plot a map for each compartment:
```Python
#Get sample model to plot
model = cobra.test.create_test_model("textbook")
#Plot
sammi.plot(model,'compartment')
```

Plot only certain reactions in a single graph and shelve secondary metabolites:
```Python
#Get sample model to plot
model = cobra.test.create_test_model("textbook")

#Define reactions
tca = ['ACONTa','ACONTb','AKGDH','CS','FUM','ICDHyr','MDH','SUCOAS']
gly = ['ENO','FBA','FBP','GAPD','PDH','PFK','PGI','PGK','PGM','PPS','PYK','TPI']
ppp = ['G6PDH2r','GND','PGL','RPE','RPI','TALA','TKT1','TKT2']
dat = tca + gly + ppp

#Define secondaries
secondaries = ['^h_.$','^h2o_.$','^atp_.$','^adp_.','^pi_.','^o2_.','^co2_.','^nad_.','^nadh_.','^ndap_.','^ndaph_.']

#Plot
sammi.plot(model,dat,secondaries = secondaries)
```

Plot lists of reactions in separate subgraphs:
```Python
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
```

Add (random) data to plotted subgraphs:
```Python
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
```

Divide map into subsystems, map random data using color and size, and shelve secondary metabolites.
```Python
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
```
