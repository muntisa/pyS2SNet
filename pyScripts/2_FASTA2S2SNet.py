"""
FASTA2S2SNet = transform FASTA files in S2SNet input files (PDB,Chain,Seq)

Authors:
Yong Liu | y.liu@udc.es
Cristian R Munteanu | muntisa@gmail.com

Affiliation:
Computer Science Faculty, University of A Coruna, Spain
"""

def FASTA2S2SNet(inFASTA,outS2SNet):
    # read the FASTA file
    finFASTA = open(inFASTA,"r")
    linesFASTA = finFASTA.readlines()
    finFASTA.close()
    Seq=""
    foutFile = open(outS2SNet,"w") # start (over)write the output file
    iline=0
    for sline in linesFASTA:
        iline+=1
        if sline[0]=='>':
            PDBfasta=sline[1:5]
            ChainFasta=sline[6]
            if iline!=1:
                Seq=Seq+"\n"
            Seq=Seq+str(PDBfasta)+"\t"+str(ChainFasta)+"\t"
        else:
            Seq=Seq+sline[:-1]
    foutFile.write(Seq)
    foutFile.close()
    print "Done! "+inFASTA+" was transformed in "+outS2SNet+"."
    return

#-------------------------------------------------
# Use of FASTA2S2SNet
#-------------------------------------------------
inFASTA="FASTAChains.txt"
outS2SNet="S2SNetchains.txt"

FASTA2S2SNet(inFASTA,outS2SNet)

