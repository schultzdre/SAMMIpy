Functions
==============
There are three main user functions for rendering and plotting SAMMI visualizations. These are:

Plotting
--------------
The function :code:`sammi.plot()` is used to plot SAMMI visualizations in combination with the SAMMI classes. The function inputs are:

- **model**: COBRApy model to be visualized.
- **parsert**: How the model is to be parsed and visualized. There are several options for this parameter:

   - *Empty vector*: Default. Does not parse the model and plots all reactions and metabolites in a single graph. Not recommended for medium to large-size models.
   - *string*: One of two options. (1) A reaction or metabolite field (e.g. :code:`subsystem` or :code:`compartment`), in which case a subgraph will be drawn for each unique value associated with that field. (2) A path to a file specifying a previously drawn SAMMI map, in which case that map will be rendered.
   - *List of strings*: List of reaction IDs to be plotted. A single graph will be plotted containing only the defined reactions.
   - *List of sammi.parser() objects*: A subgraph is plotted for each :code:`sammi.parser()` object defined in the list.
- **datat**: List of :code:`sammi.data()` objects. Each object will be plotted separately in the visualization.
- **secondaries**: List of strings or regular expressions. Any metabolite, in any subgraph, matching any of the regular expressions defined here will be shelved. These metabolites are not deleted and can be returned to the graph through the floating menu window. For details of this functionality please refer to the SAMMI documentation.
- **opts**: :code:`sammi.options()` object. Additional options for loading the map.

Opening a visualization
--------------------------
the function :code:`sammi.openmap()` is used for opening previously drawn visualizations. It takes a single input: a previously drawn html file name. For instance, :code:`sammi.openmap("index_load.html")` or :code:`sammi.openmap("index_load")` open the default file to which maps are exported.

Running SAMMIpy example
----------------------------
Several examples are built into the SAMMIpy package to exemplify and test the package functionalities. These examples are described in the following section as well as the Jupyter Notebook provided. To use this function run :code:`sammi.test(n)` where :code:`n` is a number from zero to eleven describing one of the examples.