
from flask import Flask, request, jsonify
from flask_cors import CORS
import json



app = Flask(__name__)
CORS(app)


app.app_context().push()



with open("q-vercel-python.json", "r") as file:
    data = json.load(file)
    # print(data)


@app.route('/api')
def Welcome():
    all_students = data
    return all_students

@app.route('/a', methods = ['GET'])
def Students():
    all_students = data
    l = []
    for student in all_students:
        output = {student['name'] : student['marks']}
        l.append(output)
    return ("Welcome" , output)

@app.route('/', methods = ['GET'])
def Marks():
    names = request.args.getlist("name")  # Get multiple "name" values from query params
    marks_list = [student["marks"] for student in data if student["name"] in names]

    return jsonify({"marks": marks_list})


if __name__ == "__main__":
    app.run(debug=True)


