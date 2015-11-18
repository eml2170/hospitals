import pandas as pd
import numpy as np

df = pd.DataFrame.from_csv("Timely and Effective Care - Hospital.csv")
new_columns = list(df.columns)
for i in xrange(15):
	new_columns[i] = new_columns[i].lower()
	new_columns[i] = new_columns[i].replace(" ", "_")

df.columns = new_columns
left = df.query('measure_name == "Left before being seen"')
hospitals_per_state = df.groupby('state').hospital_name.nunique()
data = left[['address','city','state','score']]
data["location"] = data["address"] + ", " + data["city"] + ", " + data["state"]
data = data[["location","score"]]
data = data[data["score"] != "Not Available"]
#data.to_csv("left_pct.csv", index=False)