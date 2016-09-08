# alk-collateral-sensitivity
Repository for the R code and experimental data for the paper "Collateral sensitivity networks reveal evolutionary instability and novel treatment strategies in ALK mutated non-small-cell lung cancer." (preprint available soon)

Files included:

[1] final_expt_data.xlsx: File contains survival curves for all collateral sensitivity assays considered, presented as average survival followed by standard deviation. For each survival curve, contains EC50 and Hill coefficient from fitting procedure as well as assoicated confidence intervals, where computable. Sheet name indicates the drug-resistant cell line for which the data on that sheet is presented, and the drug being treated is listed adjacent to the survival table. 

[2] get_EC50_Hill_coeff_upload.R: Contains the code used to fit the survival curves to a Hill function to obtain EC50 and Hill coefficient. 

[3] test_lc_data.xlsx: Input file for R script. This must be modified to contain the desired drug concentration/survival values for fitting. 

[4] count_cycles.py: This code counts the number of cycles of a particular length from directed graph, defined by an adjacency matrix G (defined in the script).
