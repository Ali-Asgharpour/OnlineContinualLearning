import pandas as pd

def editCitation(path):
    '''edit citation column
     replace num if "cite by num" is citation
     and replace "check" if citation is empty
      and else replace with "0" 
      and save new data in result.csv'''
    print(path)
    df = pd.read_csv(path)
    for i in range(0 , len(df.index)):
        citation = df.loc[i , 'Citation']
        print(i)
        print(df.loc[i , 'Title'])
        try:
            int(citation)
        except:
            print(type(citation))
            print(citation)
            if type(citation) == str:
                words = citation.split(' ')
                first_word = words[0]
                if first_word == 'Cited':
                    df.loc[i , 'Citation'] = words[2]
                else:
                    df.loc[i , 'Citation'] = '0'
            else:
                df.loc[i , 'Citation'] = 'check'

    df.to_csv('result.csv' , index=False)   #crate new result.csv with dataframe

path = input('enter path:')
editCitation(path)

