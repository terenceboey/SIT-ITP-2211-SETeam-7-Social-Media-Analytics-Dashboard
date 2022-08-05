from pathlib import Path
import os
import pandas as pd

def countTopic(filename,camp):
    path = f"C:\\Users\\65866\\MLSTUFF\\ta_result2\\{camp}\\{filename}"
    df = pd.read_csv(path)
    return int(df[df.columns[0]].count())-1

def cleanTopicCSVbyPath(filename,camp):
    path = f"C:\\Users\\65866\\MLSTUFF\\ta_result2\\{camp}\\{filename}"
    df = pd.read_csv(path)
    newColumn = []
    for i in range(len(df.index)):
        newString = df['WordScore'][i].replace("'", '').replace(
            "[", '').replace("]", '').replace("(", '').replace(")", '').replace(".", '')
        cleanString = "".join(filter(lambda x: not x.isdigit(), newString)).replace(
            ", ,", " ").replace(",", "")
        wordArray = cleanString.split("  ")
        newColumn.append(wordArray)
    df['TopicWords'] = newColumn
    df['TopicInterpretation'] = ""
    df.to_csv(path, index=False)

def goCrazy():
    camp = 'appreciate'
    countryList = os.listdir(f"C:\\Users\\65866\\MLSTUFF\\ta_result2\\{camp}")
    overview = pd.read_csv(f'C:\\Users\\65866\\MLSTUFF\\ta_result2\\overall_{camp}_topics.csv')
    overview['positive_topics'] = 0
    overview['negative_topics'] = 0
    overview['neutral_topics'] = 0

    for k in countryList:
        print(f"doing {k}")
        try:
            path = "\\"+k+"\\" + "topicinfo_"+camp+"_" + k + "_negative.csv"
            # cleanTopicCSVbyPath(path)
            overview.loc[overview.Country==k,'negative_topics']= countTopic(path,camp)
        except:
            print("Missing negative")

        try:
            path = "\\"+k+"\\" + "topicinfo_"+camp+"_" + k + "_positive.csv"
            # cleanTopicCSVbyPath(path)
            overview.loc[overview.Country==k,'positive_topics']= countTopic(path,camp)
        except:
            print("Missing positive")

        try:
            path = "\\"+k+"\\" + "topicinfo_"+camp+"_" + k + "_neutral.csv"
            # cleanTopicCSVbyPath(path)
            overview.loc[overview.Country==k,'neutral_topics']= countTopic(path,camp)
        except:
            print("Missing neutral")

        print(f"done {k}")
    print(overview)
    overview.to_csv(f'C:\\Users\\65866\\MLSTUFF\\ta_result2\\overall_{camp}_topics_count.csv')


def goCrazy2():
    camp = 'appreciate'
    countryList = os.listdir(f"C:\\Users\\65866\\MLSTUFF\\ta_result2\\{camp}")
    for k in countryList:
            print(f"doing {k}")
            try:
                path = "\\"+k+"\\" + "topicinfo_"+camp+"_" + k + "_negative.csv"
                cleanTopicCSVbyPath(path,camp)
            except:
                print("Missing negative")

            try:
                path = "\\"+k+"\\" + "topicinfo_"+camp+"_" + k + "_positive.csv"
                cleanTopicCSVbyPath(path,camp)
            except:
                print("Missing positive")

            try:
                path = "\\"+k+"\\" + "topicinfo_"+camp+"_" + k + "_neutral.csv"
                cleanTopicCSVbyPath(path,camp)
            except:
                print("Missing neutral")

            print(f"done {k}")

# goCrazy()
goCrazy()
