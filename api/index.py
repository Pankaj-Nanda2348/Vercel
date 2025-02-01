
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
    print(names)
    
    # Create an ordered dictionary to maintain the correct order of marks
    marks_dict = {student['name']: student['marks'] for student in data}
    
    # Collect the marks in the order of the requested names
    marks_list = [marks_dict.get(name, None) for name in names]  # Get marks in requested order
    
    print(marks_list)  # For debugging purposes
    
    return jsonify({"marks": marks_list})

if __name__ == "__main__":
    app.run(debug=True)


