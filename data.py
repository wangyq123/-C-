import pandas as pd


def get_dict(data):
    product_id = data['product_id'].values.tolist()
    product_parent = data['product_parent'].values.tolist()
    product_title = data['product_title'].values.tolist()
    product = list(zip(product_parent, product_title))
    dictionary = dict(zip(product_id,product))
    return dictionary

if __name__=='__main__':
    PATH = '..\\2020_Weekend2_Problems\\Problem_C_Data\\hair_dryer.tsv'
    data = pd.read_csv(PATH, sep='\t')
    d = get_dict(data)
    print(d)
