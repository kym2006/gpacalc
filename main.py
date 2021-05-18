import flask 
from flask import render_template
from flask.globals import request
import math
app=flask.Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/testing')
def testing():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/calculate')
def calculate():
    output="Thank you for submitting: " + str(request.args)
    gpa = 0
    for i in range(1, 4):
        gpa += float(request.args["mark"+str(i)]) * float(request.args["weightage"+str(i)])
    gpa/=float(sum([int(request.args["weightage"+str(i)]) for i in range(1,4)]))
    out=f"Score: {gpa}<br>"
    if math.ceil(gpa)>=80:
        out+="GPA: 4.0"
        return out 
    elif math.ceil(gpa)>=70:
        out+="GPA: 3.6"
        return out 
    elif math.ceil(gpa)>=65:
        out+="GPA: 3.2"
        return out 
    elif math.ceil(gpa)>=60:
        out+="GPA: 2.8"
        return out 
    elif math.ceil(gpa)>=55:
        out+="GPA: 2.4"
        return out 
    elif math.ceil(gpa)>=50:
        out+="GPA: 2.0"
        return out 
    else:
        out+="GPA: FAIL"
        return out 



app.run(host="0.0.0.0", port=8080, debug=True)


