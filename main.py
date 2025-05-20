"""
main.py: první projekt do Engeto Online Python Akademie

author: Jan Bláha
email: jan.blaha@bcas.cz"
"""

import getpass

TEXTS = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.""",
]

USERS = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}


def analyze(text):
    """
    Prints basic statistics about text given as a parameter.

    Prints number of different word types and a word length histogram.
    """
    
    print(
        "There are {0} words in the selected text.".format(
            len(text.split())
        )
    )
    print(
        "There are {0} titlecase words.".format(
            len([t for t in text.split() if t.istitle()])
        )
    )
    print(
        "There are {0} uppercase words.".format(
            len([t for t in text.split() if t.isupper()])
        )
    )
    print(
        "There are {0} lowercase words.".format(
            len([t for t in text.split() if t.islower()])
        )
    )
    print(
        "There are {0} numeric strings.".format(
            len([t for t in text.split() if t.isnumeric()])
        )
    )
    print(
        "The sum of all the numbers is {0}.".format(
            sum([int(t) for t in text.split() if t.isnumeric()])
        )
    )

    print("-" * 45)
    print("LEN | " + "OCCURENCIES".center(30, " ") + " | NR.")
    print("-" * 45)
    for i in range(1, max([len(t) for t in text.split()]) + 1):
        print(
            str(i).rjust(3, " ")
            + " | "
            + ("*" * len([t for t in text.split() if len(t) == i]))
            .ljust(30, " ")
            + " | "
            + str(len([t for t in text.split() if len(t) == i]))
        )

username = input("Username: ")
password = getpass.getpass("Password: ")

if USERS[username] == password:
    print("----------------------------------------")
    print("Welcome to the app, " + username)
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
    index = input("Enter a number btw. 1 and 3 to select: ")
    print("----------------------------------------")

    if index.isnumeric():
        index = int(index) - 1
        if index < 0 or index > 2:
            print("Number must be between 1 and 3. Exiting.")
        else:
            analyze(TEXTS[index])
    else:
        print("Wrong input. Exiting.")
else:
    print("unregistered user, terminating the program...")