# app.py
from pathlib import Path
import time
import pandas as pd
import yfinance as yf
from flask import Flask, render_template_string, request
from pandas.tseries.offsets import DateOffset

# ---------------------------
# CONFIG
# ---------------------------
CFG = {
    "tickers": ["AAPL", "MSFT", "TSLA"],  # symbols to fetch
    "years_to_fetch": 3,                  # fetch this many years
    "interval": "1d",                     # daily bars
    "adjust": True,                       # adjust for splits/dividends
    "data_dir": "data/raw",               # where CSVs are saved
    "sleep_seconds": 0,                   # pause between ticker requests
}

# ---------------------------
# Data Collection
# ---------------------------
def fetch_and_save(ticker: str) -> Path:
    """Download with yfinance and save CSV with a real Date column."""
    out_dir = Path(CFG["data_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{ticker}.csv"

    df = yf.download(
        tickers=ticker,
        period=f"{CFG['years_to_fetch']}y",
        interval=CFG["interval"],
        auto_adjust=CFG["adjust"],
        progress=False,
        threads=True,
    )

    if df.empty:
        print(f"[WARN] {ticker}: no data returned.")
        return out_path

    # Ensure Date is a proper column (not just index)
    df = df.reset_index()
    df.to_csv(out_path, index=False)
    print(f"[OK] {ticker}: {len(df)} rows → {out_path}")
    return out_path

def collect_data():
    for t in CFG["tickers"]:
        try:
            fetch_and_save(t)
            time.sleep(CFG["sleep_seconds"])
        except Exception as e:
            print(f"[ERROR] {t}: {e}")

# ---------------------------
# Web App (Flask)
# ---------------------------
app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Stock Data (last {{ years }} years)</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    h1 { color: #2c3e50; }
    table { border-collapse: collapse; width: 100%; margin: 1rem 0 2rem; }
    th, td { border: 1px solid #ddd; padding: 6px; text-align: center; }
    th { background-color: #2c3e50; color: white; }
    .note { color:#555; margin-bottom:1rem }
  </style>
</head>
<body>
  <h1>Stock Market Data (last {{ years }} years)</h1>
  <div class="note">
    Showing all rows from last {{ years }} years.<br>
    Files saved under <code>{{ data_dir }}</code>.
  </div>
  {% for ticker, data in tables.items() %}
    <h2>{{ ticker }}</h2>
    {{ data | safe }}
  {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    years = int(request.args.get("years", CFG["years_to_fetch"]))
    start = pd.Timestamp.today().normalize() - DateOffset(years=years)

    tables = {}
    for t in CFG["tickers"]:
        path = Path(CFG["data_dir"]) / f"{t}.csv"
        if path.exists():
            df = pd.read_csv(path, parse_dates=["Date"])
            df = df[df["Date"] >= start].sort_values("Date")  # keep ALL rows
            tables[t] = df.to_html(classes="table", index=False)
        else:
            tables[t] = "<p>No data available</p>"

    return render_template_string(
        HTML_TEMPLATE, tables=tables, years=years, data_dir=CFG["data_dir"]
    )

# ---------------------------
# Run
# ---------------------------
if __name__ == "__main__":
    collect_data()                 # fetch & save 3y CSVs
    app.run(debug=True, port=5000) # open http://127.0.0.1:5000
