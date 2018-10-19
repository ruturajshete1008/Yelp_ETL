from flask import Flask, render_template, jsonify
import pymongo
import pandas as pd
import json
from bson import json_util
import json
from bson import ObjectId
from pprint import pprint


app = Flask(__name__)


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.Yelp_ETL
collection = db.businesses

@app.route("/")
def welcome():
    cities = collection.distinct('city')[0:9]
    # Render the template with the cities list passed in
    return render_template('index.html',cities=cities)

@app.route("/api/v1.0/business_data/<city>")
def city_data(city):
    businesses_city = collection.find({'city':city})
    serialized_list =[]
    for doc in businesses_city:
        doc['_id'] = doc['_id'].__str__()   
        serialized_list.append(doc)

    return jsonify(serialized_list)

@app.route("/api/v1.0/business_data/<city>/<business_name>")
def biz_name(city,business_name):
    entry = collection.find_one({'city': city, 'name': business_name})
    entry['_id'] = entry['_id'].__str__()
    return jsonify(entry)


# @app.route("/api/v1.0/business_data")
# def business_data():
#     """
#     Return the business twitter and yelp data as json
#     """

#     return jsonify(business_data)



# @app.route("/api/v1.0/business_data/<business_name>")
# def business_name(business_name):
#     """Fetch the business whose name matches the path variable supplied by the user, or a 404 if not."""

#     canonicalized = business_name.replace(" ", "").lower()
#     for character in business_data:
#         search_term = character["name"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": f"Character with real_name {real_name} not found."}), 404


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

