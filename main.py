"""
Main script to parse XML file and save to CSV/JSON or PostgreSQL
"""
import os
import sys

from dotenv import load_dotenv

from src.utils.db_writer import save_to_postgresql
from src.utils.file_writer import save_to_csv, save_to_json
from src.utils.utils import pretty_print_xml, load_text_file, save_text_file
from src.utils.xml_parser import parse_xml_to_dict


def main():
    """
    Main function
    :return:
    """
    if len(sys.argv) < 3:
        print("Usage: python script.py <xml_file> <db_or_csv_or_json>")
        sys.exit(1)

    load_dotenv()

    xml_file = sys.argv[1]
    action = sys.argv[2]

    try:
        data = parse_xml_to_dict(xml_file)

        if action == "csv":
            save_to_csv(data)
        elif action == "json":
            save_to_json(data)
        elif action == "pretty_xml":
            file_content = load_text_file(xml_file)
            # print(file_content)
            output_content = pretty_print_xml(file_content)
            # print(output_content)
            save_text_file("pretty.xml", output_content)

        elif action == "db":
            db_config = {
                "host": os.getenv("DB_HOST"),
                "database": os.getenv("DB_NAME"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD")
            }
            save_to_postgresql(data, db_config)
        else:
            print("Invalid action. Use 'csv' to save as CSV or 'db' to save to PostgreSQL.")
    except Exception as e:
        print(f"!!! Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
