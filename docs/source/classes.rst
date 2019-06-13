Classes
==============
Three classes used to render visualizations are defined in the SAMMIpy package. This section describes these classes. For details on how to use them please refer to the subsequent sections. These classes are the following:

Parser
--------------
The class :code:`sammi.parser()` defines an object to be used in parsing the model into subgraphs upon loading. Although there are many ways to partition models using SAMMIpy, one of the options is defining a vector of :code:`sammi.parser()` objects where each object defines one subgraph. The :code:`sammi.parser()` class takes three inputs:

- **reactions**: List. Reaction IDs of reactions to be included in the subgraph.
- **name**: String. Name of the subgraph to be displayed in the visualization.
- **flux**: List. Optional. Values to be mapped as reaction colors. Defaults to all NAs where no data is mapped.

Data
--------------
The class :code:`sammi.data()` defines which data to be mapped onto the visualization and how. Similarly to the previous class, a vector of :code:`sammi.data()` objects can be defined to plot multiply data types. The class takes five inputs:

- **group**: String. Has three options: :code:`reactions`, :code:`metabolites`, and :code:`links`. Defines where the data will be mapped.
- **kind**: String. Has two options: :code:`color` and :code:`size`. Defines what kind of data to map onto the defined group. :code:`color` can be user with :code:`reactions` and :code:`metabolites` to define node and link color. :code:`color` cannot be used with :code:`links`, as link color matches the corresponding reaction node color. :code:`size` can be used to define node radius or link width.
- **data**: Numerical array where each row defines a reaction or metabolite and each column defines a condition to be mapped. Should have size :code:`len(ids)` by :code:`len(conditions)`.
- **ids**: List of strings. Reaction or metabolite IDs where the data will be mapped. Should be IDs of the variable defined in *group*.
- **conditions**: List of strings. Names to be used for each data condition mapped.

Options
--------------
The class :code:`sammi.options()` defines additional options of how the model is plotted. This class takes three fields:

- **htmlName**: Name of html file where the output will be written. Defaults to :code:`index_load.html`. If this option is not defined, the file :code:`index_load.html` will be continuously overwritten every time a new visualization is generated. If users wish to save a visualization to a different file, or wish to visualize multiple maps at once, this parameter can be changed.
- **load**: Boolean, defaults to :code:`True`. Whether or not to load the visualization on a new browser tab. If this parameter is set to false, new visualizations can be rendered by refreshing a previously loaded tab or by using the :code:`sammi.openmap()` function.
- **jscode**: String. Sequence of JavaScript commands to be run following the rendering of the visualization. This can used, for example, to change coloscales and subgraphs upon loading the model. This options requires familiarity with JavaScript and the SAMMI html layout.