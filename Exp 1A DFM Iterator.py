#Iterates over folders, making DFM's and producing Nate/Jockers Frequency tables. 
from os import listdir
root = '/Users/nate/Desktop/Thesis/Experiment 1'
Fold_List = listdir(root) #Manually remove DS Store & Exports Folder
for folder in Fold_List:
    corpus = root + '/' + folder + '/Full Corpus' 
    #corpus = root + '/' + folder + '/Variant Corpora/Stylo Prepped'
    
    Nate = Nate_DFM(corpus, nMFW = 1200)
    #Nate = Jock_DFM(corpus, nMFW = 1200)
    Nate_Titles = list(Nate.columns)

    Nate_Anon = Nate[Nate['Author:']=='ANON']
    Nate_Train = Nate[Nate['Author:']!='ANON']
    
    Nate.drop(['Author:', 'Genre:', 'Text Name:'], axis = 1, inplace = True)
    Nate_Anon.drop(['Author:', 'Genre:', 'Text Name:'], axis = 1, inplace = True)
    Nate_Train.drop(['Author:', 'Genre:', 'Text Name:'], axis = 1, inplace = True)
    
    Nate_Anon = Nate_Anon.transpose()
    Nate_Train = Nate_Train.transpose()
    
    export = root + '/' + folder

    Nate_Anon.to_csv(export + "/3. AF | AA - freq_table_secondary_set.txt", sep = " ")
    Nate_Train.to_csv(export + "/3. AF | AA - freq_table_primary_set.txt", sep = " ")
    #Nate_Anon.to_csv(export + "/2. AF | SP - freq_table_secondary_set.txt", sep = " ")
    #Nate_Train.to_csv(export + "/2. AF | SP - freq_table_primary_set.txt", sep = " ")
    #Nate_Anon.to_csv(export + "/1. AF | NG - freq_table_secondary_set.txt", sep = " ")
    #Nate_Train.to_csv(export + "/1. AF | NG - freq_table_primary_set.txt", sep = " ")