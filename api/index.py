
from flask import Flask, request, jsonify
from flask_cors import CORS
import json



app = Flask(__name__)
CORS(app)


app.app_context().push()



with open("q-vercel-python.json", "r") as file:
    data = json.load(file)



@app.route('/api', methods = ['GET'])
def Marks():
    names = request.args.getlist("name")  # Get multiple "name" values from query params
    marks_list = [student["marks"] for student in data if student["name"] in names]

    return jsonify({"marks": marks_list})


if __name__ == "__main__":
    app.run(debug=True)


