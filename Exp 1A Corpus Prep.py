######### GRAMMAR PURGE --> Creates alt corpus, of all text files, with all grammar removed. 
######### GRAMMAR PURGE --> Used for readying Stylo Classifications for GP frequency tables. 
######### GRAMMAR PURGE --> Needed for "4. CF | NG" Freq Tables. Outputs results to "Variant Corpus" Folders. 
def Grammar_Purge(inp, n=1):    
    from math import floor; import os; import shutil; import string
    
    my_punctuation = {"!":"",'"':"","#":"","$":"","%":"","&":"","(":"", ")":"",
                              "*":"","+":"",",":"","-":"",".":"","/":"",":":"",";":"",
                              "<":"","=":"",">":"","?":"","@":"","[":"","\\":"","]":"",
                              "^":"","_":"","`":"","{":"","|":"","}":"","~":"",
                              '“':"", '”':"","’":"", "‘":"", "'":"" }
    
    x = Data_Prep(inp, full = True) 
    y = Data_Prep(inp, full = False) #Y is used within the 'try' bit for creating the export file path

    out_path = inp + '/GrammarPurged/'
    
    
    if os.path.exists(out_path) == True:
        shutil.rmtree(out_path)
        os.makedirs(out_path)
    else: 
         os.makedirs(out_path)

    for j in range (0, len(x)):
        text = open(x[j]).read() 
        text = text.lower()
        text = text.translate(str.maketrans(my_punctuation))
        step = len(text)/n 
        i = 0
        while i < n:
                    output = open(out_path + y[j] + '_' + str(i) + '.txt', 'w')
                    output.write( text [floor((step*i)) : floor((step*(i+1))) ])
                    i += 1
    return(out_path)


from os import listdir
root = '/Users/nate/Desktop/Thesis/Experiment 1'
Fold_List = listdir(root) #Manually remove DS Store
for folder in Fold_List:
    corpus = root + '/' + folder + '/Full Corpus' 
    Grammar_Purge(corpus)

###################################
###### END GRAMMAR PURGE FUNCTION
##################################

######### ALL APOSTROPHES --> Creates alt corpus, of all text filess. Replaces Trailing apostrophes with blank space (removing speech marks etc.)
######### ALL APOSTROPHES --> And replaces in-word apostrophes with "XXX" as stylo won't remove letter combinations. 
######### ALL APOSTROPHES --> Used for readying Classifications for AA frequency tables. 
######### ALL APOSTROPHES --> Needed for "3. AF | AA" & "6. CF | AA" Freq Tables. Outputs results to "Variant Corpus" Folders. 
def All_Apostrophes(inp, n=1):    
    from math import floor; import os; import shutil; import string
    my_punctuation = {"!":"",'"':"","#":"","$":"","%":"","&":"","(":"", ")":"",
                              "*":"","+":"",",":"","-":"",".":"","/":"",":":"",";":"",
                              "<":"","=":"",">":"","?":"","@":"","[":"","\\":"","]":"",
                              "^":"","_":"","`":"","{":"","|":"","}":"","~":"",
                              '“':"", '”':"","’":"'", "‘":"'"}
    apostrophe_sub = {"'":"X"}
    
    x = Data_Prep(inp, full = True) 
    y = Data_Prep(inp, full = False) #Y is used within the 'try' bit for creating the export file path

    out_path = inp + '/AllApostrophes/'
    
    
    if os.path.exists(out_path) == True:
        shutil.rmtree(out_path)
        os.makedirs(out_path)
    else: 
         os.makedirs(out_path)

    for j in range (0, len(x)):
        text = open(x[j]).read() 
        text = text.lower()
        text = text.translate(str.maketrans(my_punctuation))
        text = text.translate(str.maketrans(apostrophe_sub))
        step = len(text)/n 
        i = 0
        while i < n:
                    output = open(out_path + y[j] + '_' + str(i) + '.txt', 'w')
                    output.write( text [floor((step*i)) : floor((step*(i+1))) ])
                    i += 1
    return(out_path)


from os import listdir
root = '/Users/nate/Desktop/Thesis/Experiment 1'
Fold_List = listdir(root) #Manually remove DS Store
for folder in Fold_List:
    corpus = root + '/' + folder + '/Full Corpus' 
    All_Apostrophes(corpus)