# Yelp_ETL

## Project Description:
## Bridging the gap between yelp and twitter data: 
* The goal of this application is to create API which can query data collected from yelp and twitter for a particular business.
* we can pull business reviews and ratings from both sources.
* This application returns business reviews and tweets in the form of json.
* we are trying to gather reviews from yelp account and tweets from twitter accounts of individual businesses
* Using flask, these results will be displayed on dynamic web pages. 
* We also want to analyze relationship between yelp rating and twitter tweets content and count.

## Project Team:
Rafael Santa Cruz
Ruturaj Shete
Mehrun Nisha

## Tools used:
 MongoDB, Twitter API, Kaggle Yelp Data Files, Flask, PyMongo, HTML, CSS

## Project Phases:
#ETL Process

Data Extract: read the data, often from multiple sources

Transform: clean and structure the data in desired form

Load: write the data into a database for storage

## Data Source 
*  We wanted to use data directly from Yelp. However, yelp API is very restrictive about its access to data.
   We had no choice but to use yelp academic dataset from kaggle.
   The dataset is in the form of JSON files

* Following ten cities based on number of businesses in the dataset were selected.

Las Vegas     23535
Phoenix       15472
Charlotte      7740
Scottsdale     7138
Pittsburgh     5615
Mesa           5343
Henderson      3984
Tempe          3569
Chandler       3519
Gilbert        2937

## Transformation Process
  The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc.).
  Data cleansing and transformation was done by python in Jupyter Notebook.

## Database used to store information 
* Python script and twitter API were used to collect twitter account for the businesses in the dataset.
* After cleansing and transformation, data from json files were saved in Mongo Database.
   It is a list of businesses along with city and state.

## Steps to follow while querying
* User must type the business title cased and include all spaces necessary (`El Pollo Loco` vs `elpolloloco`).
* Also, this application assumes the user has twitter handles and yelp account names which are loaded into mongo db.
* Yelp does not allow scraping on their website, therefore we had to use this method. Also, since twitter api key is not required 
* anyone can use this * application without having to generate their own api key.
* The tweets returned are the latest tweets. All of the tweets from the landing page are returned as a JSON object.

# Flask Routes:

* Routes based on city name: It would be a detail of businesses in the city
* Routes based on business name in a particular city: It would return tweets for a particular business in a city.

## Reference:
https://github.com/ruturajshete1008/Yelp_ETL.git

https://www.kaggle.com/yelp-dataset/yelp-dataset

https://confluence.atlassian.com/bitbucket/branching-a-repository-223217999.html 


