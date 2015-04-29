"""
S2SNetFilterByPDBchains = filter S2SNet files using a list of PDB chains

Authors:
Yong Liu | y.liu@udc.es
Cristian R Munteanu | muntisa@gmail.com

Affiliation:
Computer Science Faculty, University of A Coruna, Spain
"""

def S2SNetFilterByPDBchains(PDBChainsFName,S2SNetFName,NewS2SNetFName):
    print "Filtering S2SNet files using a list of PDB chains ...",
    PDBchainF= open(PDBChainsFName,"r")
    linesPSDBChains = PDBchainF.readlines()
    PDBchainF.close()
        
    S2SNetF = open(S2SNetFName,"r")
    linesS2SNet = S2SNetF.readlines()
    S2SNetF.close()

    NewS2SNetF= open(NewS2SNetFName, "w")
    
    for cline in linesPSDBChains:
        if cline[-1]=='\n': cline= cline[:-1]
        cPDB,cChain=cline.split('\t')
        
        for sline in linesS2SNet:
            sPDB,sChain,sSeq=sline.split('\t')
            if (cPDB == sPDB) and (cChain == sChain):
                NewS2SNetF.write(sline) 
    NewS2SNetF.close()
    print "Done!"
    return

#-------------------------------------------------
# Use of S2SNetFilterByPDBchains
#-------------------------------------------------
PDBChainsFName = "PDBchains.txt"
S2SNetFName    = "S2SNetchains.txt"
NewS2SNetFName = "NewS2SNetChains.txt"

S2SNetFilterByPDBchains(PDBChainsFName,S2SNetFName,NewS2SNetFName)

