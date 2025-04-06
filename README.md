# 📊 Ray Finance App

**Ray Finance App** is a Python-based financial analysis tool that scrapes and compares key financial metrics of top Indian companies in the **FMCG** and **IT** sectors using [Screener.in](https://www.screener.in). The data is presented through a sleek and interactive GUI built with **CustomTkinter**.

---

## 🔧 Features

- 📈 Extracts and compares:
  - Compounded Sales Growth
  - Compounded Profit Growth
  - Stock Price CAGR
  - Return on Equity (ROE)
- 🏢 Covers leading companies from:
  - **FMCG Sector**: HUL, ITC, Nestle, Dabur, Marico, etc.
  - **IT Sector**: TCS, Infosys, Wipro, HCL Tech, Tech Mahindra, etc.
- 🖥️ Interactive GUI built with **CustomTkinter**
- ⚙️ Uses `requests` and `BeautifulSoup` for efficient web scraping
- 📋 Easy-to-read summaries displayed in a popup window

---

## 🗂️ Project Structure

```text
Ray-Finance-App/
│
├── user_interface.py                # GUI file built with CustomTkinter
├── WebScraping_FMCG_Screener.py    # Scrapes data for FMCG companies
├── WebScraping_IT_Screener.py      # Scrapes data for IT companies
└── README.md                        # Project documentation

