import requests
from bs4 import BeautifulSoup

# Step 1: Create a session
session = requests.Session()

# Step 2: Log in
login_url = 'https://mwiki.fib.upc.edu/pti/index.php?title=Special:UserLogin&returnto=Categor%C3%ADa%3Aproyectos&returntoquery='
payload = {
    'username': 'ruben.tous',
    'wpPassword1': 'UPC$secret2025'
}
session.post(login_url, data=payload)

# Step 3: Access a page
page_url = 'https://mwiki.fib.upc.edu/pti/index.php/Categor%C3%ADa:proyectos'
response = session.get(page_url)
#print(response.text)

# Step 4: Parse content
soup = BeautifulSoup(response.text, 'html.parser')
content = soup.find('div', class_='body')  # Adjust selector to your wiki

print(content)

with open('out.html', 'w') as output:
    output.write(response.text)