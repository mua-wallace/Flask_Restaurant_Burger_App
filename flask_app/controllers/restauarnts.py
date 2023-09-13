from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.restaurant import Restaurant


@app.route('/resto_form')
def restaurant_form():
    return render_template('create_resto.html')

@app.route('/create_restaurant', methods=['POST'])
def create_restaurants():
    data = {
        "name":request.form['restaurant_name']
    }
    Restaurant.save(data)
    
    return redirect('/burgers')