#Import Libraries
from flask import Flask, request, render_template,jsonify
 
import model # load model.py
 
app = Flask(__name__)



# render htmp page
@app.route('/')
def home():
    return render_template('index.html')
 
# get user input and the predict the output and return to user
@app.route('/predict',methods=["POST"])

     
    #take data from form and store in each feature   

def predict():
    if request.method == "POST":
        sqft = float(request.form['sqft'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        loc = request.form.get('loc')
        area = request.form.get('area')
        availability = request.form.get('avail') 
        balcony=3
        price_per_sqft=8514.285714

 
     
    # predict the price of house by calling model.py
    predicted_price = model.predict_house_price(bath, balcony, sqft, bhk,price_per_sqft,area,availability,loc)       
 
 
    # render the html page and show the output
    return render_template('index.html', prediction_text='Predicted Price of Bangalore House is {}'.format(predicted_price))
 
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
     
if __name__ == "__main__":
    app.run()