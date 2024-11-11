import pandas as pd
import os

OUTPUT_CSV_DIR = "output_csv"
OUTPUT_JSON_DIR = "output_json"


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
