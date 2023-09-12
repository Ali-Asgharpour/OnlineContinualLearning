import pandas as pd
import matplotlib.pyplot as plt

def show(correct , incorrect):
    '''show diagram'''
    correct = correct*100/(correct + incorrect)
    incorrect = incorrect*100/(correct + incorrect)

    labels = 'correct', 'incorect'
    sizes = [correct , incorrect]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)

    plt.ioff()
    plt.show()

df1 = pd.read_csv("sheet.csv")
df2 = pd.read_csv("result.csv")
correct = 0
incorrect = 0

for i in range(0 , len(df1.index)):
    relevance1 = df1.loc[i , "Relevance"]
    relevance2 = df2.loc[i , "Relevance"]
    if relevance1 == relevance2 :
        correct += 1
    else:
        incorrect += 1
        print(i)

show(correct , incorrect)     

        