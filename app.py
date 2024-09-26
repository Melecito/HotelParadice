from flask import Flask, request, render_template, url_for

from datetime import datetime

import chatBot_ok 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/service")
def service():
    return render_template('service.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')



@app.route("/guide")
def guide():
    return render_template('guide.html')

@app.route("/package")
def package():
    return render_template('package.html')

@app.route("/single")
def single():
    return render_template('single.html')

@app.route("/testimonial")
def testimonial():
    return render_template('testimonial.html')



if(__name__ == '__main__'):
    app.run(debug=True)