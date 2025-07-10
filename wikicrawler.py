import requests
from bs4 import BeautifulSoup
import os
from markdownify import markdownify as md

# Change these
USERNAME = "USUARIO UPC"
PASSWORD = "PASSWORD UPC"
BASE_URL = "https://mwiki.fib.upc.edu"  # Example: https://mywiki.org

# Start a session
session = requests.Session()

# Step 1: Load login page to get the token
login_page_url = f"{BASE_URL}/pti/index.php?title=Special:UserLogin&returnto=Categor%C3%ADa:proyectos"
response = session.get(login_page_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the wpLoginToken value
token_input = soup.find("input", {"name": "wpLoginToken"})
wp_login_token = token_input["value"] if token_input else ""

print("Found: wpLoginToken="+wp_login_token)

# Prepare payload
payload = {

    "wpName": USERNAME,
    "wpPassword": PASSWORD,
    "pluggableauthlogin": "Log in with PluggableAuth",
    "wpRemember": "1",  # if you want "keep me logged in"
    "wpLoginToken": wp_login_token,
    "wpEditToken": "+\\",  # appears as such in your code
    "title": "Special:UserLogin",
    "authAction": "login",
    "force": "",
    "domain": "PTI",
}

# Submit login form
post_url = f"{BASE_URL}/pti/index.php?title=Special:UserLogin&returnto=Categor%C3%ADa:proyectos"
print(post_url)

login_response = session.post(post_url, data=payload)
with open('out.html', 'w') as output:
    output.write(login_response.text)

# Check if login succeeded
if "Logout" in login_response.text or "Sign out" in login_response.text:
    print("✅ Logged in successfully!")
else:
    print("⚠️ Login might have failed.")

#FETCH PROJECTS LIST

# Example: now fetch a page
target_page = f"{BASE_URL}/pti/index.php?title=Special:UserLogin&returnto=Categor%C3%ADa:proyectos"
page_resp = session.get(target_page)

if page_resp.status_code == 200:
    print("✅ Successfully fetched target page.")
    # Example: print partial HTML or extract text
    soup = BeautifulSoup(page_resp.text, "html.parser")
    content_div = soup.find("div", {"class": "mw-parser-output"})  # main content
    if content_div:
        text_content = content_div.get_text()
        print(text_content[:1000])  # Print first 1000 chars
else:
    print("⚠️ Failed to fetch target page.")


'''html_projects_content = str(content_div)
for href in html_projects_content.find_all("href"):
    title = img.get("title")
    print(title)'''



for a in content_div.find_all("a"):
    href = a.get("href")
    title = a.text
    print(href)
    print(title)
    os.makedirs(title, exist_ok=True)
    os.makedirs(title+"/images", exist_ok=True)


    target_page = f"{BASE_URL}/pti/index.php?title=Special:UserLogin&returnto=Categor%C3%ADa:proyectos"



    resp = session.get(BASE_URL+href)
    psoup = BeautifulSoup(resp.text, "html.parser")
    content_div = psoup.find("div", {"class": "mw-parser-output"})
    if not content_div:
        continue

    # Extract text
    html_content = str(content_div)
    with open(title+'/index.html', 'w') as output:
        output.write(html_content)


    # Find and download images
    for img in content_div.find_all("img"):
        img_src = img.get("src")
        if not img_src:
            continue

        # Some wikis use relative image URLs
        img_url = BASE_URL+img_src
        img_filename = os.path.basename(img_src.split("?")[0])
        img_path = os.path.join(title+"/images", img_filename)

        # Download image
        img_resp = session.get(img_url)
        with open(img_path, "wb") as f:
            f.write(img_resp.content)

        # Replace in HTML with local markdown-style link
        markdown_img = f"![{img.get('alt', '')}](images/{img_filename})"
        print("markdown_img= "+markdown_img)
        img.replace_with(markdown_img)

    #to markdown
    html_content = str(content_div)
    markdown_content = md(html_content, heading_style="ATX")
    with open(title+'/README.md', 'w') as output:
        output.write(markdown_content)

    
    
#TO MARKD