import requests
import pandas as pd
url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
data=response.json()
df=pd.json_normalize(data)
df=df[["id",
      "name","username","email","phone"]]
df=df.rename(columns={"id":"userid"})
#df["phone"]=df["phone"].astype(int)
print(df.head())
df.to_csv("clean_user.csv",index=False)