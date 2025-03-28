#pip install beautifulsoup4 requests openpyxl


import requests #To access a webpage
from bs4 import BeautifulSoup
import openpyxl #Create a Excel file of the data

# URL of the company page
url = "https://www.screener.in/company/TCS/consolidated/"
# Set headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Send the request
response = requests.get(url, headers=headers)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract company name from <h1> tag
#company_name = soup.find("h1", class_="h2 shrink-text").text.strip()

#print("Company Name:", company_name)


''' 
quater_names=soup.find_all("th")
quater_names_final=[]
for name in quater_names:
        quater_names_final.append(name.text.strip())
print("Company Name:", len(quater_names),quater_names_final)
'''

revenue = soup.find_all("tr")
revenue_final=[]
revenue_final2=[]
print(type(revenue))

aa=[]
bb=[]

for rev in revenue:
    revenue_final.append(rev.text.strip())
    revenue_final2.append(rev.get_text(strip=True))
print("Company Revenue:", len(revenue),len(revenue_final),revenue_final)
print("Company :",len(revenue_final2),revenue_final2)

aaa=[]

for rev in revenue:

    aa.append(rev.find("td", class_="text"))
    aaa.append(rev.find_all("td", class_="text"))
    bb.append(rev.find("td", class_="text" or ""))
print("aaa",aaa)

print("a",aa)


print("b",bb)



