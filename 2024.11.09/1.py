email = input()

if '@' in email and email.index('@') != 0:
    if '.' in email[email.index('@'):]:
        print("да")
    else:
        print("нет")
else:
    print("нет")

#sgd@ya.ru
#да

#abcde@fghij
#нет
