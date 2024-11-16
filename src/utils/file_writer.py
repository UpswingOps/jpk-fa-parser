"""
File writer utility functions
"""
import os
import pandas as pd

OUTPUT_CSV_DIR = "output_csv"
OUTPUT_JSON_DIR = "output_json"
OUTPUT_HTML_DIR = "output_html"


def save_to_csv(data):
    """
    Save data to CSV files
    :param data:
    :return:
    """
    check_if_path_exists_if_not_create(OUTPUT_CSV_DIR)
    for key, records in data.items():
        if records:
            df = pd.DataFrame(records)
            output_filename = f"{OUTPUT_CSV_DIR}/{key}.csv"
            df.to_csv(output_filename, index=False)
            records_count = len(records)
            print(f"Data saved to CSV files: {output_filename}. Records: {records_count}")


def save_to_json(data):
    """
    Save data to JSON files
    :param data:
    :return:
    """
    check_if_path_exists_if_not_create(OUTPUT_JSON_DIR)
    for key, records in data.items():
        if records:
            output_filename = f"{OUTPUT_JSON_DIR}/{key}.json"
            with open(output_filename, "w", encoding="utf-8") as f:
                records = str(records).replace("'", '"')
                f.write(records)
            records_count = len(records)
            print(f"Data saved to JSON files: {output_filename}. Records: {records_count}")


def save_to_html(data):
    """
    Save data to HTML files
    :param data:
    :return:
    """
    check_if_path_exists_if_not_create(OUTPUT_HTML_DIR)
    for key, records in data.items():
        if records:
            df = pd.DataFrame(records)
            output_filename = f"{OUTPUT_HTML_DIR}/{key}.html"
            html_table = df.to_html(index=False)
            html_content = generate_html_document(key, html_table)
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(html_content)

            records_count = len(records)
            print(f"Data saved to HTML files: {output_filename}. Records: {records_count}")


def generate_html_document(key: str, html_table: str):
    """
    Generate HTML document
    :param key:
    :param html_table:
    :return:
    """
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{key} Data</title>
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}
        th {{
            background-color: #f2f2f2;
            text-align: left;
        }}
    </style>
</head>
<body>
    <h1>{key.capitalize()} Data</h1>
    {html_table}
</body>
</html>"""
    return html_content


def check_if_path_exists_if_not_create(path: str):
    """
    Check if path exists, if not create it
    :param path:
    :return:
    """
    # print(path)
    # if not path.exists(path):
    #     path.mkdir(parents=True, exist_ok=True)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Path '{path}' created.")
