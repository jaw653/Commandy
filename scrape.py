import requests
from bs4 import BeautifulSoup as bs
import re
import json

url = 'https://ss64.com/bash/'
page = requests.get(url)

soup = bs(page.content, 'html.parser')
results = soup.find(class_='az')

# print(results.prettify())
rows = results.find_all('tr')

clean = re.compile('<.*?>')

cmd_dict = {}
for row in rows:
    data = row.find_all('td')
    cmd = re.sub(clean, '', str(data[1]))
    description = re.sub(clean, '', str(data[2]))
    if len(cmd) == 1:
        if cmd == 'v' or cmd == 'w' or cmd == '.':
            cmd_dict[cmd] = description
    else:
        cmd_dict[cmd] = description

json_dict = json.dumps(cmd_dict, indent=2)
print(json_dict)
