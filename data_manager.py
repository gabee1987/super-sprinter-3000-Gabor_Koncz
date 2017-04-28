"""
    Data manager for Super Sprinter 3000
    loads,saves,modifies data in specified file
"""


from flask import Flask, redirect, url_for, request
import csv


def ID_generator(stories):
    """
        Generates an ID for the entries.
        Loads the output of show_stories,
        checks the line number of it and adds 1 to it.
    """
    ID_numbers = [int(id[0]) for id in stories]
    if not ID_numbers:
        return str(1)
    return str(max(ID_numbers) + 1)


def open_file(story_ID, filename="database.csv"):
    """
        Opens the specified file to show its content.
        Reads it content as rows.
    """
    try:
        with open(filename, 'r') as workfile:
            row = workfile.readlines()
            stories = [item.split(';') for item in row]
            return stories
    except FileNotFoundError:
        stories = None


def write_to_file(stories, filename="databse.csv"):
    """
        Saves data to the specified file.
        Write the entry as rows.
    """
    with open(filename, 'w') as workfile:
        for item in stories:
            row = ';'.join(item)
            workfile.write(row + '\n')


def add_story(story_ID, filename="database.csv"):
    """
        Adds the entries what the user gives.
    """
    stories = open_file(story_ID)
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
        new_entries.append(request.form[name])
    stories.append(new_entries)
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






