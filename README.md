# SAMMIpy

This package provides a wrapper for running the Semi-Automated Metabolic Map Illustrator (SAMMI) from Python scripts and the Python command line. The SAMMI tool can be found at [www.sammitool.com](https://www.sammitool.com). The package works with the [COBRApy](https://opencobra.github.io/cobrapy/) toolbox and requires an internet connection to render maps. For more complex, up-to-date examples and to learn how to use the tool please check out the examples in the Jupyter Notebook file.

## Documentation
The SAMMIpy documentation can be found [here](https://sammipy.readthedocs.io/en/latest/).

## Installation

To install the package run ```pip install sammi``` from the Python command line.

## Usage

To use the SAMMI package run ```import sammi``` from within your python code. The function ```sammi.plot``` reads the template file ```index.html``` located at ```sammi.__path__[0] + '\\browser'```, and outputs the generated map to the same folder in the file defined within the function (defaulting to ```index_load.html```). 

To open previously generated maps use ```sammi.openmap(htmlName)```. Once maps are generated they can be exported in the SAMMI specific format to be shared and saved.

## Help

For help check ```help(sammi.plot)``` within Python or read the SAMMIpy documentation [here](https://sammipy.readthedocs.io/en/latest/). Users can also look at the examples provided in the Jupyter Notebook in this folder. All of the examples provided in the notebook can be run using ```sammi.test(n)``` where ```n``` ranges from 0 to ten.