import requests
import pandas as pd
from datetime import datetime

# ==============================================================================

token = 738561
timeframe = "minute"
sdt = datetime(2015,2,2)
edt = datetime(2015, 4,2)
enctoken = ""

# ==============================================================================

header = {
    "Authorization" : f"enctoken {enctoken}"
}
url = f"https://kite.zerodha.com/oms/instruments/historical/{token}/{timeframe}"
param = {
    "oi" : 1,
    "from" :  sdt,
    "to" : edt
}

session = requests.session()
data = session.get(url, params=param, headers=header).json()["data"]["candles"]

df = pd.DataFrame(data)
print(df)
