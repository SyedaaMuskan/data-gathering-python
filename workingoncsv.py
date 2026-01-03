import requests
from io import StringIO
import pandas as pd
url="https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv?utm_source=chatgpt.com"
req=requests.get(url)
data=StringIO(req.text)
df=pd.read_csv(data).info()
print(df)