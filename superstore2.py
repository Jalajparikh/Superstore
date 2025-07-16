# === Import Libraries ===
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Load Dataset with Safe Encoding ===
try:
    df = pd.read_csv("Superstore.csv", encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv("Superstore.csv", encoding='ISO-8859-1')  # Fallback

# === Convert Order Date to datetime ===
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month_name()
df['Year'] = df['Order Date'].dt.year

# === Category-wise Sales & Profit ===
category_group = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
category_group.plot(kind='bar', figsize=(8, 5), title="Sales and Profit by Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

# === Region-wise Profit ===
region_profit = df.groupby('Region')['Profit'].sum().sort_values()
region_profit.plot(kind='barh', color='skyblue', title="Profit by Region")
plt.xlabel("Profit")
plt.tight_layout()
plt.show()

# === Segment-wise Performance ===
seg_perf = df.groupby('Segment')[['Sales', 'Profit']].sum()
seg_perf.plot(kind='bar', figsize=(8, 4), title="Sales & Profit by Customer Segment")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

# === Monthly Sales Trend ===
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
monthly_sales.plot(figsize=(12, 5), title="Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Date")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Top & Bottom Sub-Categories by Profit ===
subcat = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values(by='Profit')
colors = ['red' if p < 0 else 'green' for p in subcat['Profit']]
fig, ax = plt.subplots(figsize=(10, 6))
subcat['Profit'].plot(kind='barh', ax=ax, color=colors)
plt.title("Profit by Sub-Category")
plt.xlabel("Profit")
plt.tight_layout()
plt.show()
print("EDA completed")
