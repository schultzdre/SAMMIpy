.. SAMMIpy documentation master file, created by
   sphinx-quickstart on Wed Jun 12 15:51:25 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SAMMIpy
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

SAMMIpy is a tool for visualizing metabolic networks and metabolic network simulations using SAMMI directly from Python using the COBRApy toolbox. This documentation describes the Pythons wrapper for this visualization. You can view the full documentation for SAMMI `here
<https://sammi.readthedocs.io/en/latest/index.html>`_, and the documentation for COBRApy `here
<https://cobrapy.readthedocs.io/en/stable/>`_.

Installation and Usage
===================================
SAMMIpy can be installed via :code:`pip` by running the following code in the command window:

.. code-block:: none

    pip install sammi

To update the package use:

.. code-block:: none

    pip install sammi -U

To use the package add the following code to your python script:

.. code-block:: python

    import sammi

Some of the functionality available in SAMMI, such as PDF download and data upload, are not directly available though this plugin. To use these functions download the model in a SAMMI format and upload the file in the SAMMI web interface at `www.SammiTool.com
<https://bioinformatics.mdanderson.org/Software/SAMMI/>`_.

For a full description of this plugin please refer to the remaining sections of this documentation.

Documentation
=================

.. toctree::
   :maxdepth: 2

   classes
   functions
   examples
