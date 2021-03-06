"""
    Data manager for Super Sprinter 3000
    Loads and saves data in specified file.
    by Gábor Koncz
"""


from flask import Flask, redirect, url_for, request
import csv


def ID_generator(stories):
    """
        Generates an ID for the entries,
        based on the line numbers.
    """
    ID_numbers = [int(id[0]) for id in stories]
    if not ID_numbers:
        return str(1)
    return str(max(ID_numbers) + 1)


def open_file(filename="database.csv"):
    """
        Opens the specified file and
        reads its content as rows, return a list.
    """
    try:
        with open(filename, 'r') as workfile:
            row = workfile.readlines()
            stories = [item.replace("\n", "").split(';') for item in row]
            return stories
    except FileNotFoundError:
        stories = None


def write_to_file(stories, filename="database.csv"):
    """
        Saves data to the specified file.
        Write the entries as rows.
    """
    with open(filename, 'w') as workfile:
        for item in stories:
            story = [element.strip("\n") for element in item]
            row = ';'.join(story)
            workfile.write(row + "\n")










