from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import logging
import table
app = Flask(__name__)
logging.basicConfig(filename='application.log', level=logging.INFO,
    format='%(levelname)s:%(message)s')

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'database-2.cshux5aaxeaw.us-east-1.rds.amazonaws.com' 
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'rishi123'
app.config['MYSQL_DB'] = 'reg'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        logging.info(name)
        age = details['age']
        email = details['email']
        phone = details['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO information(name, age, email, phone) VALUES (%s, %s, %s, %s)", (name, age, email, phone))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM information")
    if resultValue >0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
