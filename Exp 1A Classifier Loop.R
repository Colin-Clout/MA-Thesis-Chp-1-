Meta = '/Users/nate/Desktop/Thesis/Experiment 1'
Options = list.files(Meta)

Classifiers = list("svm", "knn", "delta")
MFW = list(100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
Culling = list(5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100)
Tables = list("1. AF | NG - ", "2. AF | SP - ", "3. AF | AA - ", "4. CF | NG - ", "5. CF | SP - ", "6. CF | AA - ")


for (entry in Options){
  path = paste(Meta, '/', entry, '/',  sep ='')
  setwd(path)
  for (method in Classifiers){
    for (value in MFW){
      for (num in Culling){
        for (style in Tables){
      prim_table = paste(style, "freq_table_primary_set.txt", sep = "")
      sec_table  = paste(style, "freq_table_secondary_set.txt", sep = "")
      classify(gui = FALSE, mfw.max = value, mfw.min = value, classification.method = method, 
               culling.min = num, culling.max = num, 
               training.frequencies = prim_table,
               test.frequencies = sec_table,
               use.existing.freq.table = TRUE,
               outputfile = paste(path, "/Outputs/", style, " | ", entry, " | ", method, " | ", value, 
                                  " MFW", " | ", num, " Culling", ".txt", sep = ''))
      }
      }
      }
      }
}



