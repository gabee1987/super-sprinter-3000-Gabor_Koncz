"""
    Super Sprinter 3000
    A basic web server to store data about
    a teams Agile developement process
"""


from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/list')
def story_list():
    









if__name__ == "__main__":
    app.run(debug=True)