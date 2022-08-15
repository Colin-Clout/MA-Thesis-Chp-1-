#Quick Method of Counting the average text size across each corpus
#Link to each corpus is plugged in & iterated over. Each corpus' text files are read, split into a list, the size of the list 
#then added to a corpus int, and that int is finally divided by 25 (number of texts in each corpus)

Twentieth = '/Users/nate/Desktop/Thesis/Experiment 1/20th Century 1/Full Corpus'
Victorian = '/Users/nate/Desktop/Thesis/Experiment 1/Victorian Corpus 1/Full Corpus'
EME = '/Users/nate/Desktop/Thesis/Experiment 1/EME Corpus 1/Full Corpus'

from Housman4_01 import Data_Prep
Twentieth = Data_Prep(Twentieth, full = True)
Victorian = Data_Prep(Victorian, full = True)
EME = Data_Prep(EME, full = True)

Twentieth_Count = 0
Victorian_Count = 0
EME_Count = 0


for text in Twentieth:
    with open(text, "r") as Document:
        Document = Document.read().split()
        Twentieth_Count += len(Document)
        
for text in Victorian:
    with open(text, "r") as Document:
        Document = Document.read().split()
        Victorian_Count += len(Document)  
        
for text in EME:
    with open(text, "r") as Document:
        Document = Document.read().split()
        EME_Count += len(Document)
        
        
        
Twentieth_Count = Twentieth_Count / 25
Victorian_Count = Victorian_Count / 25
EME_Count = EME_Count / 25
