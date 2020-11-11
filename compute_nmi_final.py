import sys
import numpy as np
import pandas as pd
import nibabel as nib
import math
import csv

def FisherTrans(x):

  '''
  Fisher's transformation
  '''

  try:
    return 0.5*(math.log((1+x)/(1-x)))
  except Exception, e:
    print str(e)

def ReadCSVFile(filename,header):

  '''
  load csv file and return a list
  '''

  output_list = []
  try:
    f = open(filename, 'rt')
    reader = csv.reader(f)
    if header:
      header = reader.next()
    for row in reader:
      output_list.append(row)
    f.close()
    return output_list
  except Exception, e:
    print str(e)

def compute_nmi(dataListFname, refDataFname, maskFname):

  '''
  compute neural maturity index

  dataListFname contains all the individual stats file names.

  refDataFname is the reference adult group-level brain stats map thresholded(p<0.01, FDR corrected).

  maskFname is the grey matter mask.
  '''

  dataList = ReadCSVFile(dataListFname,1)

  maskImg = nib.load(maskFname)
  maskData = maskImg.get_data()

  refImg = nib.load(refDataFname)
  refData = refImg.get_data()

  # create an index vector for mask, involving voxels that are significantly activated or de-activated and within the grey matter mask 
  maskIdx = np.where(((refData>0)|(refData<0))&(maskData>0)) 

  refVec = refData[maskIdx]

  output_mtx = np.zeros((len(dataList), 2))
  output_fname = 'nmi_output.csv'

  for i in range(len(dataList)):
    idataList = dataList[i]

    output_mtx[i,0] = i
    idata_Img = nib.load(idataList[0])
    idata_Data = idata_Img.get_data()
  
    idata_Vec = idata_Data[maskIdx]

    idata_corr = np.corrcoef(idata_Vec, refVec)

    output_mtx[i,1] = FisherTrans(idata_corr[0,1])

  df_column_names = ['subject_id', 'nmi']
  output_df = pd.DataFrame(output_mtx, columns=df_column_names)
  output_df.to_csv(output_fname,sep=',',header=True,index=False)
