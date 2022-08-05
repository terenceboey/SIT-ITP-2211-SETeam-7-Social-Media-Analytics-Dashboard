from distutils.command import clean
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import re
import string
import emoji
import numpy as np
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import os
from pathlib import Path
from cleantext import clean
import torch

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')


#downloads for nltk
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('stopwords')
#nltk.download('omw-1.4')

stopword = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


def getProjectDir():
    proj_dir = Path(__file__).parent
    return proj_dir


def getCountryList():
    # append names of countries into list
    countryNameData = pd.read_csv(
        "countries_final_nikos.csv", low_memory=False)
    countriesList = countryNameData["name"].tolist()
    return countriesList


def load_data_csv(csv_string):
    data = pd.read_csv(csv_string)
    return data


def remove_emoji(text):
    text = clean(text, no_emoji=True)
    return text


def remove_mult_spaces(text):  # remove multiple spaces
    return re.sub("\s\s+", " ", text)

# clean hashtags at the end of the sentence, and keep those in the middle of the sentence by removing just the # symbol


def clean_hashtags(tweet):
    new_tweet = " ".join(word.strip() for word in re.split(
        '#(?!(?:hashtag)\b)[\w-]+(?=(?:\s+#[\w-]+)*\s*$)', tweet))  # remove last hashtags
    # remove hashtags symbol from words in the middle of the sentence
    new_tweet2 = " ".join(word.strip() for word in re.split('#|_', new_tweet))
    return new_tweet2

# filter special characters such as & and $ present in some words


def filter_chars(a):
    sent = []
    for word in a.split(' '):
        if ('$' in word) | ('&' in word):
            sent.append('')
        else:
            sent.append(word)
    return ' '.join(sent)


def remove_punct(text):
    text = text.replace('\r', '').replace('\n', ' ').replace(
        '\n', ' ').lower()  # remove \n and \r and lowercase
    # remove links and mentions
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    # remove non utf8/ascii characters such as '\x9a\x91\x97\x9a\x97'
    text = re.sub(r'[^\x00-\x7f]', r'', text)
    banned_list = string.punctuation + 'Ã'+'±'+'ã'+'¼'+'â'+'»'+'§'
    table = str.maketrans('', '', banned_list)
    text = text.translate(table)

    return text


def clean_tweet(text):
    text = remove_emoji(text)
    text = remove_punct(text)
    text = clean_hashtags(text)
    text = filter_chars(text)
    text = remove_mult_spaces(text)

    return text


def tokenization(text):
    text = re.split('\W+', text)
    return text


def remove_stopword(text):
    text = [word for word in text if word not in stopword]
    return text


def stemming(text):
    text = [stemmer.stem(word) for word in text]
    return text


def lemmatizing(text):
    s = [lemmatizer.lemmatize(word) for word in text]
    return text


def cleaning_tweet(dataframe):

    dataframe['Cleaned_Tweet'] = dataframe['Tweet'].apply(
        lambda x: clean_tweet(x))

    dataframe['Tweet_tokenized'] = dataframe['Cleaned_Tweet'].apply(
        lambda x: tokenization(x))

    dataframe['Tweet_removed_stop_word'] = dataframe['Tweet_tokenized'].apply(
        lambda x: remove_stopword(x))

    dataframe['Tweet_stemmed'] = dataframe['Tweet_removed_stop_word'].apply(
        lambda x: stemming(x))

    dataframe['Tweet_lemmatized'] = dataframe['Tweet_removed_stop_word'].apply(
        lambda x: lemmatizing(x))


def clean_campaign_csvs():
    list_of_country = getCountryList()
    root_dir = getProjectDir()
    campaign_category = ['appreciate_campaign', 'gifts_campaign',
                         'donation_campaign', 'benefits_campaign', 'support_campaign']
    for j in range(len(campaign_category)):
        campaign_dir = str(root_dir) + "\\campaign_category_results"
        campaign_subdir = campaign_dir + f"\\{campaign_category[j]}"
        for i in range(len(list_of_country)):
            filtered_path = campaign_subdir + "\\" + \
                campaign_category[j] + "_" + f'{list_of_country[i]}.csv'
            print(f"currently doing {campaign_category[j]}")
            dummyList = []
            for chunk in pd.read_csv(
                    filtered_path, on_bad_lines='skip', low_memory=False, chunksize=10000):
                dummyList.append(chunk)
            tweet_df = pd.concat(dummyList, axis=0)
            del dummyList
            cleaning_tweet(tweet_df)
            tweet_df.to_csv(filtered_path, encoding='utf-8', index=False)
            print(f"{list_of_country[i]} for {campaign_category[j]} done")

