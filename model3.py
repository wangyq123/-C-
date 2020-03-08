import datareader
import random

def getScoreByMontecarlo1(values,times,TV1=0.8,TV2=0.6):
    productscore={}
    for i in range(times):
        for value in values:
            if value[2]=='Y':
                if value[0] in productscore.keys():
                    productscore[value[0]][0]+=value[1]
                    productscore[value[0]][1]+=1
                else:
                    productscore[value[0]]=[value[1],1]
            elif value[3]=='N':
                if random.random()<=TV1:
                    if value[0] in productscore.keys():
                        productscore[value[0]][0]+=value[1]
                        productscore[value[0]][1]+=1
                    else:
                        productscore[value[0]]=[value[1],1]
                else:
                    if value[0] in productscore.keys():
                        productscore[value[0]][0]+=6-value[1]
                        productscore[value[0]][1]+=1
                    else:
                        productscore[value[0]]=[6-value[1],1]
            else:   #when value[3] is Y
                if random.random()<=TV2:
                    if value[0] in productscore.keys():
                        productscore[value[0]][0]+=value[1]
                        productscore[value[0]][1]+=1
                    else:
                        productscore[value[0]]=[value[1],1]
                else:
                    if value[0] in productscore.keys():
                        productscore[value[0]][0]+=6-value[1]
                        productscore[value[0]][1]+=1
                    else:
                        productscore[value[0]]=[6-value[1],1]
    for item in productscore:
        productscore[item][0]/=productscore[item][1]
    return productscore

def getScoreByMontecarlo2(values,times,TV1=0.8,TV2=0.6):
    productscore={}
    for i in range(times):
        for value in values:
            if value[4]=='Y':
                if value[0] in productscore.keys():
                    productscore[value[0]][0]+=value[1]+value[1]*value[2]+(6-value[1])*(value[3]-value[2])
                    productscore[value[0]][1]+=1
                else:
                    productscore[value[0]]=[value[1]+value[1]*value[2]+(6-value[1])*(value[3]-value[2]),1]
            elif value[5]=='N':
                if random.random()<=TV1:
                    if value[0] in productscore.keys():
                        productscore[value[0]][0]+=value[1]+value[1]*value[2]+(6-value[1])*(value[3]-value[2])
                        productscore[value[0]][1]+=1
                    else:
                        productscore[value[0]]=[value[1]+value[1]*value[2]+(6-value[1])*(value[3]-value[2]),1] 
                else:
                    rou=random.random()
                    oppsite_votes=value[3]-value[2]
                    if value[0] in productscore.keys():
                        
                        productscore[value[0]][0]+=6-value[1]+value[1]*value[2]*rou+(6-value[1])*value[2]*(1-rou)\
                                                    +(6-value[1])*oppsite_votes*rou+value[1]*oppsite_votes*(1-rou)
                        productscore[value[0]][1]+=1
                    else:
                        productscore[value[0]]=[6-value[1]+value[1]*value[2]*rou+(6-value[1])*value[2]*(1-rou)\
                                                    +(6-value[1])*oppsite_votes*rou+value[1]*oppsite_votes*(1-rou),1]
            else:
                if random.random()<=TV2:
                    if value[0] in productscore.keys():
                        productscore[value[0]][0]+=value[1]+value[1]*value[2]+(6-value[1])*(value[3]-value[2])
                        productscore[value[0]][1]+=1
                    else:
                        productscore[value[0]]=[value[1]+value[1]*value[2]+(6-value[1])*(value[3]-value[2]),1] 
                else:
                    rou=random.random()
                    oppsite_votes=value[3]-value[2]
                    if value[0] in productscore.keys():
                        
                        productscore[value[0]][0]+=6-value[1]+value[1]*value[2]*rou+(6-value[1])*value[2]*(1-rou)\
                                                    +(6-value[1])*oppsite_votes*rou+value[1]*oppsite_votes*(1-rou)
                        productscore[value[0]][1]+=1
                    else:
                        productscore[value[0]]=[6-value[1]+value[1]*value[2]*rou+(6-value[1])*value[2]*(1-rou)\
                                                    +(6-value[1])*oppsite_votes*rou+value[1]*oppsite_votes*(1-rou),1]
    for item in productscore:
        productscore[item][0]/=productscore[item][1]
        productscore[item][0]=round(productscore[item][0],2)
    return productscore

if __name__=='__main__':
    filename='..\\2020_Weekend2_Problems\\Problem_C_Data\\hair_dryer.tsv'
    df=datareader.read(filename)
    # values=list(zip(df['product_id'],df['star_rating'],df['vine'],df['verified_purchase']))
    # print(values)
    # # TV1=0.8
    # # TV2=0.6
    # print(getScoreByMontecarlo1(values,1000))
    values2=list(zip(df['product_id'],df['star_rating'],df['helpful_votes'],df['total_votes'],df['vine'],df['verified_purchase']))
    # print(values2)
    # for item in values2:
    #     print(item)
    results=getScoreByMontecarlo2(values2,100)
    for item in results:
        print(item,results[item])
