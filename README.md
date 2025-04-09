# 📊 Ray Finance: Sectoral Stock Analysis Dashboard

## 🔖 Table of Contents
- [📌 Introduction](#-introduction)
- [✨ Features](#️-features)
- [📁 Project Structure](#-project-structure)
- [🏗️ Architecture](#️-architecture)
- [🧾 Code Overview](#-code-overview)
- [🚀 How to Use](#-how-to-use)
- [🛠️ Requirements](#-requirements)
- [📌 Notes](#-notes)

## 📌 Introduction
### Overview
**Ray Finance** is a desktop application designed to fetch and display financial metrics of top companies in different sectors using real-time data scraping from <code>screener.in</code>. The app offers a tabbed interface and a user-friendly GUI powered by CustomTkinter.
###Scope
This document covers the featured, project structure, architecture, code overview, how to use, requirements and guidelines for this Ray Finance project.


<h2>✨ Features</h2>
<ul>
  <li><strong>🔐 Login Authentication:</strong> Simple login screen to restrict access.</li>
  <li><strong>📁 Sector-Based Analysis:</strong> Choose between IT Outsourcing and FMCG sectors for comparison.</li>
  <li><strong>📊 Real-Time Data:</strong> Uses web scraping to pull updated metrics from screener.in.</li>
  <li><strong>📈 Key Financial Metrics:</strong> Includes Sales Growth, Profit Growth, ROE, and Stock Price CAGR.</li>
  <li><strong>🖥️ Responsive GUI:</strong> Scrollable, styled tables for better readability.</li>
  <li><strong>🧭 Tabbed Navigation:</strong> Additional tabs for Gold Market and Debt Investing.</li>
</ul>


## 📁 Project Structure
### Directory Layout
```plaintext
MyAwesomeApp/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/myawesomeapp/
│   │   │   │   ├── activities/
│   │   │   │   ├── adapters/
│   │   │   │   ├── models/
│   │   │   │   ├── repositories/
│   │   │   │   ├── viewmodels/
│   │   │   │   └── utils/
│   │   │   ├── res/
│   │   │   └── AndroidManifest.xml
│   └── build.gradle
├── build.gradle
└── settings.gradle
```

### Key Components
- activities: Contains Activity classes responsible for UI screens.
- adapters: Includes adapters for RecyclerView and other UI components.
- models: Defines data models used in the app.
- repositories: Handles data operations and business logic.
- viewmodels: Manages UI-related data in a lifecycle-conscious way.
- utils: Contains utility classes and helper functions.

## ⚙️ Setup Instructions
<h2>🔧 Setup Instructions</h2>

<h3>1. Clone the Repository</h3>
<pre><code>git clone https://github.com/diptadeepray/Ray-Finance-App.git
cd Ray-Finance-App
</code></pre>

<h3>2. Create a Virtual Environment</h3>
<p>It's recommended to use a virtual environment to manage dependencies.</p>

<pre><code># For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
</code></pre>

<h3>3. Install the Requirements</h3>
<p>All the installed Python packages, in the virtual environment, along with their versions is listed in the requirements.txt. All the python packages can installed, in any virtual environment later, using the following command in the terminal:
<code>requirements.txt</code>:</p>

<pre><code>pip install -r requirements.txt
</code></pre>

<hr>

<h2>📝 Notes</h2>

<ul>
  <li>To exit the virtual environment, run:
    <pre><code>deactivate</code></pre>
  </li>
  <li>If you add new packages, don’t forget to update <code>requirements.txt</code>:
    <pre><code>pip freeze > requirements.txt</code></pre>
  </li>
</ul>



<h1>📊 Ray Finance: Sectoral Stock Analysis Dashboard</h1>

<h2>✨ Features</h2>
<ul>
  <li><strong>Login Interface:</strong> Authenticated access with a simple GUI built using CustomTkinter.</li>
  <li><strong>Dropdown-Based Sector Selection:</strong> Choose between IT Outsourcing and FMCG sectors for analysis.</li>
  <li><strong>Live Web Scraping:</strong> Extracts and processes financial data from <code>screener.in</code>.</li>
  <li><strong>Dynamic UI:</strong> Scrollable and responsive tables for multiple companies and financial metrics.</li>
  <li><strong>Tabbed Layout:</strong> Share Market, Gold Market, and Debt Investing tabs with dynamic content loading.</li>
</ul>


<h2>📁 Project Structure</h2>
<pre>
📦 RayFinance
├── 🧠 user_interface.py             # Main GUI file with login, tabs, and dynamic analysis rendering
├── 🔍 WebScraping_IT_Screener.py   # Scraper for TCS and IT sector competitors
├── 🔍 WebScraping_FMCG_Screener.py # Scraper for HUL and other FMCG companies
</pre>

<h2>🧱 Architecture</h2>
<ul>
  <li><strong>Frontend GUI:</strong> Built with <code>customtkinter</code> for an enhanced look and feel of the desktop app.</li>
  <li><strong>Web Scraping Modules:</strong> 
    <ul>
      <li><code>WebScraping_IT_Screener.py</code> - Scrapes TCS and other major IT companies.</li>
      <li><code>WebScraping_FMCG_Screener.py</code> - Scrapes HUL and other major FMCG companies.</li>
    </ul>
  </li>
  <li><strong>Backend Logic:</strong> The scraping results are returned as structured tables and injected into the UI dynamically on selection.</li>
</ul>



<h2>🧾 Code Overview</h2>

<h3><code>user_interface.py</code></h3>
<ul>
  <li>Initializes the app window and handles login authentication.</li>
  <li>On successful login, shows tabs and dropdown to select sectors.</li>
  <li>Dynamically imports and runs the appropriate web scraping module based on selection.</li>
  <li>Displays the results in styled, scrollable tables inside the Share Market tab.</li>
</ul>

<h3><code>WebScraping_IT_Screener.py</code></h3>
<ul>
  <li>Scrapes data from TCS, Infosys, Wipro, HCL Tech, Tech Mahindra, and LTIMindtree.</li>
  <li>Extracts and aligns metrics like:
    <ul>
      <li>Compounded Sales Growth</li>
      <li>Compounded Profit Growth</li>
      <li>Stock Price CAGR</li>
      <li>Return on Equity</li>
    </ul>
  </li>
</ul>

<h3><code>WebScraping_FMCG_Screener.py</code></h3>
<ul>
  <li>Scrapes financial metrics from companies like HUL, Nestle, Britannia, Dabur, ITC, and more.</li>
  <li>Follows the same extraction logic as the IT screener for consistency.</li>
</ul>



<h2>🚀 How to Use</h2>
<ol>
  <li>Ensure you have Python 3 installed and run the following to install dependencies:</li>
</ol>
<pre><code>pip install requests beautifulsoup4 customtkinter</code></pre>

<ol start="2">
  <li>Run the application:</li>
</ol>
<pre><code>python user_interface.py</code></pre>

<ol start="3">
  <li>Login using:
    <ul>
      <li><strong>Username:</strong> admin</li>
      <li><strong>Password:</strong> 1234</li>
    </ul>
  </li>
  <li>Select a sector from the dropdown and click "Run Analysis".</li>
  <li>Wait a few moments while real-time data is fetched and displayed.</li>
</ol>



<h2>🛠️ Requirements</h2>
<ul>
  <li>Python 3.8 or above</li>
  <li><code>requests</code></li>
  <li><code>beautifulsoup4</code></li>
  <li><code>customtkinter</code></li>
</ul>

<h2>📌 Notes</h2>
<ul>
  <li>The scraping is done directly from public sources without any API dependency.</li>
  <li>Ensure a stable internet connection while scraping data.</li>
</ul>



