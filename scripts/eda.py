import pandas as pd 

df=pd.read_csv("cleaned_data/customer_shopping.csv")

print(df.head(3))

#1 Total Revenue...................
print(df["Purchase Amount (USD)"].sum())
#2 Average Purchase
print(df["Purchase Amount (USD)"].mean())
#3 Highest Purchase
print(df["Purchase Amount (USD)"].max())
#4 Lowest Purchase
print(df["Purchase Amount (USD)"].min())
#5 Number of Customers
print(df["Customer ID"].count())


#.............Customer Analysis...................

#Top Spending Customers..................
Top_Customers = df.groupby("Customer ID").agg(
    Total_spends=("Purchase Amount (USD)","sum")
).sort_values("Total_spends",ascending=False)

print(Top_Customers.head(10))

#Average Spending by Gender.............
Avg_spend= df.groupby("Gender").agg(
    Total_spends=("Purchase Amount (USD)","mean")
)
print(Avg_spend)

#Average Spending by Age Group............
Avg_spend= df.groupby("Age Group").agg(
    Total_spends=("Purchase Amount (USD)","mean")
)
print(Avg_spend)

#Subscription vs Spending..................
print(df.groupby("Subscription Status")["Purchase Amount (USD)"].mean())

#........................Product Analysis..................

#Most Purchased Items...........
print(df["Item Purchased"].value_counts())
#Category Sales
print(df.groupby("Category")["Purchase Amount (USD)"].sum())
#Best Selling Color
print(df["Color"].value_counts())
#Best Selling Size
print(df["Size"].value_counts())


#...............Location Analysis.................
#Revenue by Location
print(df.groupby("Location")["Purchase Amount (USD)"].sum().sort_values(ascending=False))
#Average Spending by Location
print(df.groupby("Location")["Purchase Amount (USD)"].mean())
#Seasonal Analysis
print(df.groupby("Season")["Purchase Amount (USD)"].sum())
#Highest Rated Season
print(df.groupby("Season")["Review Rating"].mean())


#..................Discount Analysis...................
#Discount vs Purchase
print(df.groupby("Discount Applied")["Purchase Amount (USD)"].mean())
#Promo Code Usage
print(df["Promo Code Used"].value_counts())
#Payment Analysis
print(df["Payment Method"].value_counts())
#Payment Method Revenue
print(df.groupby("Payment Method")["Purchase Amount (USD)"].sum())

#Review Analysis
#Average Rating by Category
print(df.groupby("Category")["Review Rating"].mean())
#Highest Rated Item
print(df.groupby("Item Purchased")["Review Rating"].mean().sort_values(ascending=False))

#Customer Loyalty
#Previous Purchases
print(df.groupby("Previous Purchases")["Purchase Amount (USD)"].mean())
#Purchase Frequency
print(df["Frequency of Purchases"].value_counts())
#Weekly Customers Spending
print(df[df["Frequency of Purchases"]=="Weekly"]["Purchase Amount (USD)"].mean())

#Advanced Analysis
#Top 10 Locations
location=df.groupby("Location").agg(
    Revenue=("Purchase Amount (USD)","sum")
).sort_values(by="Revenue",ascending=False)

print(location.head(10))

#Top Categories in Each Season
pivot=df.pivot_table(
    values="Purchase Amount (USD)",
    index="Season",
    columns="Category",
    aggfunc="sum"
)

print(pivot)

#Correlation
print(df[["Age","Purchase Amount (USD)","Review Rating","Previous Purchases"]].corr())
#Highest Revenue Combination
combo=df.groupby(["Gender","Category"]).agg(
    Revenue=("Purchase Amount (USD)","sum")
).sort_values(by="Revenue",ascending=False)

print(combo)