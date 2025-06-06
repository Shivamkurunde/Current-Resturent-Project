from flask import Flask, render_template

app = Flask(_name_)

# Home route
@app.route('/')
def home():
    return render_template('home.html')  # templates/home.html

# Menu main page
@app.route('/menu')
def menu():
    return render_template('menu.html')  # templates/menu.html

# Veg menu section
@app.route('/menu/veg')
def veg():
    return render_template('menu-sections/veg.html')  # templates/menu-sections/veg.html

# Gym food section
@app.route('/menu/gym')
def gym():
    return render_template('menu-sections/gym.html')  # templates/menu-sections/gym.html

# Street chaat section
@app.route('/menu/street-chaat')
def street_chaat():
    return render_template('menu-sections/street-chaat.html')  # templates/menu-sections/street-chaat.html

# Ice Cream section (Optional: Add if you want this route too)
@app.route('/menu/ice-cream')
def ice_cream():
    return render_template('menu-sections/ice-cream.html')  # templates/menu-sections/ice-cream.html

if _name_ == '_main_':
    app.run(debug=True)