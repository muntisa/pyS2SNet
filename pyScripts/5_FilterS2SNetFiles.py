"""
FilterS2SNetFiles = get only the PDBchains from the first file that are not found in second file
                    (remove from negatives the positives PDBchains)
Authors:
Yong Liu | y.liu@udc.es
Cristian R Munteanu | muntisa@gmail.com

Affiliation:
Computer Science Faculty, University of A Coruna, Spain
"""

def FilterS2SNetFiles(ToBeFilter,Filter,Filtered):
    print "Filtering "+ToBeFilter+" with "+Filter+" ... "
    
    NegativeFile = open(ToBeFilter,"r")
    Negativelines = NegativeFile.readlines()
    NegativeFile.close()

    Positiveallchains= open(Filter,"r")
    Positiveallchianslines= Positiveallchains.readlines()
    Positiveallchains.close()

    NegativeFinalFile = open(Filtered,"w")
    for negativeline in Negativelines:
        Flag=0 # no encuentra seq equal
        nPDB, nChain, nSeq = negativeline.split('\t')
        for positiveline in Positiveallchianslines:
            pPDB, pChain, pSeq = positiveline.split('\t')
            if nSeq == pSeq:
                Flag=1 # encuentra seq equal
        if Flag == 0: # no encuentra seq equal
            NegativeFinalFile.write(negativeline)        
    NegativeFinalFile.close()
    print "Done! Filtered file:"+Filtered
    return

#-------------------------------------------------
# Use of FilterS2SNetFiles
#-------------------------------------------------

ToBeFilter = "S2SNetchains.txt"
Filter     = "S2SNetFilter.txt"
Filtered   = "S2SNetFiltered.txt"

FilterS2SNetFiles(ToBeFilter,Filter,Filtered)
