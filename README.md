Describe prerequisite installation
Numpy, sklear, Gurobi, Networks

What does the git contain:
Subfolder codes contains implementations of the algorithms. 
Subfolder graphs contains implementation with preprocessed dataset to reproduce the graphs. 
Subfolder data contains all the preprocessed datasets. 


Explain the code structure, description and instructions for executing different mechanisms implemented, and paper reference.  

Implemented algorithms
Baselines: 1. FairILP, 2. DetConstSort (full reference) 
OurSolutions: GrBinaryILP, ApproxMultiIPF, RAPF, RandRAPF
Describe where these codes are.



Extend the README.md with information and instructions for someone who wants to apply your technique to their dataset. Then what would they require to prepare the dataset and proceed with reusing your code?

How to prepare the dataset: 
n number of items, m number of ranked lists, distribution of the protected attributes over the items to create proportion.  

How to use the code:
Go to the folder named codes, change the line which contains the dataset path name and run the code.




I noticed that there are several folders and runnable-code in the repository. It would be a good idea to include them in the README.md so that the public may benefit from all of your shared code as opposed to a specific single target.
Add .gitignore (I think the standard python .gitignore by GitHub should work: https://github.com/github/gitignore/blob/main/Python.gitignore)
Remove unnecessary or auto-generated files (e.g., *.bak files)
