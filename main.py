import math
import os

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from flask import Flask, jsonify

app = Flask(__name__)

data=[]

@app.route('/')
def hello():
    di = {"message":'This is Cities List :-+-:',"data":data}
    return jsonify(di)


def getData():
    url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"
    response = requests.get(url)
    # Read the data (text format) from response.
    global data
    data = response.json()
    # with open("./test.txt",'w') as f:
    #     f.write(str(data))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getData()
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
