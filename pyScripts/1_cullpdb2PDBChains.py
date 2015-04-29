"""
cullpdb2PDBChains = get PDB chains from cullpdb files

Authors:
Yong Liu | y.liu@udc.es
Cristian R Munteanu | muntisa@gmail.com

Affiliation:
Computer Science Faculty, University of A Coruna, Spain
"""

def cullpdb2PDBChains(cullpdbFile,PDBchainFile):
    print "cullpdb2PDBChains: getting PDB chains from cullpdb files ... ",
    cullpdb= open(cullpdbFile,"r")
    linescullpdb = cullpdb.readlines()
    cullpdb.close()

    seq=""
    PDBIDChains= open(PDBchainFile,"w")
    for cline in linescullpdb:
        PDBID= cline[0:4]
        Chain= cline[4]
        seq= seq + str(PDBID)+"\t"+str(Chain)+"\n"
    PDBIDChains.write(seq)
    PDBIDChains.close()
    print "done!"
    return

#-------------------------------------------------
# Use of cullpdb2PDBChains
#-------------------------------------------------

cullpdbF  = "cullpdb_pc20_res1.6_R0.25_d150314_chains2442.txt"
PDBchainF = "PDBchains.txt"

cullpdb2PDBChains(cullpdbF,PDBchainF)


