#Import Libraries
from flask import Flask, request, render_template, jsonify
import BangaloreModel as tm

import BangaloreModel # load model.py
 
app = Flask(__name__)
 
# render htmp page
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': tm.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_area_names', methods=['GET'])
def get_area_names():
    response = jsonify({
        'area': tm.get_area_values()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_availability_names', methods=['GET'])
def get_availability_names():
    response = jsonify({
        'availability': tm.get_availability_values()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
     
    #take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    print(input_features)
    bath = input_features[0]
    balcony = input_features[1]
    total_sqft_int = input_features[2]
    bhk = input_features[3]
    price_per_sqft = input_features[4]
    area_type = input_features[5]
    availability = input_features[6]
    location = input_features[7]
     
    # predict the price of house by calling model.py
    predicted_price = BangaloreModel.predict_house_price(bath,balcony,total_sqft_int,bhk,price_per_sqft,area_type,availability,location)       
 
 
    # render the html page and show the output
    return render_template('index.html', prediction_text='Predicted Price of Bangalore House is {:.2f} lacs'.format(predicted_price))
 
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
     
if __name__ == "__main__":
    app.run()