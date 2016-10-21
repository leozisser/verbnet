__author__ = 'Leo'
from bs4 import BeautifulSoup
import requests, csv, time

k = open('deleteafterreading.txt','w+', encoding='utf-8')

def token():
    token_response = requests.post('https://datamarket.accesscontrol.windows.net/v2/OAuth2-13', {'client_id':'verbnet2016',
                                                                                    'client_secret': 'Tm0V3GhIwA6CG6B0EzOfUMhfO8AZDy8Op+CDTanywjg=',
                                                                                    'scope':'http://api.microsofttranslator.com',
                                                                                    'grant_type': 'client_credentials'})
    token_json = token_response.json()
    token = token_json["access_token"]
    print (token)
    authorization_value = "Bearer " + token
    return authorization_value

authorization_value = token()

ms_link = "http://api.microsofttranslator.com/v2/Http.svc/Translate"
ms1_link = "http://api.microsofttranslator.com/V2/Http.svc/GetTranslations"

j = 1

with open ('synsets.txt', 'r', encoding='utf-8') as synsets, open ('translations_ms1.txt', 'w', encoding='utf-8', ) as translation:
    synsets = csv.reader(synsets, delimiter = ',')
    for row in synsets:
        for i in row:
            word = str(i).strip(" ")
            print(word)
            ms_params = {'appId': authorization_value, 'from': 'en', 'to': 'ru','text': word, 'maxTranslations':'20'}
            response = requests.post(ms1_link, params=ms_params)
            #print(soup.string.contents)
            translate = response.text
            # print(translate)
            soup = BeautifulSoup(translate, "html.parser").text
            # print(soup)
            translation.write(soup + ',')
        j += 1
        print(j)
        translation.write('\n')

