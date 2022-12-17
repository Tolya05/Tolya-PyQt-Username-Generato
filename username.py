from itertools import combinations
from random import choice
import secrets
from string import ascii_letters, digits, punctuation
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout

def usernameGenerator(words, username_layout: QVBoxLayout, password_layout: QHBoxLayout):
    names = list(words)
    usernames_tuples = []
    for i in range(len(names) + 1):
        usernames_tuples += (combinations(names, i))

    usernames_all = [''.join(tups) for tups in usernames_tuples]
    usernames = [choice(usernames_all) for _ in range(10)]
    for username in usernames:
        username_label = QLabel(username)
        username_layout.addWidget(username_label)

    password = password_generator()
    password_label = QLabel(password)
    password_layout.addWidget(password_label)

def password_generator():
    alphabet = ascii_letters + digits + punctuation
    pwd_len = 10
    pwd = ''.join(secrets.choice(alphabet) for _ in range(pwd_len))
    return pwd

def clearLayout(layout):
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
