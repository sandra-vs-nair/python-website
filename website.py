# -----------------------------------------------------------
# Creating a website using python.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------
 
from flask import Flask, render_template

# Create a Flask instance.
app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home_page():
    return render_template("Website.html")

@app.route('/author')
def author():
    return render_template("author.html")

@app.route('/book')
def book():
    return render_template("book.html")

@app.route("/account", methods=['POST'])
def account():
    return render_template("account.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__=="__main__":
    app.run(debug=True)