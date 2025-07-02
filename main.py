import analysis_tool as AT
from datetime import datetime

# pd.set_option("display.max_columns", None)   # 不省略欄位
# pd.set_option("display.max_rows", None)      # 不省略列數
# pd.set_option("display.width", None)         # 自動調整寬度
# pd.set_option("display.max_colwidth", None)  # 展開欄位內容


df = AT.download_google_trend_csv()
df = AT.cleaning_searching_acount(df)
df = AT.cleaning_datetime(df)

now = datetime.now().replace(microsecond=0)
df['更新时间'] = f'{now}'


fig = AT.plotting_figure(df)
fig.update_layout(width=1280, height=720)
fig.show()
