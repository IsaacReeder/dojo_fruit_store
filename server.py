from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print('strawberry', request.form['strawberry'])
    strawberry=request.form['strawberry']
    print('raspberry', request.form['raspberry'])
    raspberry=request.form['raspberry']
    print('apple', request.form['apple'])
    apple=request.form['apple']
    print('first_name', request.form['first_name'])
    first_name=request.form['first_name']
    print('last_name', request.form['last_name'])
    last_name=request.form['last_name']
    print('student_id', request.form['student_id'])
    student_id=request.form['student_id']
    return render_template("checkout.html", first_name=first_name, last_name=last_name, student_id=student_id, apple=apple, strawberry=strawberry, raspberry=raspberry)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True) 