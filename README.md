# clab_hawaii
**This repository has the code and related material that I am using in my PyPSA project related to a 100% renewable, reliable energy system for Oahu**
-----------------------------------------------------------------------------------------------------------------------

Link to Zenodo archive of repo: [![DOI](https://zenodo.org/badge/608204404.svg)](https://zenodo.org/doi/10.5281/zenodo.10214776)

-----------------------------------------------------------------------------------------------------------------------
The following is a description of the contents of each folder:  
  
**Data Processing:** Code that performed the necessary functions to turn weather data into capacity factors  
* Finished, processed weather capacity factors and electricity demand input files are in the Input Data folder.
* Each subfolder contains detailed instructions on how to run the data processing scripts
  
**Input Data:** The energy demand or weather capacity files used as inputs for PyPSA  

**Output Data:** The output files for each analysis  
* First workbook tab in the output data .xlsx is an exact copy of the model input parameters xlsx fed into PyPSA

**Plotting Code:** The code used to make each graph. Broken down by figure.

**HPCC:** Code, information, and inputs needed to run PyPSA on Caltech's high performance computing cluster  
* Optional, PyPSA runs fine on desktop

-----------------------------------------------------------------------------------------------------------------------
To run an optimization via PyPSA:
1. Download clab_pypsa on your system as described in the submodule (will create a folder)
2. Put weather capacity factors and electricity demand input files from the above "Input Data" GitHub folder (as .csv) into the clab_pypsa folder
3. Put Gurobi license file and model input parameters .xlsx file from the above "Output Data" Github folder in the folder that contains the clab_pypsa folder (not in the clab_pypsa folder)
4. In command terminal, type "conda activate pypsa_table"
5. Then "python clab_pypsa/run_pypsa.py -f filename.xlsx" <-- filename is the name of the .xlsx model input parameters file.
6. Enjoy

