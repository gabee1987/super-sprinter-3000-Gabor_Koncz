"""
    Super Sprinter 3000
    A basic web server to store data about
    a teams Agile developement process
"""


from flask import Flask, request, render_template
from data_manager import *


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/list', methods=["GET", "POST"])
def show_story_list():
    stories = open_file("database.csv")
    table_header = [
                    "ID",
                    "Story Title",
                    "User Story",
                    "Acceptance Criteria",
                    "Business Value",
                    "Estimation",
                    "Status",
                    "Action"
                    ]
    return render_template("list.html", stories=stories, table_header=table_header)


@app.route('/story', methods=['GET', 'POST'])
@app.route('/story/<story_ID>')
def create_story(story_ID=None):
    if story_ID:
        editing_story = open_file(story_ID)
        return render_template("form.html", story_ID=story_ID)
    return render_template("form.html", story_ID="")







if __name__ == "__main__":
    app.run(debug=True)