__author__ = 'Leo'
#-*-coding: utf-8-*-
import requests, re,csv
# a = open('url_responsesample1.txt', 'w', encoding='utf-8')
# regex = re.compile("[а-я]*(?=\",\"pos\":\"глагол\")")
# word = ''
# ya_token = 'dict.1.1.20160901T163720Z.c3986420442a734b.8cc59bf531e62d68cc41631bbc43ffac7c070440'
# ya_params ={'key': ya_token, 'lang':'en-ru', 'text': word }
# ya_link = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
word = "breathe"
# response = requests.get(ya_link, params = ya_params)
# response.json()
# print (response)
# response1 = requests.get("https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20160901T163720Z.c3986420442a734b.8cc59bf531e62d68cc41631bbc43ffac7c070440&lang=en-ru&text=breathe")
# response1.json()
# match = re.findall(regex,response1.text)
# a.write(str(match).replace('\'', ''))

#regex = re.compile("[^\"]*(?=\",\"pos\":\"глагол\")")
ms_token = 'Bearer'+'verbnet2016'+'http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fidentity%2fclaims%2fnameidentifier=verbnet2016&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1472897139&Issuer=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&HMACSHA256=qlid6j9Re08hPBAIYMWnFhyNo7NXaV34S3vN9DY6l2w%3d='
ms_link = "http://api.microsofttranslator.com/v2/Http.svc/GetTranslations"
j=1

ms_params = {'appId': 'verbnet2016', 'from':'en', 'to': 'ru','text': word, 'maxTranslations':'20'}

with open ('synsets_demo.txt', 'r', encoding='utf-8') as synsets, open ('translations_ms1.txt', 'w', encoding='utf-8', ) as translation:
    synsets = csv.reader(synsets, delimiter = ',')
    for row in synsets:
        for i in row:
            word = str(i).strip(" ")
            print(word)
            print(j)
            response = requests.post(ms_link, params = ms_params) #{'authToken': ms_token, 'from':'en', 'to': 'ru','text': word, 'maxTranslations':'20'})
            print(response)
            #response.json()
            #match = re.findall(regex,response.text)
            #translation.write(str(match).replace('\'', '')+ '\t')
            translation.write(response.text)
        translation.write('\n')
        j+=1

