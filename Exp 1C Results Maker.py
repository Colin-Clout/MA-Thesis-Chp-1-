######### Results Maker from Exports of MFW Experiment. 
import pandas as pd
from os import listdir
from Housman4_01 import Data_Prep
from HousFixes import Nate_DFM
root = '/Users/nate/Desktop/Thesis/Experiment 1C'
Fold_List = listdir(root) #Manually remove DS Store. 
Fold_List.remove(".DS_Store")


#Various Data in the for-loop appended to these lists, which are later used to create a dataframe & export as CSV. 
FreqCount, CorpusTitle, CorpusPart, Classifier, MFWValue, CullingValue, SuccessSum, FailureSum, TotalSum, TPA = [], [], [], [], [], [], [], [], [], []

for folder in Fold_List:
    ResultSet = Data_Prep((root + '/' + folder + '/Outputs/'), full = True)
    Titles = Data_Prep((root + '/' + folder + '/Outputs/'), full = False)
    
    for i in range (0, len(ResultSet)):
        title = Titles[i][3:] #Remove the Number from the Title
        title = title.replace(" -", "").replace(".txt", "") #Remove hyphens and file-endings
        title = title.split(" | ") #Attributes are all separated by " | ", in experiment. 
        
        Success = 0
        Failure = 0 #; Total= Success + Failure; Percentage classification = (Success+Failure/Total)*100
        To_Parse = []


        with open(ResultSet[i], "r") as Doc: 
            Document = Doc.readlines() 
            for line in Document:
                if ("ANON_" in line): 
                    To_Parse.append(line)
                
   
            for entry in To_Parse:
                entry = entry.split()
                if (entry[2] in entry[0]):
                    Success += 1
                else: 
                    Failure += 1
    
        FreqCount.append(title[0]) ; CorpusTitle.append(title[1][:-2]) ; CorpusPart.append(int(title[1][-1])) ; Classifier.append(title[2]) 
        MFWValue.append(int(title[3].split()[0]))   ;  CullingValue.append(int(title[4].split()[0])) ; SuccessSum.append(Success) ; FailureSum.append(Failure) ; TotalSum.append(((Success/(Success + Failure))*100))
        if (int(title[1][-1]) <= 2): TPA.append(2)
        else: TPA.append(1)

Result = pd.DataFrame(data = [FreqCount, CorpusTitle, CorpusPart, Classifier, MFWValue, CullingValue, SuccessSum, FailureSum, TotalSum, TPA],
                      index = ["Freq Method", "Corpus", "Part", "Classifier", "MFW", "Culling", "Success", "Failure", "Total", "TPA"]).transpose()


#Result.to_csv("/Users/nate/Desktop/Thesis/Experiment 1/CollectedResults.csv")

x = Result.sort_values(by = ["Corpus", "Classifier", "Freq Method", "MFW", "Culling", "Part"])
for i in range (0, len(x), 3):
    x.iloc[i][6] += x.iloc[i+1][6]
    x.iloc[i][6] += x.iloc[i+2][6]
    
    x.iloc[i][7] += x.iloc[i+1][7]
    x.iloc[i][7] += x.iloc[i+2][7]
    
    x.iloc[i][8] = (x.iloc[i][6] / (x.iloc[i][6] + x.iloc[i][7]) * 100)
    
    x.iloc[i][9] = 100
    
Combined_TPAs = x.loc[x["TPA"] == 100]
Combined_TPAs.to_csv("/Users/nate/Desktop/Thesis/Exp 1C CombinedResults POS.csv")


