Google Trend Treemap
Generate a Treemap chart of Google trending searches with one click. This project runs as a web API that fetches real-time data and visualizes it dynamically.

🔍 Features
Automatically scrapes Google Trends (Traditional Chinese interface)

Treemap visualization showing search volume

Deployable as a public web API for real-time usage

🧰 Tech Stack
Python + Flask

Playwright (for browser automation)

Pandas + Plotly (data processing & visualization)

🚀 Quick Deployment (Fly.io)
Fork this repository

Install Fly CLI

Log in via CLI: fly auth login

Launch app: fly launch (follow prompts)

Edit fly.toml to adjust region and port (usually 8080)

Deploy: fly deploy

Visit your Fly.io app URL to view the live Treemap

📂 Project Structure
graphql
复制
编辑
├── api.py             # Flask API entry point  
├── analysis_tool.py   # Data processing & plotting module  
├── requirements.txt   # Python dependencies  
├── fly.toml           # Fly.io deployment configuration  
└── README.md          # Project description  
