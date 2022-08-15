########## NATE DFM Maker
########## Ensure Housman4 Functions are loaded before running, or will crash. 
def Nate_DFM(data, nMFW = 1000, culling = 0, chunks = 1):
    dfList = []
    import pandas as pd; import string; import collections; from sklearn import svm; from os import listdir; import re; from string import punctuation

    if chunks == 1:
        Corpus_List = Data_Prep(data, full=True)
    else: 
        data = splitter(data, n=chunks)
        Corpus_List = Data_Prep(data, full = True)

        

    for i in range (0, len(Corpus_List)):   
        with open(Corpus_List[i], "r") as Corpus_List[i]: #This line and below mimics line 14 in R studio
            Document = Corpus_List[i].read().lower()
            
            #Replace all Left/Right single quotation marks, flanked by a space, with nothing (dialogue / contractions with no ending)
            
            Document = Document.replace(" ’", "")
            Document = Document.replace(" ‘", "")
            Document = Document.replace("’ ", "")
            Document = Document.replace("‘ ", "")
            
            my_punctuation = {"!":"",'"':"","#":"","$":"","%":"","&":"","(":"", ")":"",
                              "*":"","+":"",",":"","-":"",".":"","/":"",":":"",";":"",
                              "<":"","=":"",">":"","?":"","@":"","[":"","\\":"","]":"",
                              "^":"","_":"","`":"","{":"","|":"","}":"","~":"",
                              '“':"", '”':"","’":"'", "‘":"'" }
            apostrophe_sub = {"'":"X"} #Stylo Can't handle Apostrophes. This preserves the tokens, without explicitly requiring the apostrophe unicode. 
            
            Document = Document.translate(str.maketrans(my_punctuation))
            Document = Document.translate(str.maketrans(apostrophe_sub))
            
            Document = Document.split()
            
        
        #The following snippet uses the counter argument to create a "Counter" type. The most_common() argument makes this into a list. 
        Doc_Stats = (collections.Counter(Document)).most_common() #Create my own dictionaries here instead? 

        
        #Get the total number of words in the "tabl" variable.
        Word_Count = 0
        for j in range (0, len(Doc_Stats)):
            Word_Count += Doc_Stats[j][1]
        
        #Divide the Doc_stats number by the relative % word-count, and turn the corresponding data into a dictionary 
        temp_dict = { (Doc_Stats[i][0]) : (100*(Doc_Stats[i][1]/Word_Count)) for i in range(0, len(Doc_Stats)) }  
        
        #Add the dictionary to t
        dfList.append(temp_dict)                                                                
    
    #Turn the list of dictionaries into a Dataframe
    Combined_DF = pd.DataFrame(dfList) 
    
    #Use the "Data_Prep" function to extract a list of corpus names, then set the Dataframe row names to the Corpus_List Names              
    Corpus_List = Data_Prep(data, full=False)
    Combined_DF.insert(0, 'Index:', Corpus_List) 
    Combined_DF = Combined_DF.set_index('Index:')

    #Split the Corpus list. Each line becomes a tuple of the style (AUTHOR - Genre - Text Name)
    for i in range(0, len(Corpus_List)):
        Corpus_List[i] = Corpus_List[i].split('_')
    
    #Split the tuples into 3 separate lists
    Author_List, Genre_List, Text_List = [], [], []
    for i in range(0, len(Corpus_List)):
        Author_List.append(Corpus_List[i][0])
        Genre_List.append(Corpus_List[i][1])
        Text_List.append(Corpus_List[i][2:])
    
    #Merge the 'Text List', as it may contain multiple tuples (Each word from the title will be its own entry in the tuple)
    for i in range (0, len(Text_List)):
        Text_List[i] = ' '.join(Text_List[i])

    #Add the 3 lists, created above, into the dataframe    
    Combined_DF.insert(0, 'Text Name:', Text_List)
    Combined_DF.insert(0, 'Genre:', Genre_List)
    Combined_DF.insert(0, 'Author:', Author_List)
    
    #Set all "NAs" to 0
    Combined_DF = Combined_DF.fillna(0)
    
    #Below Line Culls based off of the percentage given in argument; default to 50 
    if culling > 0:
        Combined_DF = Combined_DF.drop(columns=Combined_DF.columns[((Combined_DF==0).mean()>(culling/100))],axis=1)
    
    #DFM = Combined_DF.iloc[0:(len(Combined_DF.index)), 0:(nMFW+3)] 
    
    ###### NEW Stuff
    DFM = Combined_DF
    empty_list = [100.0, 100.0, 100.0]
    
    for i in range (3, (len(DFM.columns))):
        cap_sum = capped_average(DFM.iloc[:, i] )
        empty_list.append(cap_sum)
    
    DFM.loc['Averages'] = empty_list #Appending list as row to DF
    
    DFM.sort_values(by = 'Averages', axis = 1, ascending = False, inplace = True)
    DFM.drop('Averages', inplace = True)
    
    DFM = DFM.iloc[0:(len(DFM.index)), 0:(nMFW+3)] 
    
    return (DFM)

