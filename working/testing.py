import pandas as pd

df = pd.read_csv("./test-web-fill-form.csv")

for i in range(0, len(df)):
    print("Name:", df.iloc[i, 0])
    print("Status:", df.iloc[i, 1])