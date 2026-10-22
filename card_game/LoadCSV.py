import csv, os
from typing import List

def create_csv_reader(config_path: str):
    try:
        return open(config_path, "r") 
    except IOError as exc:
        print("An error occurred.")
        print(exc)
        raise exc

def get_csv_rows(file_name: str) -> List[List[str]]:
    csv_data = []
    path = os.getcwd()
    path = path.replace("\\","/")
    try:
        reader = create_csv_reader(path + "/" + file_name)
        for row in reader:
            csv_data.append(row.split(","))
        reader.close()
    except Exception as e:
        print("An error occurred.")
        print(e)
    return csv_data