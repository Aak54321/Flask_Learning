from flask import Flask,render_template,url_for,redirect,request
#initializing the flask app
app = Flask(__name__)
#adding the default home page a static directory
@app.route("/")
def home():
   return render_template("base.html")
#setting the route for login page along with the methods to be used
@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        #fetch the name what you got entered
        user_name = request.form["n"]
        #put it to the respective page
        return redirect(url_for("msg",uname = user_name))
    else:
        return render_template("login.html")
@app.route("/<uname>")
def msg(uname):
    return render_template("post_login.html",content = uname)

if __name__ == "__main__":
    app.run(debug = True)

