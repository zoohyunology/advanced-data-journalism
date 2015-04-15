import json, csv
from flask import Flask, g, render_template, make_response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/json")
def sample_json():
    data = list(csv.DictReader(open("dispatches.csv", 'rU')))
    
    # data = {
    #     'bills': [
    #         {
    #             'title': "Modifies death certification laws to include advanced practice registered nurses, assistant physicians, and physician assistants",
    #             'created_at': "2015-02-26 01:37:57",
    #             'updated_at': "2015-04-10 00:55:33",
    #             'id': "MOB00007111",
    #             'chamber': "upper",
    #             'state': "mo",
    #             'session': "2015",
    #             'type': [
    #                 "bill"
    #             ],
    #             'subjects': [
    #                 "Transportation"
    #             ],
    #             'bill_id': "SB 517"
    #         }
    #     ]
    # }

    # Turn the data into JSON
    json_string = json.dumps(data)

    # Return JSON to the browser
    response = make_response(json_string)
    response.headers['Content-Type'] = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)