from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def Hello():
    return '<h1>Salam</h1>'

@app.route("/Rehman")
def Rehman():
    return render_template("index.html")

@app.route("/Ravi")
def Ravi():
    return render_template("ravi.html")    

@app.route("/Elmar")
def Elmar():
    return render_template("elmar.html")

@app.route("/Sebuhi")
def Sebuhi():
    return render_template("sebuhi.html")

@app.route("/Fezail")
def Fezail():
    return render_template("fezail.html")

@app.route("/SamirMuellim")
def Samir():
    return render_template("Samir_muellim.html")



if __name__=='__main__':
    app.run(debug=True)