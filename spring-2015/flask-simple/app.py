import json, csv
from flask import Flask, g, render_template, make_response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/json")
def sample_json():

    data = list(csv.DictReader(open("dispatches.csv", 'rU')))

    # Turn the data into JSON
    json_string = json.dumps(data)

    # Return JSON to the browser
    response = make_response(json_string)
    response.headers['Content-Type'] = 'application/json'

    return response


@app.route("/map")
def crime_static():
    return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)
