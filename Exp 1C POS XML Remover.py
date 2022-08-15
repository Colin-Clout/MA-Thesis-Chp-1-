
corpus = []
inp = '/Users/nate/Downloads/XMLs'

def XML_Prep (data, full=False):
    from os import listdir
    Corpus_List = listdir(data)
        
    '''
    for item in Corpus_List:
        if (item.endswith(".txt") == False) or (item.endswith(".xml") == False):
            Corpus_List.remove(item)
    '''
    for item in Corpus_List:
        if(item.endswith(".DS_Store")):
            Corpus_List.remove(item)
    if full == True:
        for i in range (0, len(Corpus_List)):
            Corpus_List[i] = data + '/' + Corpus_List[i]
        return(Corpus_List)
    else: return (Corpus_List)
    
    
x = XML_Prep(inp, full = True) 
y = XML_Prep(inp, full = False) #Y is used within the 'try' bit for creating the export file path

import re
for i in range (0, len(x)):
    with open(x[i], "r") as document: 
        document = document.readlines()
        
        parsed = []
        for line in document:
            if "rend" in line:
                continue
            elif "lemma" in line:
                parsed.append(line)
        
        
        prepped = []
        for line in parsed:
            if "emptycell" in line:
                continue
            else:
                scan = re.findall('"([^"]*)"', line)
                to_add = scan[0] + "*" + scan[1]
                prepped.append(to_add)
    corpus.append(prepped)

export = inp + '/Parsed/'
import os; import shutil
    

    
if os.path.exists(export) == False:
    os.makedirs(export)

for i in range (0, len(corpus)):  
    entry = ' '.join(corpus[i])
    output = open(export + y[i] + '.txt', 'w')
    output.write(entry)
    
