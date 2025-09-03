import pandas as pd
import matplotlib.pyplot as plt

# 1) CSV load
df = pd.read_csv("sales_data.csv")

# 2) Date ko datetime me convert
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

# 3) Month name nikaal lo
df["Month"] = df["Date"].dt.month_name()

# 4) Month-wise total sales
monthly = df.groupby("Month")["Sales"].sum()

# 5) Month ko calendar order me lane ke liye reindex
order = ["January","February","March","April","May","June",
         "July","August","September","October","November","December"]
monthly = monthly.reindex(order)

# 6) Print nicely
print("=== Monthly Total Sales ===")
for m, v in monthly.items():
    print(f"{m:>9}: {v}")

# 7) Bar chart
ax = monthly.plot(kind="bar", rot=45, title="Monthly Sales (2025)")
ax.set_xlabel("Month")
ax.set_ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")  # image file save
plt.show()
