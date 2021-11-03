from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"input",
        "name":"people involved",
        "message":"New Expense - Invovled people: ",
    },
]

def is_user(user):
    with open('users.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            if row == user:
                return True

    return False

def awesome_prompt():
    infos = prompt(expense_questions)
    return infos

def new_expense(*args):
    infos = awesome_prompt()
    
    # L'optimisation s'est fait isekai par truck-kun :
    # https://ih1.redbubble.net/image.761262045.2536/flat,750x,075,f-pad,750x1000,f8f8f8.jpg
    while not(is_user(infos["spender"])):
        print("The spender does not exist. Try with an existing user.")
        infos = awesome_prompt()

    with open('expense_report.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        l = []
        for elem in infos:
            l.append(infos[elem])
        writer.writerow(some_input for some_input in l)

    print("Expense Added !")
    return True
