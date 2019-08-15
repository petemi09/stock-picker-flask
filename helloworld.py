from flask import Flask, request, render_template

import csv
import os
import random

app = Flask(__name__)

def run():
    dict1 = {}
    with open(os.path.join(os.path.dirname(__file__),'companylist.csv')) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        dict1["NUM"] = []
        dict1["ID"] = []
        dict1["NAME"] = []
        for row in csv_reader:
            if line_count == 0:                
                line_count += 1
            else:
                items = [line_count,row[0],row[1]]
                dict1["NUM"].append(items)
            line_count += 1
    randNum = random.choice(dict1["NUM"])
    return randNum

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      string = run()
      id1 = string[1]
      nameThing = string[2]
      return render_template('results.html', name=id1, other=nameThing)
   elif request.method == 'GET':
      return render_template('index.html')

