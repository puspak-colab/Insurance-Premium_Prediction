# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 10:24:16 2021

@author: PUSPAK
"""

# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'insurance_premium_model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        
        bmi = float(request.form['bmi'])
        
        sex=request.form['sex']
        if(sex=='Male'):
            sex=1
        else:
            sex=0	
        
        smoker=request.form['smoker']
        if(smoker=='Yes'):
            smoker=1
        else:
            smoker=0	
        
        children = int(request.form['children'])
        
        region=request.form['region']
        if(region=='NorthEast'):
            region=0
        elif(region=='NorthWest'):
            region=1
        elif(region=='SouthEast'):
            region=2
        else:
            region=3
                   
        data = np.array([[age, bmi, sex, smoker, children, region]])
        pred = regressor.predict(data)
        
        return render_template('result.html', prediction="Your Insurance Premium should be near about:"+" "+"$"+str(np.round(pred,2)))

if __name__ == '__main__':
	app.run(debug=True)