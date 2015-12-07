import json, csv
from flask import Flask, g, render_template, make_response

app = Flask(__name__)

########## TEST EXAMPLES ##########

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/template-test")
@app.route('/template-test/<name>')
def template_test(name=None):
    capitalized_name = name.upper()
    return render_template("template-test.html", test=capitalized_name)


########## SERVER-SIDE RENDERING ##########

@app.route("/incidents-server")
def template_server():
    data = list(csv.DictReader(open("dispatches.csv", 'rU')))
    return render_template("template-server.html", data=data)

########## CLIENT-SIDE RENDERING ##########

@app.route("/incidents-client")
def template_client():
    return render_template("template-client.html")

@app.route("/incidents.json")
def sample_json():

    data = list(csv.DictReader(open("dispatches.csv", 'rU')))

    # Turn the data into JSON
    json_string = json.dumps(data)

    # Return JSON to the browser
    response = make_response(json_string)
    response.headers['Content-Type'] = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)