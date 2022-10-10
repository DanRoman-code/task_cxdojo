import csv
import re
from bs4 import BeautifulSoup

CSV_PATH = r"C:\Users\coderc\Desktop\testProject\test_app\files\test_task.csv"
XML_PATH = r"C:\Users\coderc\Desktop\testProject\test_app\files\test_task.xml"


def working_with_files():
    users_csv_info = []
    users_xml_info = []

    with open(CSV_PATH, "r") as file:
        pattern = re.compile("^[a-zA-Zа-яА-Я.]+$")

        reader = csv.reader(file)
        for row in reader:
            if len(" ".join(row).split()) == 3 and bool(pattern.search(row[0])):
                users_csv_info.append(
                    {"username": row[0], "password": row[1], "date_joined": row[2]}
                )

    with open(XML_PATH, "r") as file:
        data = file.read()
        bs_data = BeautifulSoup(data, "xml")

        for user in bs_data.select("users user"):
            user = [user.first_name.text, user.last_name.text, user.avatar.text]
            if len(" ".join(user).split()) == 3 and bool(
                pattern.search(user[0]) and pattern.search(user[1])
            ):
                users_xml_info.append(
                    {"first_name": user[0], "last_name": user[1], "avatar": user[2]}
                )

    valid_users = []

    for user_csv in users_csv_info[1:]:
        for user_xml in users_xml_info:
            if user_xml["last_name"].lower() in user_csv["username"].lower():
                user_xml.update(user_csv)
                valid_users.append(user_xml)
                users_xml_info.remove(user_xml)

    return valid_users


if __name__ == "__main__":
    working_with_files()
