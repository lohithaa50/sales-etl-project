import pandas as pd
customers=pd.read_csv("data/customers.csv")
products=pd.read_csv("data/products.csv")
orders=pd.read_csv("data/orders.csv")

customers = customers.drop_duplicates(subset=["CustomerID"])
customers["CustomerName"] = customers["CustomerName"].str.strip()
customers["City"] = customers["City"].str.upper()

products = products.drop_duplicates(subset=["ProductID"])
products["ProductName"] = products["ProductName"].str.strip()
products["Price"] = products["Price"].astype(float)

orders = orders.drop_duplicates(subset=["OrderID"])
orders["Quantity"] = orders["Quantity"].astype(int)
result = pd.merge(orders, customers, on="CustomerID", how="inner")
result = pd.merge(result, products, on="ProductID", how="inner")
result["TotalSales"] = result["Quantity"] * result["Price"]
result = result.sort_values(by="TotalSales", ascending=False)
result.to_csv("output/finalsales.csv", index=False)