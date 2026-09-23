from datetime import datetime
from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')
def home():
    #This gets the current date and time to display on the page
    today=datetime.now().strftime("%B %d, %Y")
    return render_template('index.html',current_time=today)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def contact():
    #This list stores your items. you can add more items here anytime!!
    products = [
        {
            "id": 1,
            "name": "Classic t-shirt",
            "price": 70,
            "description": "Comfortable shirt",
            "image": "T-shirt.png"
        },
        {
            "id": 2,
            "name": "Minimalist Backpack",
            "price": 100,
            "description": "Waterproof design",
            "image": "Backpack.png"
        },
        {
            "id": 3,
            "name": "Leather Wallet",
            "price": 40,
            "description": "Slim, Genuine leather wallet with RFID protection",
            "image": "Wallet.png"
        }
    ]

    #We pass the 'products' list into the HTML template
    return render_template('shop.html',items=products)


if __name__ == '__main__':
    app.run(debug=True)




