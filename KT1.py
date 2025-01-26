"""
KT1
"""
connection = True
while connection:
    email = input("Введите адресс электронной почты: ")
    if "." in email and "@" in email:
        print("Ваш адрес электронной почты записан")
        break
    else:
        print("Адрес не действителен, повторите попытку")
