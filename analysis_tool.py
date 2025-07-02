import datetime

from playwright.sync_api import sync_playwright
from datetime import date
import pandas as pd
import os
import plotly.express as px
import numpy as np
from io import StringIO
import time
import re
from pathlib import Path



from playwright.sync_api import Playwright, sync_playwright



def cleaning_searching_acount(df):
    df['搜尋量'] = df['搜尋量'].str.replace('万','0000')
    df['搜尋量'] = df['搜尋量'].str.replace(',','')
    df['搜尋量'] = df['搜尋量'].str.replace('+', '')
    return df






def cleaning_datetime(df):
    df['已開始'] = df['已開始'].str.replace(' [UTC+8]', ' ', regex=False)
    df['已開始'] = '熱搜開始時間	 ' + df['已開始']
    return df

def plotting_figure(df):
    # 確保搜尋量為數值型別
    df["搜尋量"] = pd.to_numeric(df["搜尋量"], errors="coerce")

    # 建立 log 搜尋量欄位（顏色依據）
    df["log_搜尋量"] = df["搜尋量"].apply(lambda x: np.log10(x + 1) if pd.notnull(x) else 0)

    # 建立 label 作為圖中顯示文字
    df["label"] = (
        df["Google 搜尋趨勢"] + "<br>" +
        df["已開始"].astype(str) + "<br>" +
        df["搜尋量"].astype(str)
    )

    # 圖表標題，使用第一筆更新時間
    update_time = df['更新时间'].iat[0] if '更新时间' in df.columns else "未知"
    title_text = f"24小時內Google關鍵字排名<br>更新時間：{update_time}"

    # 建立 Treemap 圖
    fig = px.treemap(
        df,
        path=["label"],
        values="搜尋量",
        color="log_搜尋量",
        color_continuous_scale=px.colors.sequential.Blues,
        title=title_text
    )

    # 美化圖表外觀（背景、邊距）
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(t=60, l=25, r=25, b=25)

    )

    # 將 Treemap 的根節點底色改為白色（不然會灰灰的）
    fig.update_traces(root_color="white")

    return fig

def download_google_trend_csv():
    print('打开爬虫工具.....')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        print('強制繁體中文介面.....')
        page.goto("https://trends.google.com/trending?geo=TW&hl=zh-TW")
        time.sleep(2)

        print('趨勢狀態=只顯示活躍的趨勢.....')
        page.get_by_role("button", name=re.compile("趨勢狀態")).click()
        time.sleep(1)
        page.get_by_role("switch", name="只顯示活躍的趨勢").click()
        time.sleep(1)

        print('排序條件=搜尋量.....')
        page.get_by_role("button", name=re.compile("排序條件")).click()
        time.sleep(1)
        page.get_by_role("menuitemradio", name="搜尋量").click()
        time.sleep(1)

        print('每頁列數=50.....')
        page.get_by_role("combobox", name="每頁列數").locator("div").click()
        time.sleep(1)
        page.get_by_role("option", name="50").click()
        time.sleep(1)


        print('匯出.....')
        page.get_by_role("button", name="匯出").click()
        time.sleep(1)

        # 等待下載行為並點選「下載 CSV」
        with page.expect_download() as download_info:
            page.get_by_role("menuitem", name="下載 CSV").click()

        download = download_info.value
        df = pd.read_csv(download.path(), encoding="utf-8")

        # ✅ 關閉瀏覽器
        context.close()
        browser.close()

        # ✅ 最重要：有 return
        return df
