import csv
# import sys
# import os


def write_csv(cleaned_data: list[dict], data_filename: str):
    keys = cleaned_data[0].keys()
    with open(data_filename, "w", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(cleaned_data)
    print(">>> O arquivo de dataset limpo foi escrito com sucesso!")
