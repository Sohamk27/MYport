from flask import Flask,render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('info.txt', mode='a') as info:
        email = data['Email']
        subject = data['Subject']
        name = ['Name']
        file = info.write(f'\n{email}, {subject}, {name}')
        return file

def write_to_csv(data):
    with open('database.csv', mode='a') as info2:
        email = data['Email']
        subject = data['Subject']
        name = ['Name']
        csv_writer = csv.writer(info2, delimiter=",", newline='', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, name])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data = request.form.to_dict()
        write_to_csv(data)
        write_to_file(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return "try again"