What does the git contain:
Contains a requirements.txt file
Contains a README.md
Subfolder codes contains implementations of the algorithms. 
Subfolder graphs contains implementation with preprocessed dataset to reproduce the graphs. 
Subfolder data contains all the preprocessed datasets. 



Implemented algorithms
Baselines: 
1. FairILP (Caitlin Kuhlman and Elke Rundensteiner. 2020. Rank aggregation algorithms for
fair consensus. Proceedings of the VLDB Endowment 13, 12 (2020), 2706–2719.)
2. DetConstSort (Sahin Cem Geyik, Stuart Ambler, and Krishnaram Kenthapadi. 2019. Fairnessaware
ranking in search & recommendation systems with application to linkedin
talent search. In Proceedings of the 25th ACM SIGKDD International Conference
on Knowledge Discovery & Data Mining. 2221–2231)

OurSolutions: GrBinaryIPF, ApproxMultiValuedIPF, AlgRAPF, RandAlgRAPF

To find the codes for each of the algorithms:
Subfolder codes --> Algorithm names


How to prepare the dataset: 
n number of items, m number of ranked lists, distribution of the protected attributes over the items to create proportion.  

How to use the code:
Go to the folder named codes, change the line which contains the dataset path name and run the code.


Reproducing the figures:
Go to subfolder graphs
Figure 1 --> Run Fig_1a_plot.ipynb,  Fig_1b_plot.ipynb, Fig_1c_plot.ipynb
Figure 2 --> Run Fig_2a_plot.ipynb,  Fig_2b_plot.ipynb, Fig_2c_plot.ipynb
Figure 3 --> Run Fig_3a_plot.ipynb,  Fig_3b_plot.ipynb, Fig_3c_plot.ipynb
Figure 4 --> Run Fig_4a_plot.ipynb,  Fig_4b_plot.ipynb, Fig_4c_plot.ipynb
Figure 5 --> Run Fig_5a_code, Fig_5a_plot.ipynb,  Fig_5b_code, Fig_5b_plot.ipynb
Figure 6 --> Run Fig_6a_plot.ipynb,  Fig_6b_plot.ipynb
Figure 7 --> Run Fig_7a_plot.ipynb,  Fig_7b_plot.ipynb
Figure 8 --> Run fig_8a_code.py, Fig_8a_plot.ipynb,  fig_8b_code.py, Fig_8b_plot.ipynb, fig_8c_code.py, Fig_8c_plot.ipynb, fig_8d_code.py, Fig_8d_plot.ipynb
Figure 9 --> Run Fig_9a_plot.ipynb,  Fig_9b_plot.ipynb


**Add .gitignore (I think the standard python .gitignore by GitHub should work: https://github.com/github/gitignore/blob/main/Python.gitignore)
**Remove unnecessary or auto-generated files (e.g., *.bak files)
