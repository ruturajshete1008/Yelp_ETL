from flask import Flask, render_template, jsonify
import pymongo
import pandas as pd
import twitter_scrape


app = Flask(__name__)


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.Yelp_ETL
collection = db.businesses


def serialize(array):
    """
    Changes MongoDB ID to string to be able to serialize as JSON.
    """
    serialized_list =[]
    for doc in array:
        doc['_id'] = doc['_id'].__str__()   
        serialized_list.append(doc)
    return serialized_list

@app.route("/")
def welcome():
    cities = collection.distinct('city')[0:9]
    # Render the template with the cities list passed in
    return render_template('index.html',cities=cities)

@app.route("/api/v1.0/business_data/<city>")
def city_data(city):
    businesses_city = collection.find({'city':city})

    return jsonify(serialize(businesses_city))

@app.route("/api/v1.0/business_data/<city>/<business_name>")
def biz_name(city,business_name):
    entry = collection.find({'city':city, 'name': business_name})
    item_counts = collection.count_documents({'city':city, 'name': business_name})

    if  item_counts == 0:
        return jsonify({"error" : "Business name not found. Search terms must be titlecased and contain proper spacing. ('Subway' instead of 'subway')"}), 404
    else:
        return jsonify(serialize(entry))
        
@app.route("/api/v1.0/business_data/<city>/<business_name>/tweets")
def tweets(city, business_name):
    entry = collection.find({'city':city, 'name': business_name})
    item_counts = collection.count_documents({'city':city, 'name': business_name})

    if  item_counts ==0:
        return jsonify({"error" : "Business name not found. Search terms must be titlecased and contain proper spacing. ('Subway' instead of 'subway')"}) ,404
    else:
        screen_name = entry[0]['twitter_handle']
        tweets = twitter_scrape.get_tweets(screen_name)
        return jsonify({"tweets" : tweets})



if __name__ == "__main__":
    app.run(debug=True)




# {'_id': ObjectId('5bc23ab19930080c1edfb5a7'),
#  'address': '211 W Monroe St',
#  'attributes': None,
#  'business_id': 'bFzdJJ3wp3PZssNEsyU23g',
#  'categories': 'Insurance, Financial Services',
#  'city': 'Phoenix',
#  'hours': None,
#  'is_open': 1,
#  'latitude': 33.4499993,
#  'longitude': -112.0769793,
#  'name': 'Geico Insurance',
#  'neighborhood': '',
#  'postal_code': '85003',
#  'review_count': 8,
#  'stars': 1.5,
#  'state': 'AZ'}

