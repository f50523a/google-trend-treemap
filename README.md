📈 Google Trends Taiwan Treemap
Generate a real-time Treemap chart of Google trending searches in Taiwan with just one click.
This project launches a browser in the background to fetch the latest data and displays a dynamic chart directly.

🔍 Features
Auto-scrapes Google Trends (Traditional Chinese) using Playwright

Filters to show only active trending topics

Sorts by search volume, displays top 50

Real-time Treemap visualization using Plotly

Deployable as a public interactive web interface

🧰 Tech Stack
Python + Playwright (headless browser scraping)

Pandas (data processing)

Plotly (Treemap visualization)

📸 Demo

↑ Generated Treemap chart

💡 How It Works
Launches a headless Chromium browser

Forces Traditional Chinese UI on Google Trends

Enables "Only show active trends"

Sorts by search volume, 50 results per page

Clicks Export → Download CSV

Parses and cleans the data

Visualizes using Plotly Treemap

🚀 Quick Run (for local test)
bash
复制
编辑
pip install -r requirements.txt
python main.py
The chart will auto-display after scraping completes (~10s).

📂 Project Structure
bash
复制
编辑
.
├── analysis_tool.py     # Web scraper + cleaner + visualizer
├── main.py              # Entry point: one-click run
├── requirements.txt     # Python dependencies
├── 作图.jpg               # Sample output
├── 过程.jpg               # Screenshot of scraping flow
└── README.md
✅ Use Case
This project is designed to be shared as a live demo or interview portfolio to showcase:

Python automation

Real-time data processing

Clean and interactive visualization
