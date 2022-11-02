Describe prerequisite installation
Numpy, sklear, Gurobi, Networks
**mention how to install
** version of library and hardware config.

What does the git contain:
Contains a requirements.txt file
Subfolder codes contains implementations of the algorithms. 
Subfolder graphs contains implementation with preprocessed dataset to reproduce the graphs. 
Subfolder data contains all the preprocessed datasets. 



Explain the code structure, description and instructions for executing different mechanisms implemented, and paper reference.  

Implemented algorithms
Baselines: 1. FairILP, 2. DetConstSort (full reference) 
OurSolutions: GrBinaryILP, ApproxMultiIPF, RAPF, RandRAPF
Describe where these codes are.



How to prepare the dataset: 
n number of items, m number of ranked lists, distribution of the protected attributes over the items to create proportion.  

How to use the code:
Go to the folder named codes, change the line which contains the dataset path name and run the code.


Reproducing the figures:
**describe which set of codes to run from graph subfolder to reproduce which figure.


**Add .gitignore (I think the standard python .gitignore by GitHub should work: https://github.com/github/gitignore/blob/main/Python.gitignore)
**Remove unnecessary or auto-generated files (e.g., *.bak files)
