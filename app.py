from flask import Flask, render_template


app = Flask("__main__")

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/features/")
def features():
    return render_template('features.html')


@app.route("/Case/")
def case():
    return render_template('case.html')


@app.route("/resources/")
def resource():
    return render_template('resource.html')


@app.route("/contact/")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5150)