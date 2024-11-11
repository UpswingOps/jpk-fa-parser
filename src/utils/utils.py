"""
Utility functions.
"""
import xml.dom.minidom
import json


def load_text_file(file_path):
    """Load text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def save_text_file(file_path, data):
    """Save text file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)


def pretty_print_xml(xml_string):
    """Pretty print XML string."""
    dom = xml.dom.minidom.parseString(xml_string)
    xml_string = dom.toprettyxml(indent="  ", encoding="utf-8", newl="").decode("utf-8")
    # return xml_string.replace('\n\n', '\n')
    return xml_string


def pretty_print_json(data):
    """Pretty print JSON data."""
    return json.dumps(data, indent=4)
