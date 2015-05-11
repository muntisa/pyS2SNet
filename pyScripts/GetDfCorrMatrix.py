# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:57:58 2015

@author: Cristian
"""

def CorrMatFile(DsFile,CorrFile):
    import pandas as pd
    df=pd.read_csv(DsFile)   # read CSV dataset
    df_corr= df.corr()       # get correlation matrix for ds
    df_corr.to_csv(CorrFile) # print to file the corralation matrix
    return
# --------- MAIN -----------------------
    
# Generate Correlation Matrix file from a CSV dataset file
CorrMatFile('TestDs.csv','CorrMat.csv')

