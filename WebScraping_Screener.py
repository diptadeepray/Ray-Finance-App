


#In P/E
'''Is the P/E more than average?
Are the other companies overvalues or undervalues compared to their own P/E
Id the median P/E of those companies more or less than P/E of TCS'''

#In all data_points parameters
# Average OPM,TAX Beter or worse than TCS?
# Revenue, Net Profit consistently increases for TCS and all other companies?
# If consistently increases,

#In all summary_points parameters, are they better or worse than TCS?

# Sales-Expenses ratio of all companies, better or worse than TCS?



def WebScrapingMethod(url="https://www.screener.in/company/TCS/consolidated/"):
    data_points = ["Sales", "Expenses", "OPM %", "Tax %", "Net Profit"]

    summary_points = ["Compounded Sales Growth", 'Compounded Profit Growth', 'Stock Price CAGR', 'Return on Equity']

    import requests  # To access a webpage
    from bs4 import BeautifulSoup

    # URL of the company page

    # Set headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

    # Send the request
    response = requests.get(url, headers=headers)
    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    all_sections = soup.find_all("section")
    for one_section in all_sections:

        if (one_section["id"] == "quarters"):
            print(one_section["id"])
            all_quater_names = []

            all_tr = one_section.find_all("tr")
            for one_tr in all_tr:

                # Print all data-points
                all_td = one_tr.find_all("td")  # Find all td in the row
                if all_td:
                    one_list = []
                    for one_td in all_td:
                        # print("inside td")
                        try:
                            one_list.append(
                                float(one_td.text.strip().replace(",", "").replace("  ", "").replace("\xa0", "")))
                        except Exception as e:
                            one_list.append(one_td.text.strip())
                            # print(type(one_td.text.strip()))
                            # print(repr(one_td.text.strip()))

                    a = one_list[0]
                    for one_data in data_points:
                        if a.startswith(one_data):
                            print(one_list)
                            break

                # To get the quater names
                all_th = one_tr.find_all("th")  # Find all td in the row
                if all_th:
                    for one_th in all_th:
                        # print(one_td.text.strip())
                        all_quater_names.append(one_th.text.strip())
                    print(all_quater_names)

                # Prints only if the list exists otherwise prints nothing

















        elif (one_section["id"] == "profit-loss"):
            print()
            print(one_section["id"])



















            '''
            Previously
            tr>>>>>
            th-Quater names
            td-Row name+DataPoints

            tbody>>>>

            tr>>>>
            1 th              Any of them?
            tr>>>
            td, td


            '''

            all_tables = one_section.find_all("table")

            for one_table in all_tables:



                first_th = one_table.find("th")


                if first_th:


                    for one_summary_point in summary_points:

                        if (one_summary_point == first_th.text.strip()):
                            print("a",first_th.text.strip())

                            all_tr = one_table.find_all("tr")

                            for one_tr in all_tr:
                                all_td=one_tr.find_all("td")
                                if all_td:
                                    a=[]
                                    i=0
                                    for one_td in all_td:
                                        if i==1:
                                            a.append(one_td.text.strip())
                                        i+=1
                                    print(a)



                                #print(one_td.text.strip())












            print()
            print("Next one dude!")

            all_quater_names = []

            all_tr = one_section.find_all("tr")
            for one_tr in all_tr:

                # Print all data-points
                all_td = one_tr.find_all("td")  # Find all td in the row
                if all_td:
                    one_list = []
                    for one_td in all_td:
                        # print("inside td")
                        try:
                            one_list.append(
                                float(one_td.text.strip().replace(",", "").replace("  ", "").replace("\xa0", "")))
                        except Exception as e:
                            one_list.append(one_td.text.strip())
                            # print(type(one_td.text.strip()))
                            # print(repr(one_td.text.strip()))

                    a = one_list[0]
                    for one_data in data_points:
                        if a.startswith(one_data):
                            print("td",one_list)
                            break

                # To get the quater names
                all_th = one_tr.find_all("th")  # Find all td in the row
                if all_th:
                    for one_th in all_th:
                        # print(one_td.text.strip())
                        all_quater_names.append(one_th.text.strip())
                    print("th",all_quater_names)


                # Prints only if the list exists otherwise prints nothing




WebScrapingMethod()