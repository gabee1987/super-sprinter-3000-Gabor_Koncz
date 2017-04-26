"""
    Data manager for Super Sprinter 3000
    load,save,modify data in specified file
"""


from flask import Flask
import csv


def ID_generator():
    """
        Generates an ID for the entries.
        Loads the output of show_stories, 
        checks the line number of it and adds 1 to it.
    """
    table = show_stories()
    return str(len(table) + 1)



def show_stories(filename="database.csv"):
    """
        Loads the data from a file. 
        Returns a list with the specific entries.
    """
    stories = list()
    try:
        with open(filename, 'r') as workfile:
            for row in workfile:
                row = row.strip(\n)
                stories.append(list(ID_generator()) + row.split(';'))
    except FileNotFoundError:
        stories = None
    return stories



def add_story(new_story, filename="database.csv"):
    """
        Adds the entries what the user gives.
        Append it to the list as a new line.
    """
    with open(filename, 'a') as workfile:
        workfile.write(';'.join(new_story) + '\n')




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


