from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os
import pandas as pd

app = Flask(__name__)

# Path to the inventory JSON file
inventory_file = 'inventory.json'

# Load inventory data from JSON file
def load_inventory():
    if not os.path.exists(inventory_file):
        return []
    with open(inventory_file, 'r') as f:
        return json.load(f)

# Save inventory data to JSON file
def save_inventory(inventory):
    with open(inventory_file, 'w') as f:
        json.dump(inventory, f, indent=4)

# Generate low stock alerts
def get_low_stock_alerts(inventory, threshold=5):
    return [item for item in inventory if item['quantity'] <= threshold]

@app.route('/')
def index():
    inventory = load_inventory()
    low_stock_alerts = get_low_stock_alerts(inventory)
    return render_template('index.html', inventory=inventory, low_stock_alerts=low_stock_alerts)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        new_product = {
            'id': request.form['id'],
            'name': request.form['name'],
            'quantity': int(request.form['quantity']),
            'price': float(request.form['price'])
        }
        inventory = load_inventory()
        inventory.append(new_product)
        save_inventory(inventory)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    inventory = load_inventory()
    product = next((item for item in inventory if item['id'] == product_id), None)
    if request.method == 'POST':
        if product:
            product['name'] = request.form['name']
            product['quantity'] = int(request.form['quantity'])
            product['price'] = float(request.form['price'])
            save_inventory(inventory)
        return redirect(url_for('index'))
    return render_template('edit.html', product=product)

@app.route('/delete/<product_id>', methods=['GET'])
def delete_product(product_id):
    inventory = load_inventory()
    inventory = [item for item in inventory if item['id'] != product_id]
    save_inventory(inventory)
    return redirect(url_for('index'))

@app.route('/export/csv')
def export_csv():
    inventory = load_inventory()
    df = pd.DataFrame(inventory)
    df.to_csv('inventory.csv', index=False)
    return redirect(url_for('index'))

@app.route('/export/excel')
def export_excel():
    inventory = load_inventory()
    df = pd.DataFrame(inventory)
    df.to_excel('inventory.xlsx', index=False)
    return redirect(url_for('index'))

# HTML templates
@app.route('/template/<template_name>')
def get_template(template_name):
    return render_template(template_name)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
