from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/test/<username>')
def testing(username=None):
    return render_template('./index1.html', name=username)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('./thankyou.html')
    else:
        return 'Something went wrong. Try again'

# @app.route('/blog')
# def blog():
#     return 'This is my Blog.'

# #Actually flask won't execute this block, it execute Line 9 that block and forget the rest
# #However, Function names cannot be clashed
# @app.route('/blog')
# def blog2():
#     return 'This is my dog.'