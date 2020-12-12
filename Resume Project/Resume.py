from flask import Flask,render_template

app=Flask(__name__)


@app.route('/resumepage',methods=['GET', 'POST'])
def resumepage():
    return render_template('resume2.html')


if __name__ == '__main__':
    app.run(debug=True)
