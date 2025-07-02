# Google Trend Treemap

一鍵產生 Google 熱門搜尋趨勢的 Treemap 圖表，可部署成網頁 API，自動取得最新資料並動態視覺化。

## 🔍 專案特色

- 自動抓取 [Google Trends 熱門搜尋](https://trends.google.com/trending?geo=TW&hl=zh-TW)
- 支援繁體中文介面
- 顯示搜尋量的 Treemap 視覺化圖表
- 自動部署於 Render，支援免費即時運行

## 🧰 使用技術

- Python + Flask
- Playwright（模擬瀏覽器抓取）
- Pandas + Plotly（資料處理與視覺化）

## 🚀 快速部署（Render）

1. 點選 Fork 本專案
2. 登入 [Render](https://render.com)
3. 新建 Web Service，連結此 GitHub repo
4. 設定：
   - Start Command：`playwright install && python api.py`
   - Build Command：空白即可
   - Free Plan 選擇 `Singapore`
5. 點擊「Deploy」

## 📂 專案結構

├── api.py # Flask 主入口
├── analysis_tool.py # 資料處理與繪圖模組
├── requirements.txt # 所需套件
├── render.yaml # Render 自動部署設定
└── README.md # 本說明文件

less
复制
编辑

## 📬 作者

Annxu｜GitHub: [@f50523a](https://github.com/f50523a)