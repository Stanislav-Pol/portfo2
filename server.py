# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:47:40 2021
modfied 21 Nov 2021

@author: Stas
"""

from flask import Flask, render_template, request, redirect, send_from_directory
import os
from datetime import datetime
import csv

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def show_page(page_name=None):
    return render_template(page_name)

def write_to_csv(data):
    '''Write given data to the .CSV file'''
    with open("database.csv", newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        datetime = data['datetime']
        #Create csv_writer object
        #For MS Excel use ';' delimmeter
        csv_writer = csv.writer(database2, delimiter=';', 
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Write data via csv_writer
        csv_writer.writerow([email, subject, message, datetime])
        return 0


def write_to_file(data):
    '''Write given data to the .TXT file'''
    with open("database.txt", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        datetime = data['datetime']
        f_str = f'\n{email},{subject},{message},{datetime}'
        w_len = database.write(f_str)
    if w_len == len(f_str):
        return 0
    else:
        print("Write overflow or error")
        return -1

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            data['datetime'] = datetime.now()
            #write_to_file(data)
            write_to_csv(data)
            
            return redirect('/thank_you.html')
        except:
            return "Didn't save data. Some problame with file/database"
    else:
        return "Something went wrong. Try again!!"

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
# @app.route("/works.html")
# def works_page():
#     return render_template("works.html")

# @app.route("/about.html")
# def about_page():
#     return render_template("about.html")

# @app.route("/contact.html")
# def contact_page():
#     return render_template("contact.html")

# @app.route("/components.html")
# def components_page():
#     return render_template("components.html")


# @app.route("/favicon.ico")
# def favicon():
#     return url_for("favicon.png", filename="favicon.png")


# @app.route("/blog")
# def blog():
#     return "<h2>This is a blog page for crocodile</h2>"+"\n<p>Blog1</p>"

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "<h3>Blog about dog</h3>"+"\n<p>This is my dog</p>"