#Takes a series of numbers, returnd an average, in which any number > 'ceiling' turns into ceiling. 
def capped_average(row, ceiling = 10):
       total_sum = 0
        
       for i in range (0, len(row)):
           if row[i] > ceiling:
               total_sum += ceiling
           else:
               total_sum += row[i]
        
       capped_avg = total_sum / len(row)
       return (capped_avg)
   
    
   
    
   
    
   
    
   
    
############ JOCKERS DFM --> Removes all grammar, and does not have CappedAverage Protection. Otherwise identical to Nate_DFM
def Jock_DFM(data, nMFW = 1000, culling = 0, chunks = 1):
    dfList = []
    import pandas as pd; import string; import collections; from sklearn import svm; from os import listdir; import re; from string import punctuation

    if chunks == 1:
        Corpus_List = Data_Prep(data, full=True)
    else: 
        data = splitter(data, n=chunks)
        Corpus_List = Data_Prep(data, full = True)

        

    for i in range (0, len(Corpus_List)):   
        with open(Corpus_List[i], "r") as Corpus_List[i]: #This line and below mimics line 14 in R studio
            Document = Corpus_List[i].read().lower()
            
            #Replace all Left/Right single quotation marks, flanked by a space, with nothing (dialogue / contractions with no ending)
            
            Document = Document.replace(" ’", "")
            Document = Document.replace(" ‘", "")
            Document = Document.replace("’ ", "")
            Document = Document.replace("‘ ", "")
            
            my_punctuation = {"!":"",'"':"","#":"","$":"","%":"","&":"","(":"", ")":"",
                              "*":"","+":"",",":"","-":"",".":"","/":"",":":"",";":"",
                              "<":"","=":"",">":"","?":"","@":"","[":"","\\":"","]":"",
                              "^":"","_":"","`":"","{":"","|":"","}":"","~":"",
                              '“':"", '”':"","’":"", "‘":"", "'":"" }
            
            Document = Document.translate(str.maketrans(my_punctuation))
            
            Document = Document.split()
            
        
        #The following snippet uses the counter argument to create a "Counter" type. The most_common() argument makes this into a list. 
        Doc_Stats = (collections.Counter(Document)).most_common() #Create my own dictionaries here instead? 

        
        #Get the total number of words in the "tabl" variable.
        Word_Count = 0
        for j in range (0, len(Doc_Stats)):
            Word_Count += Doc_Stats[j][1]
        
        #Divide the Doc_stats number by the relative % word-count, and turn the corresponding data into a dictionary 
        temp_dict = { (Doc_Stats[i][0]) : (100*(Doc_Stats[i][1]/Word_Count)) for i in range(0, len(Doc_Stats)) }  
        
        #Add the dictionary to t
        dfList.append(temp_dict)                                                                
    
    #Turn the list of dictionaries into a Dataframe
    Combined_DF = pd.DataFrame(dfList) 
    
    #Use the "Data_Prep" function to extract a list of corpus names, then set the Dataframe row names to the Corpus_List Names              
    Corpus_List = Data_Prep(data, full=False)
    Combined_DF.insert(0, 'Index:', Corpus_List) 
    Combined_DF = Combined_DF.set_index('Index:')

    #Split the Corpus list. Each line becomes a tuple of the style (AUTHOR - Genre - Text Name)
    for i in range(0, len(Corpus_List)):
        Corpus_List[i] = Corpus_List[i].split('_')
    
    #Split the tuples into 3 separate lists
    Author_List, Genre_List, Text_List = [], [], []
    for i in range(0, len(Corpus_List)):
        Author_List.append(Corpus_List[i][0])
        Genre_List.append(Corpus_List[i][1])
        Text_List.append(Corpus_List[i][2:])
    
    #Merge the 'Text List', as it may contain multiple tuples (Each word from the title will be its own entry in the tuple)
    for i in range (0, len(Text_List)):
        Text_List[i] = ' '.join(Text_List[i])

    #Add the 3 lists, created above, into the dataframe    
    Combined_DF.insert(0, 'Text Name:', Text_List)
    Combined_DF.insert(0, 'Genre:', Genre_List)
    Combined_DF.insert(0, 'Author:', Author_List)
    
    #Set all "NAs" to 0
    Combined_DF = Combined_DF.fillna(0)
    
    #Below Line Culls based off of the percentage given in argument; default to 50 
    if culling > 0:
        Combined_DF = Combined_DF.drop(columns=Combined_DF.columns[((Combined_DF==0).mean()>(culling/100))],axis=1)
    
    #DFM = Combined_DF.iloc[0:(len(Combined_DF.index)), 0:(nMFW+3)] 
    
    ###### NEW Stuff
    DFM = Combined_DF
    empty_list = [100.0, 100.0, 100.0]
    
    for i in range (3, (len(DFM.columns))):
        cap_sum = capped_average(DFM.iloc[:, i], ceiling = 100) #Ceiling @ 100% effectively invalidates this function. Maintained only to keep export consistency with Nate_DFM code. 
        empty_list.append(cap_sum)
    
    DFM.loc['Averages'] = empty_list #Appending list as row to DF
    
    DFM.sort_values(by = 'Averages', axis = 1, ascending = False, inplace = True)
    DFM.drop('Averages', inplace = True)
    
    DFM = DFM.iloc[0:(len(DFM.index)), 0:(nMFW+3)] 
    
    return (DFM)


