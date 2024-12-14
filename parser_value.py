# csv parsing

# online resources
# https://docs.python.org/3/library/csv.html

import csv

def parse_parameters(genre):
    result = []

    with open('imdb-movie-data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        
        for row in reader:
            # print each row of the csv
            print(row)
            genres = row['Genre'].split(",")

            if genre in genres:

                result.append(row)
                print(row)
                #print("kdkdkd")
                break
            # pass genre from the csv
            # print(row['Genre'])
    
    return (result)

print(parse_parameters("Western"))

