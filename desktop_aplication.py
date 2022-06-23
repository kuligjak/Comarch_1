# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("db_test.xlsx")

df_global_bus = df.loc[df["Owner Org"] == "Global Business"]
df_detail = df.loc[df["Owner Org"] == "Detail"]

unique_owners = df["Owner Org"].unique()
unique_owners = unique_owners.tolist()

df_owners = {}

for owner in unique_owners:
    df_owner = owner.replace(" ", "_")
    print(f"Make new df for {owner} -> {df_owner}")
    df_owners[df_owner] = df.loc[df["Owner Org"] == owner]



print(df_owners["Global_Business"])




