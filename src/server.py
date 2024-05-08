from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def dynamic_render(page_name):
    return render_template(f"{page_name}.html")

@app.route("/submit_form", methods=['POST'])
def submit_form():
    if request.method == "POST":
        return redirect("thankyou")
    return "Something went wrong. Please try again."
