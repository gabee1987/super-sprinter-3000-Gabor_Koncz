"""
    Data manager for Super Sprinter 3000
    load,save,modify data in specified file
"""


from flask import Flask
import csv


def show_stories(filename="database.csv"):
    """
        Loads the data from a file. 
        Returns a list with the specific entries.
    """
    stories = list()
    id = 1
    try:
        with open(filename, 'r') as workfile:
            for row in workfile:
                row = row.strip(\n)
                stories.append(list(str(id)) + row.split(';'))
                id += 1
    except FileNotFoundError:
        stories = None
    return stories



def add_story(filename="database.csv"):
    """
        Adds the entries what the user gives.
        Append it to the list as a new line.
    """


def delete_story(story_ID, filename="database.csv"):
    """
        Removes an entry from the specified file.
        Removes a line from the list.
    """



def update_story(story_ID, filename="database.csv"):
    """
        Update the entry specified by the story_ID.
        Replace the specified line in the list.
    """


