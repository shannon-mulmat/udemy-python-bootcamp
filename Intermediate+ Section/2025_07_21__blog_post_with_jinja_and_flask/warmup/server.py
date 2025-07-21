"""
Topics Covered:
- Jinja
- API refresh

Completed: 7/21/2025
"""

from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.today().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    sex_url = f'https://api.genderize.io?name={name}'
    sex_response = requests.get(sex_url)
    sex_data = sex_response.json()
    sex = sex_data["gender"]
    age_url = f'https://api.agify.io?name={name}'
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template('guess.html', name=name, sex=sex, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/5abcca6f4e39b4955965'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
