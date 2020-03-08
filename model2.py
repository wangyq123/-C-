import datareader

# get the final score
def getComprehensiveScore(data):
    values=list(zip(df['product_id'],df['star_rating'],df['helpful_votes'],df['total_votes']))
    productScore={}
    for item in values:
        if item[0] in productScore.keys():
            productScore[item[0]]+=item[1]*item[2]+(6-item[1])*(item[3]-item[2])
        else:
            productScore[item[0]]=item[1]+item[1]*item[2]+(6-item[1])*(item[3]-item[2])
    return productScore


if __name__=='__main__':
    filename='..\\2020_Weekend2_Problems\\Problem_C_Data\\hair_dryer.tsv'
    df=datareader.read(filename)
    # print(df['product_id'],df['helpful_votes'],df['total_votes'])
    # print(getComprehensiveScore(df))
    PS=getComprehensiveScore(df)
    for item in PS:
        print(item,PS[item])
    # print(len(PS.keys()))
    

    
