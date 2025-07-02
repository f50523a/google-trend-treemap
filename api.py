from flask import Flask, render_template_string
import analysis_tool as AT
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    df = AT.download_google_trend_csv()
    df = AT.cleaing_searching_acount(df)
    df = AT.cleaning_datetime(df)
    df['更新时间'] = datetime.now().replace(microsecond=0)

    fig = AT.plotting_figure(df)
    fig.update_layout(width=1280, height=720)
    html_graph = fig.to_html(full_html=False)

    html = f"""
    <html>
    <head><title>Google 熱門趨勢</title></head>
    <body>
        <h1>即時關鍵字 Treemap</h1>
        <form method="get">
            <button type="submit">立即更新</button>
        </form>
        {html_graph}
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
