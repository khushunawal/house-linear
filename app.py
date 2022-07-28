import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('house-prices.pkl','rb')) 

@app.route('/')
def home():
      return render_template("index.html")
  
@app.route('/pr',methods=['GET'])
def pr():
  exp = float(request.args.get('exp'))
  prediction = model.predict([[exp]])
  return render_template('index.html', prediction_text='Regression Model  has predicted salary for given experinace is : {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)