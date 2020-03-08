import pandas as pd 

def read(filename):
    data=pd.read_csv(filename,sep='\t')
    return data

if __name__=='__main__':
    filename='..\\2020_Weekend2_Problems\\Problem_C_Data\\pacifier.tsv'
    print(read(filename))
