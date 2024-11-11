import sys

import psycopg2

from src.models.db_tables import db_tables


def create_db_tables(db_config):
    """
    Create database tables
    :param db_config:
    :return:
    """
    create_table_sqls = []

    for key, record_tags in db_tables.items():

        db_columns = []
        for tag in record_tags:
            if tag.get("type") == "date":
                db_columns.append(f"{tag.get('name')} DATE")
            elif tag.get("type") == "float":
                db_columns.append(f"{tag.get('name')} FLOAT")
            elif tag.get("type") == "integer":
                db_columns.append(f"{tag.get('name')} INTEGER")
            elif tag.get("type") == "boolean":
                db_columns.append(f"{tag.get('name')} BOOLEAN")
            elif tag.get("type") == "string100":
                db_columns.append(f"{tag.get('name')} VARCHAR(100)")
            elif tag.get("type") == "string200":
                db_columns.append(f"{tag.get('name')} VARCHAR(200)")
            else:
                db_columns.append(f"{tag.get('name')} VARCHAR(50)")

        create_table_sql = f"CREATE TABLE IF NOT EXISTS {key} ({', '.join(db_columns)})"

        create_table_sqls.append(create_table_sql)

        try:
            conn = psycopg2.connect(**db_config)
            cursor = conn.cursor()

            for sql in create_table_sqls:
                cursor.execute(sql)

            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"!!! Error: {e}")
            sys.exit(1)

    print("Database tables (re)created")


def insert_to_postgresql(data, db_config):
    """
    Insert data to PostgreSQL database
    :param data:
    :param db_config:
    :return:
    """
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        for key, records in data.items():
            if records:
                for record in records:
                    columns = ', '.join(record.keys())
                    placeholders = ', '.join(['%s'] * len(record))
                    sql = f"INSERT INTO {key} ({columns}) VALUES ({placeholders})"
                    cursor.execute(sql, list(record.values()))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data saved to PostgreSQL database")
    except Exception as e:
        print(f"!!! Error: {e}")
        sys.exit(1)


def delete_from_postgresql(data, db_config):
    """
    Delete data from PostgreSQL database
    :param data:
    :param db_config:
    :return:
    """
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        for key, records in data.items():
            if records:
                for record in records:
                    # columns = ', '.join(record.keys())
                    # placeholders = ', '.join(['%s'] * len(record))
                    # sql = f"DELETE FROM {key} WHERE {columns} = {placeholders}"
                    sql = f"DELETE FROM {key}"
                    cursor.execute(sql, list(record.values()))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data deleted from PostgreSQL database")
    except Exception as e:
        print(f"!!! Error: {e}")
        sys.exit(1)


def save_to_postgresql(data, db_config):
    """
    Save data to PostgreSQL database
    :param data:
    :param db_config:
    :return:
    """
    create_db_tables(db_config)
    delete_from_postgresql(data, db_config)
    insert_to_postgresql(data, db_config)
    # drop table faktura;
