# Python    JSON (při převodu se přepisuje automaticky)
# True  ->  true
# False ->  false
# None  ->  null

# page.status_code -> 20X OK, 30X přesměrování, 40X chyby uživatele, 50X chyby serveru (400 a víc, vyhodí chybu)

import requests

with open('token.txt') as file_:
    token = file_.read().strip() # odstraní řádek navíc, přečte jen text tokenu

headers = {'Authorization': 'token ' + token} # jméno hlavičky : hodnota hlavičky

# page = requests.get('https://api.github.com/user', headers=headers)
page = requests.put('https://api.github.com/user/starred/milandufek/naucse-python', headers=headers)
page.raise_for_status()
print(page.text)
#data = page.json()
#print(data)
