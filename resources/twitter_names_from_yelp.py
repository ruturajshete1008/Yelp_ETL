
# coding: utf-8

# In[61]:


import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret
import json
import pandas as pd
from pprint import pprint
import time
import csv


# In[117]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# In[116]:


def csv_to_df(csv):
    return pd.DataFrame(pd.read_csv(csv))


# In[64]:


def append_csv(data, filename):
    with open(filename, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)


# In[114]:


def scrape_users(index_start,index_end, infile, outfile):
    """
    This function appends a CSV with Twitter handles for a given Yelp Business. 
    Search queries are Yelp Businesses in this case.
    User specifies how many items to iterate through via 'index_end'
    """
    start = index_start
    api_call_count = 0
    business_names = csv_to_df(infile)

    while index_start < index_end:
        try:
            # Iterate through specified index range
            for index in business_names.index[index_start:index_end]:
                twitter_handles = []                
                # Initialize scraping
                if index_start == start:
                    print('(Re)Initializing Twitter Screen Name Scrape...')
                    
                # Searching by name of business. Value is obtained by locating value for 'name' column for the given row
                search_query = business_names.iloc[index]['name']
                users = api.search_users(search_query,1,1, wait_on_rate_limit = True)

                if users == []:
                    twitter_handles.append(index_start)
                    twitter_handles.append("NaN")
                    print(f"No result found for {search_query}. Appending NaN...")
                else:
                    twitter_handles.append(index_start)
                    twitter_handles.append(users[0].screen_name)
                    print(f"{search_query}'s Twitter search returned {users[0].screen_name}. Appending...")

                # Append results as they come to a csv. Index on csv will match index list on Yelp dataframe.
                append_csv(twitter_handles,outfile)
                    
                # My API settings only allow for 900 requests every 15 minutes (900 seconds).
                # That comes out to 1 request/second, so make request every 1.1 seconds to not get rate limit errors.
                time.sleep(1.1)
                
                index_start +=1
                api_call_count+=1

                if api_call_count == 899:
                    print('We have appended 899 items and hit the rate limit for now. Sleeping until Twitter rate limit is reset...')
                    api_call_count = 0
                    
        except tweepy.TweepError as e:
            print(e)

    if index_start == index_end:
        return str(outfile)
        print("Scraping complete!")


# In[118]:


# calls on function to scrape all twitter users. test function.
# scrape_users(30, 40,'business_name.csv','test.csv')


# ## Manipulating Twitter Data and Merging Yelp+Twitter Dataframes
# 

# In[68]:


# Yelp business names were read in at the top of the notebook.
biz_names = csv_to_df('business_name.csv')
biz_names.head()


# In[119]:


# Read in our data as a dataframe.
twitter = csv_to_df('twitter_handles_0-78852.csv')
twitter.head()


# In[70]:


# Set the index to the index provided in the csv to properly join dataframes.
twitter = twitter.rename( columns = {'Unnamed: 1': 'twitter_handle','Items 0-52566': 'index'}).set_index('index')


# In[71]:


twitter.head()


# In[72]:


# Inner join twitter handles with business names based on their index.
merged_df = biz_names.merge(twitter, left_index=True,right_index=True)
# Clean up the dataframe to drop null values
merged_df = merged_df.dropna(how='any').reset_index(drop=True)


# In[73]:


merged_df.head(20)


# In[91]:


# Export our dataframe to csv
# merged_df.to_csv('YelpBiz_TwitterHandles.csv')


# In[90]:


# def documentArray(filename):
#     array = []
#     for row in merged_df.index[]:
#         p = merged_df.iloc[row,:].to_dict()
#         test_list.append(p)

#     pprint(test_list)

