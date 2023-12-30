from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="libManagement",
    port="3307"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/staff')
def staff():
    return render_template('staff.html')

@app.route('/book')
def book():
    cursor = db.cursor()
    query = "SELECT id,title,author,genre FROM books"
    cursor.execute(query)
    books = cursor.fetchall()  # Fetch all rows
    return render_template('book.html', books=books)


@app.route('/student')
def student():
    return render_template('student.html')




@app.route('/studentCol')
def studentCol():
    return render_template('studentCol.html')

@app.route('/add_staff', methods=['POST'])
def add_staff():
    name = request.form['name']
    position = request.form['position']
    department = request.form['department']

    # Inserting staff details into the database
    query = "INSERT INTO staff (name, position, department) VALUES (%s, %s, %s)"
    values = (name, position, department)
    cursor.execute(query, values)
    db.commit()

    return redirect('staffCol')



@app.route('/bookCol')
def bookCol():
    return render_template('bookCol.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']

    # Inserting book details into the database
    query = "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)"
    values = (title, author, genre)
    cursor.execute(query, values)
    db.commit()

    return redirect('bookCol')

@app.route('/staffCol')
def staffCol():
    return render_template('staffCol.html')



if __name__ == '__main__':
    app.run(debug=True)

