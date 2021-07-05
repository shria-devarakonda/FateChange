from flask import Flask,render_template,request

app2 = Flask("__name__")

@app2.route("/", methods =["GET", "POST"])
def index():
    if request.method =="POST":
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        return('<h1>'+name+"ius poopius is your new name and "+name+'@poop.poop is your new email id. '+ email+ ' is a bad email.' +' Refresh page for trying a new name and mail.</h1>')
    return render_template('index.html')

if __name__ == "__main__":
    app2.run(debug=True)