def labelCountry():
    list_of_country = getCountryList()

    root_dir = getProjectDir()

    campaign_category = ['appreciate_campaign', 'gifts_campaign',
                     'donation_campaign', 'benefits_campaign', 'support_campaign']

    for j in range(len(campaign_category)):
        campaign_dir = str(root_dir) + "\\campaign_category_results"
        campaign_subdir = campaign_dir + f"\\{campaign_category[j]}"
        for i in range(len(list_of_country)):
            filtered_path = campaign_subdir + "\\" + \
                campaign_category[j] + "_" + f'{list_of_country[i]}.csv'
            print(f"currently doing {campaign_category[j]}")
            dummyList = []
            for chunk in pd.read_csv(
                    filtered_path, on_bad_lines='skip', low_memory=False, chunksize=10000):
                dummyList.append(chunk)
            tweet_df = pd.concat(dummyList, axis=0)
            del dummyList
            tweet_df["Country"] = f"{list_of_country[i]}"
            tweet_df.to_csv(filtered_path, encoding='utf-8', index=False)
            print(f"{list_of_country[i]} for {campaign_category[j]} done")
            

def combineCampaign():
    
    list_of_country = getCountryList()
    root_dir = getProjectDir()
    campaign_category = ['appreciate_campaign', 'gifts_campaign',
                     'donation_campaign', 'benefits_campaign', 'support_campaign']
    combined_df = pd.DataFrame()
    
    for j in range(len(campaign_category)):
        campaign_dir = str(root_dir) + "\\campaign_category_results"
        campaign_subdir = campaign_dir + f"\\{campaign_category[j]}"
        for i in range(len(list_of_country)):
            filtered_path = campaign_subdir + "\\" + \
                campaign_category[j] + "_" + f'{list_of_country[i]}.csv'
            print(f"currently doing {campaign_category[j]}")
            dummyList = []
            for chunk in pd.read_csv(
                    filtered_path, on_bad_lines='skip', low_memory=False, chunksize=10000):
                dummyList.append(chunk)
            df = pd.concat(dummyList, axis=0)
            combined_df = pd.concat([combined_df, df])
            combined_df.to_csv(f"{campaign_category[j]}" + "_combined")
            print(f"{list_of_country[i]} for {campaign_category[j]} done")

def sentiment_score(cleaned_tweet):
    tokens = tokenizer.encode(cleaned_tweet, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits)) + 1

            
def clean_healthcare_worker_csvs():
    list_of_country = getCountryList()
    root_dir = getProjectDir()
    health_dir = str(root_dir) + "\\healthcare_worker_filtered_results"

    for i in range(len(list_of_country)):
        health_path = health_dir + f"\\healthcare_worker_filtered_{list_of_country[i]}.csv"
        print(f"currently doing {health_path}")
        dummyList = []
        for chunk in pd.read_csv(
                health_path, on_bad_lines='skip', low_memory=False, chunksize=10000):
            dummyList.append(chunk)
        tweet_df = pd.concat(dummyList, axis=0)
        del dummyList
        cleaning_tweet(tweet_df)
        tweet_df.to_csv(health_path, encoding='utf-8', index=False)
        print(f"{health_path} done")

def assign_sentiment_healthCSV():
    list_of_country = getCountryList()
    root_dir = getProjectDir()
    health_dir = str(root_dir) + "\\healthcare_worker_filtered_results"
    for i in range(len(list_of_country)):
        health_path = health_dir + f"\\healthcare_worker_filtered_{list_of_country[i]}.csv"
        df = pd.read_csv(health_path, on_bad_lines='skip', low_memory=False)
        if "sentiment" in df:
            print(f"sentiment already assigned for {list_of_country[i]}, {health_path}")
            continue
        else:
            print("doing " + f"{list_of_country[i]}")
            df['sentiment'] = df['Cleaned_Tweet'].apply(lambda x: sentiment_score(x))
            df.to_csv(health_path, encoding='utf-8', index=False)
            print(f"{health_path} done")


def single_assign_sentiment_healthCSV(country_name):
    # make sure country name is the same as in countries_final-original. follow upper and lower case.
    root_dir = getProjectDir()
    health_dir = str(root_dir) + "\\healthcare_worker_filtered_results"
    health_path = health_dir + f"\\healthcare_worker_filtered_{country_name}.csv"
    df = pd.read_csv(health_path, on_bad_lines='skip', low_memory=False)
    if "sentiment" in df:
        print(f"sentiment already assigned for {country_name}, {health_path}")
    else:
        print(f"currently doing {health_path}")
        df['sentiment'] = df['Cleaned_Tweet'].apply(lambda x: sentiment_score(x))
        df.to_csv(health_path, encoding='utf-8', index=False)
        print(f"{health_path} done")
        
        
single_assign_sentiment_healthCSV("Spain")