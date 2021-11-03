from os import name
from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"user_name",
        "message":"New User",
    }
]

def add_user(*args):
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)

    with open('users.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for elem in infos:
            writer.writerow([infos[elem]])

    print("User Created !")
    return