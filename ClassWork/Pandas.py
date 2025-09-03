# Pandas.py

import pandas as pd

'''
# series

prices = [199,5999,199,299,545]
products = ['phone','watch','cellphone','buds','shoes']

product_prices = pd.Series(prices,index=products)
print(product_prices)

print(f'\n---Head of the products: \n{product_prices.head(2)}')

print(f"\n---Tail of the products: \n{product_prices.tail(3)}")

print(f'\n---Sum:  {sum(product_prices)}')

print(f"\n---MinValue:  {min(product_prices)}")

print(f"\n---MaxValue:  {max(product_prices)}")

print(f"\n---Mean:  {product_prices.mean()}")

print("\nApply: ", product_prices.apply(lambda i: f'₹{i - i*0.05}'))

print("\nMap: ", product_prices.map(lambda i: f'₹{i}.00' ))

print("\nSorted by Values: \n",product_prices.sort_values())

print("\nSorted by index: \n",product_prices.sort_index())

print("\nSorted descending order:\n",product_prices.sort_index(ascending=False))

print("\nCount the values: \n",product_prices.value_counts())

# DataFrames
'''

data = {
    "Product": ['shoes','mobile','mobile','ear buds','watch'],
    "Brand" : ['nike',"oppo","iphone","boat",'rolex'],
    "Price": [4999,14999,129999,999,99999],
    "Stock" : [50,40,40,50,30],
    "BestSeller": [True,False,True,False,True]
}

df = pd.DataFrame(data)
print(df)
print("\n--Head of the products: \n",df.head(2))
print("\n--Tail of the products:\n",df.tail(2))
print("\n--Shape of the DataFrame:\n",df.shape)
print("\n--Columns in DataFrame;\n",df.columns)
print("\n--Index of DataFrame:\n",df.index)
print("\n--DataFrame Info:\n",df.info)
print("\n--Describe the Data: \n",df.describe())
print(df)
print("\n--Find the particular item:\n",df.loc[1,"Product"])
print(df)
print("\n--Find the particular item by using index:\n",f'₹.{df.iloc[1,2]}')

print("\n--Using iloc (Selecting a particular row):\n",df.iloc[1])

print(df)
print("\n--Using loc (selecting particular row) based on cond:\n",df.loc[df['Price']>1000])

print(df)
print("\n",df.loc[df['BestSeller']==True])
print("\n",df.loc[df["Product"]=='mobile'])

print("Before df:\n",df)
df_dropped = df.drop(columns=["Stock"])                             # temporarly del
print("After Dropping 'Stock' Column:\n",df_dropped)
print("After df:\n",df)

#print("Before df:\n",df)
#df_dropped_per = df.drop(columns=['Stock'],inplace=True)            # permanant del
#print("After Dropping 'Stock' Column:\n", df_dropped_per)
#print("After df:\n",df)

print("Before df:\n",df)
# temporary
df_renamed = df.rename(columns={'Price' : "Cost"})
print("After Renaming 'Price' to 'Cost':\n", df_renamed)
# permanant
#df_renamed_per = df.rename(columns={'Stock' : 'Stock Price'},inplace=True)
#print("After Permanant changed: \n",df_renamed_per)
print("After df:\n",df)

grouped = df.groupby("Product").agg({"Price":["sum","min"], "Stock" : "sum"})
print("Grouped Data:\n",grouped)
grouped_one_thing = df.groupby("Product")['Price'].mean()
print("Grouped One of the Data Changed:\n",grouped_one_thing)

print(df)

data2 = {
    "Brand": ['nike', 'oppo', 'iphone', 'boat', 'rolex'],
    "Rating" : [4.2, 5.0, 4.5, 4.2, 3.9]
}

df_ratings = pd.DataFrame(data2)
print("After Data:\n",df_ratings)

print("\nBefore Adding Ratings:\n",df)

df_merged = df.merge(df_ratings, on="Brand")
print("\nAfter Adding the Ratings (Merging): \n",df_merged)          # temporaryly merged

# Adding column
data3 = {
    "Product": "ipad",
    'Brand' : "apple",
    "Price" : [69999],
    "Stock" : [50],
    "BestSeller" : [True]
}
df_new = pd.DataFrame(data3)
print(df_new)

df_concat = pd.concat([df,df_new], ignore_index=True)
print(df_concat)

print("Accessing Column:\n",df["Price"])
print("Accessing more than one Column:\n",df[["Price","BestSeller","Product"]])

df["Price"] = df["Price"].astype(float)
print("Changing the Datatype:\n",df)

df["Rank"] = df["Price"].rank(ascending=False)
print("After adding Rank: ",df)

print("Sorted by Rank:\n",df.sort_values(by="Rank",ascending=False))
#print("Sort Values \n",df.sort_values(by="Price", ascending=False))

print("After sorted:\n",df)

df1 = pd.DataFrame(
    {
        "ID":[1,2],
        "Name": ["Mani","Aditya"],
        "Age":[21,22]
    })

df2 = pd.DataFrame({
    "ID":[1,2],
    "Name": ["Eswar","Venky"],
    "Age":[23,24]
})

df_combined = pd.concat([df1,df2], axis=0)
print(df_combined)

df_combined = pd.concat([df1,df2], axis=1)
print(df_combined)


print("Given Data;\n",df)
df_pivot_table = df.pivot_table(values="Price", index="Product", columns="Stock", aggfunc="max")
print("\nCreate a Table: \n\n",df_pivot_table)

#print("Given Data;\n",df)
#df_cross_table = pd.crosstab(df["Brand"], df["Price"])
#print("Create a Table '0' or '1'",df_cross_table)