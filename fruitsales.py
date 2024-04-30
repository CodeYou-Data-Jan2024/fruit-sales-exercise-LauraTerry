import pandas as pd 
data = {"2017 Sales": [35, 21], "2018 Sales": [41,34]}

fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=["2017 Sales", "2018 Sales"] )
print(fruit_sales)
fruit_sales.to_csv("fruit.csv")