from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/index.html')
def my_home2():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page_name(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def email():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            with open('./database.txt', mode='a') as my_file:
                # text = my_file.write("\n"+", ".join(data.values()))
                write_to_csv(data)
            return render_template('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return render_template('contact.html', error=error)


def write_to_csv(data):
    with open('./database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
