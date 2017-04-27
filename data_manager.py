"""
    Data manager for Super Sprinter 3000
    loads,saves,modifies data in specified file
"""


from flask import Flask
import csv


def ID_generator():
    """
        Generates an ID for the entries.
        Loads the output of show_stories,
        checks the line number of it and adds 1 to it.
    """
    stories = open_file()
    return len(table) + 1


def open_file(filename="database.csv"):
    """
        Opens the specified file to show its content.
        Reads it content as rows.
    """
    try:
        with open(filename, 'r') as workfile:
            row = workfile.readlines('\n')
            file_items = [item.split(';') for item in row]
            return file_items
    except FileNotFoundError:
        file_items = None


def write_to_file(stories, filename="databse.csv"):
    """
        Saves data to the specified file.
        Write the entry as rows.
    """
    with open(filename, 'w') as workfile:
        for item in stories:
            row = ';'.join(item)
            workfile.write(row + '\n')


def add_story(filename="database.csv"):
    """
        Adds the entries what the user gives.
    """
    stories = open_file()
    new_entries = []
    new_entries.insert(0, ID_generator())
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


def delete_story(filename="database.csv"):
    """
        Removes an entry from the specified file.
    """
    stories = open_file()
    ID = request.form["delete"]
    for story in stories:
        if story[0] == ID:
            stories.remove(story)
    write_to_file(stories)


def update_story(story_ID, filename="database.csv"):
    """
        Update the entry specified by the story_ID.
    """
    stories = show_stories()
    story_ID = request.form['edit']





