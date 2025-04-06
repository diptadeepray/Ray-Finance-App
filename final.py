all_links={"TCS": [
    "https://www.screener.in/company/TCS/consolidated/",
    "https://www.screener.in/company/INFY/consolidated/",
    "https://www.screener.in/company/WIPRO/consolidated/",
    "https://www.screener.in/company/HCLTECH/consolidated/",
    "https://www.screener.in/company/TECHM/consolidated/",
    "https://www.screener.in/company/LTIM/consolidated/",
]}
#Compare all the parameters to tcs[0=


data_points=["Sales","Expenses","OPM %","Tax %","Net Profit"]

summary_points=["Compounded Sales Growth",'Compounded Profit Growth','Stock Price CAGR','Return on Equity']


import WebScraping_Screener

WebScraping_Screener.WebScrapingMethod("https://www.screener.in/company/TCS/consolidated/")
#WebScraping_Screener.WebScrapingMethod("https://www.screener.in/company/INFY/consolidated/")
