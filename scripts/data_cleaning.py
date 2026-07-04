import pandas as pd 

df=pd.read_csv("data/customer_shopping_behavior.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())



#feature_engineering............................................

#Age Group
bins=[18,25,35,45,60,100]
labels=["18-25","26-35","36-45","46-60","60+"]
df["Age Group"]=pd.cut(df["Age"],bins=bins,labels=labels)
print(df["Age Group"])

# High Value Customer
df["High Value Customer"]=df["Purchase Amount (USD)"]>100
print(df["High Value Customer"])

#Rating Category 
def rating(x):
    if x >=4:
        return "Exelent"
    elif x >=3:
        return "Good"
    else:
        return "Poor"

df["Rating Category"]=df["Review Rating"].apply(rating)
print(df["Rating Category"])


# save the file.....................

df.to_csv("cleaned_data/customer_shopping.csv")