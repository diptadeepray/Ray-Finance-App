allOtherFMCGCompanyinks=[
    "https://www.screener.in/company/MARICO/consolidated/",
    "http://screener.in/company/NESTLEIND/",
    "https://www.screener.in/company/BRITANNIA/consolidated/",
    "https://www.screener.in/company/GODREJCP/consolidated/",
    "https://www.screener.in/company/PATANJALI/",
    "https://www.screener.in/company/DABUR/consolidated/",
    "https://www.screener.in/company/AWL/",
    "https://www.screener.in/company/EMAMILTD/consolidated/",
    "https://www.screener.in/company/COLPAL/",
    "https://www.screener.in/company/ITC/consolidated/",
    "https://www.screener.in/company/RELIANCE/consolidated/"
]

summary_points={"Compounded Sales Growth":[[]],'Compounded Profit Growth':[[]],'Stock Price CAGR':[[]],'Return on Equity':[[]]}


Compounded_Sales_Growth=[]
Compounded_Profit_Growth=[]
Stock_Price_CAGR=[]
Return_On_Equity=[]



import requests  # To access a webpage
from bs4 import BeautifulSoup

# Set headers to mimic a real browser request
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

def WebScrapingHUL():
    # Send the request
    response = requests.get("https://www.screener.in/company/HINDUNILVR/consolidated/", headers=headers)
    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    all_sections = soup.find_all("section")
    for one_section in all_sections:
        if (one_section["id"] == "profit-loss"):
            print()
            #print(one_section["id"])

            all_tables = one_section.find_all("table")

            for one_table in all_tables:
                #print("Table begins")

                first_th = one_table.find("th")

                if first_th:
                    # Because there is 1 table in the website wgich has nothing
                    # This line is implemented so that that empty table can be avoided




                    for one_summary_point in summary_points:

                        if (one_summary_point == first_th.text.strip()):
                            #print( first_th.text.strip())

                            all_tr = one_table.find_all("tr")

                            b = []
                            for one_tr in all_tr:
                                all_td = one_tr.find_all("td")

                                a = []
                                if all_td:

                                    i = 0
                                    for one_td in all_td:
                                        a.append(one_td.text.strip())
                                    #print(a) #One list is createsd

                                    b.append(a)
                            summary_points[one_summary_point]=b




def WebScrapingOtherFMCGCompanies(url):
    # Send the request
    response = requests.get(url, headers=headers)
    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    all_sections = soup.find_all("section")
    for one_section in all_sections:
        if (one_section["id"] == "profit-loss"):
            print()
            print("Getting the data of ",soup.find("h1").text.strip())

            all_tables = one_section.find_all("table")

            for one_table in all_tables:
                #print("Table begins")

                first_th = one_table.find("th")

                if first_th:
                    # Because there is 1 table in the website wgich has nothing
                    # This line is implemented so that that empty table can be avoided



                    for one_summary_point in summary_points:

                        if (one_summary_point == first_th.text.strip()):
                            #print( first_th.text.strip())

                            all_tr = one_table.find_all("tr")

                            b = []
                            for one_tr in all_tr:
                                all_td = one_tr.find_all("td")

                                a = ""
                                if all_td:

                                    i = 0
                                    for one_td in all_td:
                                        if i==1:
                                            a=one_td.text.strip()
                                        i+=1
                                    #print(a) #One list is created

                                    b.append(a)


                            # Here to be done
                            for i in range(len(summary_points[one_summary_point])):
                                summary_points[one_summary_point][i].append(b[i])
                            #summary_points[one_summary_point]=b



def WebScraping_IT_Screener_Method():
    WebScrapingHUL()

    for oneFMCGComapnyLink in allOtherFMCGCompanyinks:
        WebScrapingOtherFMCGCompanies(oneFMCGComapnyLink)

    return summary_points






