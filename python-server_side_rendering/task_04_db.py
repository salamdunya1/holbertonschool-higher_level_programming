#!/usr/bin/python3

import json
import csv
import sqlite3
from os import error
from flask import Flask, render_template, request

app = Flask(__name__)

def read_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

def read_from_csv(file_path):
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        data = csv.DictReader(f)

        for item in data:
            item['id'] = int(item['id'])
            item['price'] = float(item['price'])

            data_list.append(item)

    return data_list

def fetch_from_sqlite(file_path):
    con = sqlite3.connect(file_path)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM Products")
    data = res.fetchall()


    products = [{"id": item[0], "name": item[1],
         "category": item[2], "price": item[3]} for item in data]

    con.close()

    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
            items = data.get('items', [])

    except FileNotFoundError:
        items = []

    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get("source", None)
    product_id = request.args.get("id", None)
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Invalid type has been entered for ID")

    if source == 'json':
        file_path = 'products.json'
        products = read_from_json(file_path)

    elif source == 'csv':
        file_path = 'products.csv'
        products = read_from_csv(file_path)

    elif source == 'sql':
        file_path = 'products.db'
        products = fetch_from_sqlite(file_path)
        
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products = [p for p in products if p['id'] == product_id]

        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
