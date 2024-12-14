# requirements

# online resources
# https://flask.palletsprojects.com/en/stable/api/

#Use flask
# import csv file

# genre classification
# filtering parameters
# routes -> action, adventure, comedy, drama, romance, 

import json
from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

def parse_parameters(genre):
    result = []

    with open('imdb-movie-data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        
        for row in reader:
            # print each row of the csv
            # print(row)

            # clean strings genres 
            genres = [g.strip().lower() for g in row['Genre'].split(",")]

            # "Action,Adventure,Sci-Fi"
            # genres are capitalized
            if genre and genre.lower() in genres:

                result.append(row)
                # print(row)
                #print("kdkdkd")
                # break
            # pass genre from the csv
            # print(row['Genre'])
    
    # return list of filtered movies and length for debugging purposes
    return result, len(result)
    # debugging length for proof
    #return result, len(result)

@app.route("/")
def root():

    #genre = request.args.get('genre')
    #movies = parse_parameters(genre)

    #return jsonify(movies)

    

    genre = request.args.get('genre')
    if genre:
        movies = parse_parameters(genre)
    else:
        # If no genre is provided, return all movies
        movies = parse_parameters(None)
    
    return jsonify(movies)


    # print(request.args.get('genre'))
    
    # list = {"hello": "everybody"}
    # return json.dumps(list)

# endpoint to handle genre parameters
# localhost:8080/romance    <romance> parameter

# online resources:
# https://www.geeksforgeeks.org/use-jsonify-instead-of-json-dumps-in-flask/


# take parameters in the url
@app.route("/<genre>", methods=['GET'])
def genre_parameter(genre):
    movies = parse_parameters(genre)
    return jsonify(movies)


app.run("0.0.0.0", port=8080)

# boilerplate script to run at import time
#if __name__ == "__main__":
    #app.run("0.0.0.0", port=8080)

    # debugging error connection
    #print("Hello, World!")