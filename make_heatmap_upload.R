#Andrew Dhawan
#Sept 8 2016
#make_heatmap_upload.R
#This code enables the generation of a heatmap from 
#values within an excel file, as defined by the example
#input file heatmap_example.xlsx
library(readxl)
data <- read_excel("heatmap_example.xlsx")

rowNames <- data$`Drug`
data$`Drug` <-NULL

ec50_matrix <- data.matrix(data)
my_palette <- colorRampPalette(c("#2c7bb6","#f7f7f7", "#d7191c"))(n = 128) #299)
ec50_heatmap <- heatmap.2(ec50_matrix, Rowv=NA, Colv=NA, col =my_palette, na.color = "darkgrey", scale="none", margins=c(10,10),labRow=rowNames, trace='none',dendrogram="none",density.info="none")
