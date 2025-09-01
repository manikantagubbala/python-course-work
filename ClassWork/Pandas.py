# Pandas.py

import pandas as pd

'''
# series

prices = [199,5999,199,299,545]
products = ['phone','watch','cellphone','buds','shoes']

product_prices = pd.Series(prices,index=products)
print(product_prices)

'''

# DataFrames

data = {
    "Product": ['shoes','mobile','mobile','ear buds','watch'],
    "Brand" : ['nike',"oppo","iphone","boat",'rolex'],
    "Price": [4999,14999,129999,999,99999],
    "Stock" : [50,40,60,50,30],
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