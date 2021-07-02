from flask import Flask, render_template, send_from_directory, redirect, request
import os
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


def csv_writer(data):
    with open('database.csv', 'a', newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerow([data['name'], data['email'], data['message']])
    return 1


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        csv_writer(data)
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
