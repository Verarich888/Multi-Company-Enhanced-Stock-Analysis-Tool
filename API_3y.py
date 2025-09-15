from pathlib import Path
import time
import pandas as pd
import yfinance as yf

# ---------------------------
# CONFIG
# ---------------------------
CFG = {
    "tickers": ["AAPL", "MSFT", "TSLA"],  # symbols to fetch
    "years_to_fetch": 3,                  # fetch this many years
    "interval": "1d",                     # daily bars
    "adjust": True,                       # adjust for splits/dividends
    "result_file": "result.csv",          # combined output file
    "sleep_seconds": 0,                   # pause between ticker requests
}

# ---------------------------
# Data Collection
# ---------------------------
def fetch_and_save_all() -> Path:
    """Download data for all tickers, merge, and save to one CSV."""
    frames = []
    for t in CFG["tickers"]:
        try:
            df = yf.download(
                tickers=t,
                period=f"{CFG['years_to_fetch']}y",
                interval=CFG["interval"],
                auto_adjust=CFG["adjust"],
                progress=False,
                threads=True,
            )
            if df.empty:
                print(f"[WARN] {t}: no data returned.")
                continue
            df = df.reset_index()
            df["Ticker"] = t
            frames.append(df)
            print(f"[OK] {t}: {len(df)} rows")
            time.sleep(CFG["sleep_seconds"])
        except Exception as e:
            print(f"[ERROR] {t}: {e}")

    if frames:
        result = pd.concat(frames, ignore_index=True)
        out_path = Path(CFG["result_file"])
        result.to_csv(out_path, index=False)
        print(f"[DONE] Saved {len(result)} rows → {out_path}")
        return out_path
    else:
        print("[WARN] No data collected.")
        return None

# ---------------------------
# Run
# ---------------------------
if __name__ == "__main__":
    fetch_and_save_all()
