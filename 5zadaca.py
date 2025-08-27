import re

email = input("Unesi email: ")
eduid = input("Unesi eduID: ")

regex_email = '^[a-z]+\\.[a-z]+@fpmoz\\.sum\\.ba$'
regex_eduid = '^i[a-z]+[0-9]*@sum\\.ba$'

if re.match(regex_email, email) and re.match(regex_eduid, eduid):
    print("Uspjesno!")
else:
    print("Neuspjesno.")







