# projekt_1.py: první projekt do Engeto Online Python Akademie

# author: Katerina Bartuskova
# email: kati.bartuskova@gmail.com
# discord: bartuskovak

import re

users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
username = input("username:")
password = input("password:")
print("-"*40)
if username in users and users[username]==password:
    print("Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print("-"*40)
else:
    print("unregistred user, terminating the program..")
    exit()
TEXTS = {
    1:"""Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""",
2:"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
3:"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""" 
}
text_index = int(input("Enter a number btw. 1 and 3 to select: "))
print("-"*40)
if not text_index in TEXTS.keys():
    print("invalid data")
    exit
text_wo_commas=TEXTS[text_index].replace(",","")
words=re.split("\s+",text_wo_commas)
print("There are", len(words), "words in the selected text.")
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
sum = 0
for word in words:
    if word.istitle():
        titlecase+=1
    elif word.isupper():
        uppercase+=1
    elif word.islower():
        lowercase+=1
    elif word.isnumeric():
        numeric+=1
        sum += int(word)
print("There are", titlecase, "titlecase words.")
print("There are", uppercase, "uppercase words.")
print("There are", lowercase, "lowercase words.")
print("There are", numeric, "numeric strings.")
print("The sum of all the numbers",sum)
print("-"*40)
letter_counter=dict()
for word in words:
    n=len(word)
    if n in letter_counter:
        letter_counter[n]+=1
    else:
        letter_counter[n]=1
sorted_lc = dict(sorted(letter_counter.items()))
print("LEN|  OCCURENCES  |NR.")
print("-"*40)
for key in sorted_lc:
    bar = "*"*sorted_lc[key]
    print(f"{key:>3}|{bar:<14}|{sorted_lc[key]}")
