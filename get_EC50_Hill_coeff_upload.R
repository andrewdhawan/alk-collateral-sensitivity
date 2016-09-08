"
Andrew Dhawan
Sept 8 2016
get_EC50_Hill_coeff_upload.R

This file allows one to import the data 
from the excel file which is in a two-column 
format, with drug concentration as first column,
and survival as second column.
This is read, and fit to a Hill-type function
corresponding EC50 parameters, and Hill coefficient
are output, as well as 95% confidence intervals for
these parameters.

Also plots the experimental data, overlaid with model fit.

Saves output EC50 and Hill coefficient to output.txt
"

library(readxl)
output <- matrix(,nrow=2,ncol=2)

data <- read_excel("test_lc_data.xlsx")
drug_conc <- data$a #concentration vector
alive <- data$b #survival fraction

last_ind <- 10 #stores the number of concentrations tested/desired for fitting

#take appropriate subsets
alive <- alive[1:last_ind]
drug_conc <- drug_conc[1:last_ind]

low <- min(alive)
maxi <- max(alive)

#model fitting
m <- nls(alive~(low + ((maxi - low)/(1+((drug_conc/ec50)^b)))), start = list(ec50=0.1, b=0.1),trace=TRUE);

#confidence intervals
a <- confint(m)

print(m)
print(paste("(",a[1,1],",",a[1,2],")"))
print(paste("(",a[2,1],",",a[2,2],")"))
coeffs <- coef(m)
output[1,1] <- coeffs[[1]]
output[2,1] <- coeffs[[2]]
output[1,2] <- paste("(",a[1,1],",",a[1,2],")")
output[2,2] <- paste("(",a[2,1],",",a[2,2],")")

#save the output data in a file
write.table(output, "output.txt", sep="\t")

#plot model ouptut
plot.new()
plot(drug_conc,alive,log="x")
lines(drug_conc,predict(m))

