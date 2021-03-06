"""
    Super Sprinter 3000
    A basic web server to store data about
    a teams Agile developement process
    by Gábor Koncz
"""


from flask import Flask, request, render_template, redirect, url_for
from data_manager import *


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/list', methods=["GET", "POST"])
def show_story_list():
    """
        Shows the list page, where the stories are
        displayed as a table.
    """
    stories = open_file()
    table_header = [
                    "ID",
                    "Story Title",
                    "User Story",
                    "Acceptance Criteria",
                    "Business Value",
                    "Estimation",
                    "Status",
                    "Edit",
                    "Delete"
                    ]
    return render_template("list.html", stories=stories, table_header=table_header)


@app.route("/story", methods=["GET"])
def create_story(story_ID=None):
    """
        Shows the form page, 
        where the user can add stories to the database.
    """
    return render_template("form.html", story_ID=story_ID)


@app.route('/story', methods=["POST"])
def add_story():
    """
        Adds the entries to the database
        what the user gives through the form.
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
    for element in form_elements:
        new_entries.append(request.form[element])
    stories.append(new_entries)
    write_to_file(stories)
    return redirect(url_for("show_story_list"))


@app.route("/story/<story_ID>", methods=["POST"])
def show_edit_story(story_ID=None):
    """
        Shows the form page where the forms are already filled in,
        based on the story_ID.
    """
    stories = open_file()
    story_ID = request.form["edit_button"]
    story_to_edit = []
    for story in stories:
        if story[0] == story_ID:
            for item in story:
                story_to_edit.append(item)
    return render_template("form.html", story_ID=story_ID, story_to_edit=story_to_edit)


@app.route("/edit", methods=["POST"])
def update_story():
    """
        Updates the entry specified by the story_ID.
    """
    stories = open_file()
    story_ID = request.form["update_button"]
    for row in stories:
        if row[0] == story_ID:
            stories.remove(row)
    editing_story = [story_ID]
    form_elements = [
                    "edited_story_title",
                    "edited_user_story",
                    "edited_accept_crit",
                    "edited_business_value",
                    "edited_estimation",
                    "edited_status"
                    ]
    for element in form_elements:
        editing_story.append(request.form[element])
    stories.append(editing_story)
    write_to_file(stories)
    return redirect(url_for('show_story_list'))


@app.route("/delete_story", methods=['POST'])
def delete_story():
    """
        Removes an entry from the specified file,
        based on the story_ID.
    """
    stories = open_file()
    story_ID = request.form["delete_button"]
    for story in stories:
        if story[0] == story_ID:
            stories.remove(story)
    write_to_file(stories)
    return redirect(url_for('show_story_list'))


if __name__ == "__main__":
    app.run(debug=True)
