"""
This script is to change the feature-names of a big data file;

The problem was:
I have a friend uses SAS to process big and datasets from health insurance companies. 
Many feature-names are very long and have spaces, so SAS cannot read it.
I wrote this script to replace the first line with new feature names and copy the rest data, 
which is an very fast and efficient way to solve his problem. 
"""
import numpy as np
import shutil

def main():
  # directory and name of the source data file
  # if the code and the data are in the same directory, just give the name of the file
  data_source_file = './Data/npi.ri.tsv' 
  
  # directory and name of the new name file
  # if the code and the data are in the same directory, just give the name of the file
  new_name_file = './Data/shortname.txt'
  
  # directory and name of the new data file
  # if the code and the data are in the same directory, just give the name of the file
  new_data_file = './Data/npi_new_ri.tsv'
  
  
  fs = open(data_source_file, 'r') # open the source data file
  fs.readline()                    # read and skip the first line, and wait to be copied 
  
  fnn = open(new_name_file, 'r')
  new_line = ''
  for line in fnn:
    new_line += line.replace('\r\n', '\t')
  new_line  += '\n'
  
  fd = open(new_data_file, 'w')
  fd.write(new_line)
  shutil.copyfileobj(fs, fd)
  

  
  
if __name__=="__main__":
  main()
