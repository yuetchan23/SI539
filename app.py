from flask import Flask, render_template

app = Flask(__name__)
#
@app.route("/")
def index():
    return render_template("index.html", name='index')

# @app.route("/gallery")
# def gallery():
#     return render_template("gallery.html", name='gallery')
#
# @app.route("/contact")
# def contact():
#     return render_template("contact.html", name='contact')
#
# @app.route("/about")
# def about():
#     return render_template("about.html", name='about')

@app.route('/<filename>')          							#get the URL variable
def home(filename):
    return render_template("%s.html" % filename, name = filename)	#The argument should be in templates folder


if __name__ == "__main__":
    app.run(debug=True)
