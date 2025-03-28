# This is how the tags are arragnfes in the HTML file of Screener


#pip install beautifulsoup4 requests openpyxl


import requests #To access a webpage
from bs4 import BeautifulSoup
import openpyxl #Create a Excel file of the data

# URL of the company page
url = "https://www.screener.in/company/TCS/consolidated/"
# Set headers to mimic a real browser request
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

# Send the request
response = requests.get(url, headers=headers)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract company name from <h1> tag
#company_name = soup.find("h1", class_="h2 shrink-text").text.strip()

#print("Company Name:", company_name)



'''
<section id="quaters
{div
h2}
{div
thead(tr(th,th, th)),tbody(tr(td,td,td,...),tr(td,td,td,...),tr(td,td,td,...))}


<section id="profit-loss"
{div
h2
}
{div
thead(tr(th,th, th)),tbody(tr(td,td,td,...),tr(td,td,td,...),tr(td,td,td,...))}
'''




'''
title=soup.find_all("h2")
print(title)
#titles=soup.find("section",id="quaters").find_all("tr").find_all("th")
titles_list=[]
for t in titles:
        if t.text.strip() =="":
            pass
        else:
            titles_list.append(t.text.strip())
print("Quater Titles:", len(titles),len(titles_list),titles_list)
'''

i=0
sections=soup.find_all("section")
for s in sections:
    print("Section Starts",i)
    #all_tr=s.fi
    print(s.get("id"))
    if s.get("id")=="quarters":
        all_tr = s.find_all("tr")
        all_tr_list_quater=[]
        for one_tr in all_tr:
            if one_tr.find("th"):
                all_th = one_tr.find_all("th")
                all_th_list = []
                for single_td in all_th:
                    all_th_list.append(single_td.text.strip())
                all_tr_list_quater.append(all_th_list)
                #print(all_th_list)


            elif one_tr.find("td"):
                all_td = one_tr.find_all("td")
                all_td_list=[]
                for single_td in all_td:

                    try:
                        all_td_list.append(int(float(single_td.text.strip().replace(",", "").replace("%", ""))))
                    except Exception as e:
                        all_td_list.append(single_td.text.strip())
                all_tr_list_quater.append(all_td_list)
                #print(all_td_list)
        for one_tr in all_tr_list_quater:
            print(one_tr)



    elif s.get("id")=="profit-loss":
        all_tr = s.find_all("tr")
        all_tr_list_quater = []
        for one_tr in all_tr:
            if one_tr.find("th"):
                all_th = one_tr.find_all("th")
                all_th_list = []
                for single_td in all_th:
                    all_th_list.append(single_td.text.strip())
                all_tr_list_quater.append(all_th_list)
                # print(all_th_list)


            elif one_tr.find("td"):
                all_td = one_tr.find_all("td")
                all_td_list = []
                for single_td in all_td:

                    try:
                        all_td_list.append(int(float(single_td.text.strip().replace(",", "").replace("%", ""))))
                    except Exception as e:
                        all_td_list.append(single_td.text.strip())
                all_tr_list_quater.append(all_td_list)
                # print(all_td_list)
        for one_tr in all_tr_list_quater:
            print(one_tr)


    print("Section Ends",i)
    i+=1

'''

numbers=soup.find_all("tr")
numbers_final=[]
i=0
for n in numbers:
    print("New",i)
    i+=1
    print("Inside 1 tr")
    single_tr=n.find_all("td")
    single_tr_list=[]
    for b in single_tr:
        try:
            print("in",int(float(b.text.strip().replace(",","").replace("%",""))))
        except Exception as e:
            print("str",b.text.strip(),len(b.text.strip()))
    print(type(single_tr_list),single_tr_list)

        #print(type(b.text.strip())) # print gives /n at the end of the line
    print()
    
    #profit_loss = soup.find("section", id="profit-loss")
'''