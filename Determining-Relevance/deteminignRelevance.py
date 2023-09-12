import re
import pandas as pd

def getAbs(row_num):
    ''' return row_num's abstarct'''
    return df.loc[row_num , 'Abstract']

def checkRelevace(abs):
    '''check abs with regular expretion'''
    regu_ex_for_high = ".*Online continual learning.*"
    regu_ex_for_medium = ".*continual learning.*"
    check_high = re.search(regu_ex_for_high , abs , re.IGNORECASE)   #search on abs for regular expersion high
    check_medium = re.search(regu_ex_for_medium ,abs  , re.IGNORECASE)  #search on abs for regular expersion medium
    if check_high:
        return "high"
    elif check_medium:
        return "medium"
    else:
        return "low"
    
df = pd.read_csv("sheet.csv")
for i in range(0 , len(df.index)): #move on all rows
    abs = getAbs(i)     #find abstract
    relevance = checkRelevace(abs)  #check relevance
    df.loc[i , "Relevance"] = relevance #chage relevane

df.to_csv('result.csv' , index=False)   #crate new result.csv with dataframe
    