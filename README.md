# alk-collateral-sensitivity
Repository for the R code and experimental data for the paper "Collateral sensitivity networks reveal evolutionary instability and novel treatment strategies in ALK mutated non-small-cell lung cancer." (preprint available soon)

Files included:

[1] final_expt_data.xlsx: File contains survival curves for all collateral sensitivity assays considered, presented as average survival followed by standard deviation. For each survival curve, contains EC50 and Hill coefficient from fitting procedure as well as assoicated confidence intervals, where computable. Sheet name indicates the drug-resistant cell line for which the data on that sheet is presented, and the drug being treated is listed adjacent to the survival table. Updated 1st Feb 2017.

[2] get_EC50_Hill_coeff_upload.R: Contains the code used to fit the survival curves to a Hill function to obtain EC50 and Hill coefficient. 

[3] test_lc_data.xlsx: Input file for R script. This must be modified to contain the desired drug concentration/survival values for fitting. 

[4] count_cycles.py: This code counts the number of cycles of a particular length from directed graph, defined by an adjacency matrix G (defined in the script).

[5] make_heatmap_upload.R: R code to generate heatmaps, as presented within the manuscript. Takes in input values directly from the excel file called "heatmap_example.xlsx".

[6] heatmap_example.xlsx: Example of input data to R script to generate heatmap.

[7] data_wt_cells_drug_treatment.xlsx: Excel file containing EC50 values and confidence intervals for wild-type H3122 cells under the drugs considered. Added to give measure of day-to-day variability in EC50 data.

[8] AlecR.py, CeritR.py, CrizR.py, LorlR.py: These are Python scripts to recreate the figures showing the time series of the EC50 values during the relaxation experiments, with associated confidence intervals.

<a href="https://zenodo.org/badge/latestdoi/24318/andrewdhawan/alk-collateral-sensitivity"><img src="https://zenodo.org/badge/24318/andrewdhawan/alk-collateral-sensitivity.svg" alt="10.5281/zenodo.61933"></a>
