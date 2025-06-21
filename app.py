from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/desserts')
def desserts():
    return render_template('Desserts.html')

@app.route('/ice-cream')
def ice_cream():
    return render_template('ice-cream.html')

@app.route('/Dessert-Icream')
def dessert_icecream():
    return render_template('Dessert-Icream.html')

@app.route('/gym-food')
def gym_food():
    return render_template('gym-food.html')

@app.route('/gym-protein')
def gym_protein():
    return render_template('gym-protein.html')

@app.route('/gym-detox')
def gym_detox():
    return render_template('gym-detox.html')

@app.route('/gym-shakes')
def gym_shakes():
    return render_template('gym-shakes.html')

@app.route('/street-chaat')
def street_chaat():
    return render_template('street-chaat.html')

@app.route('/veg')
def veg():
    return render_template('veg.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
