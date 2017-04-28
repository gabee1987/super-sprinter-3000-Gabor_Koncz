"""
    Super Sprinter 3000
    A basic web server to store data about
    a teams Agile developement process
"""


from flask import Flask, request, render_template, redirect, url_for
from data_manager import *


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/list', methods=["GET", "POST"])
def show_story_list():
    stories = open_file()
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


@app.route("/story", methods=["GET"])
def create_story(story_ID=None):
    return render_template("form.html", story_ID=story_ID)


@app.route('/story', methods=["POST"])
def add_story():
    """
        Adds the entries what the user gives.
    """
    stories = open_file()
    new_entries = []
    new_entries.insert(0, ID_generator(stories))
    form_elements = [
                    "story_title",
                    "user_story",
                    "acceptance_criteria",
                    "business_value",
                    "estimation",
                    "status"
                    ]
    for name in form_elements:
        new_entries.append(request.form[name])
    stories.append(new_entries)
    write_to_file(stories)
    return redirect(url_for('show_story_list'))


@app.route("/story/<story_ID>", methods=["GET", "POST"])
def edit_story(story_ID=None):
    stories = open_file()
    story_ID = request.form['edit']
    ID = str(story_ID)
    story_to_edit = []
    for story in stories:
        if story[0] == ID:
            story_to_edit.append(story)
    return render_template("form.html", story_ID=story_ID, story_data=story_to_edit)


@app.route("/edit_story", methods=["GET", "POST"])
def update_story(story_ID, filename="database.csv"):
    """
        Update the entry specified by the story_ID.
    """
    stories = open_stories()
    story_ID = request.form['edit']
    ID = str(story_ID)
    editing_story = []
    editing_story.append(ID)
    form_elements = [
                    "story_title",
                    "user_story",
                    "acceptance_criteria",
                    "business_value",
                    "estimation",
                    "status"
                    ]
    for element in form_elements:
        editing_story.append(request.form[name])
    stories.append(new_entries)
    for element in stories:
        stories.remove(element)
        stories.insert(0, editing_story)
    write_to_file(stories)
    return redirect(url_for('show_story_list'))


def delete_story(story_ID, filename="database.csv"):
    """
        Removes an entry from the specified file.
    """
    stories = open_file()
    ID = request.form["delete"]
    for story in stories:
        if story[0] == ID:
            stories.remove(story)
    write_to_file(stories)
    return redirect(url_for('show_story_list'))










if __name__ == "__main__":
    app.run(debug=True)