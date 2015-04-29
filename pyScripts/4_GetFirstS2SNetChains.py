"""
GetFirstS2SNetChain = get only the first chains from all PDBs in S2SNet format (PDB, Chain, Seq)

Authors:
Yong Liu | y.liu@udc.es
Cristian R Munteanu | muntisa@gmail.com

Affiliation:
Computer Science Faculty, University of A Coruna, Spain
"""

def GetFirstS2SNetChains(ToFilter,FilteredFirstChain):
    print "Getting only the first chains from all PDBs in S2SNet format ... "
    ToFilterS2SNetF= open(ToFilter, "r")
    AllChainslines= ToFilterS2SNetF.readlines()
    ToFilterS2SNetF.close()

    FilteredChainsFile= open(FilteredFirstChain,"w")
    tPDB="0000"
    for line in AllChainslines:
        PDB,Chains,Sep= line.split('\t')
        if tPDB!=PDB:
            FilteredChainsFile.write(line)
            tPDB=PDB
    FilteredChainsFile.close()
    print "Done! Now we have the single chain from the same PDBID."
    return

#-------------------------------------------------
# Use of GetFirstS2SNetChain
#-------------------------------------------------

ToFilter = "S2SNetchains.txt"
FilteredFirstChain = "S2SNetFilteredChains.txt"

GetFirstS2SNetChains(ToFilter,FilteredFirstChain)
