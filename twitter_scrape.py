from splinter import Browser
from bs4 import BeautifulSoup as bs

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def text(x):
    """ 
    Deletes all '\n' instances in HTML text to clean it up. Requires a parsed BeautifulSoup object.
    """
    return x.text.replace('\n','')


# def random_element(x):
#     """
#     Takes in a list and returns a random element from the list.
#     If there's only one element, return first element.
#     """
#     if len(x) > 1:
#         return x[r.randint(0,len(x)-1)]
#     else:
#         return x[0]


def get_soup(url):
    """ 
    This function uses splinter and beautiful soup to serve you up a BeautifulSoup object to scrape from.
        Just hit it with your url of interest and you're all set.
        
    """
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    return soup   

def get_tweets(screen_name):
    """
    Returns a list of tweets from Mars weather Twitter page.
    Only returns tweets that have been loaded upon navigation to the page.
    """
    twitter_acc = get_soup(f"https://twitter.com/{screen_name}?lang=en")
    tweets = twitter_acc.find_all('div', class_="js-tweet-text-container")
    tweet_list = [text(tweet) for tweet in tweets]
        
    return tweet_list


