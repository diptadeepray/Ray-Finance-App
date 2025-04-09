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
### Scope
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

