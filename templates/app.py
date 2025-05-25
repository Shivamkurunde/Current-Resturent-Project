from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sectionHome')
def section_home():
    return render_template('home.html')

@app.route('/sectionVeg')
def section_veg():
    return render_template('menu-sections/veg.html')

# Add similar routes for all other sections

if __name__ == '__main__':
    app.run(debug=True)