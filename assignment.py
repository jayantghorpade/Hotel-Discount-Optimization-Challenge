
# -----------------------------------------------
# Hotel Discount Analysis and Optimization Script
# Author: Jayant_G, Developer
# Purpose: Analyze hotel discount effectiveness, revenue impact,
#          and segment hotels for better pricing strategies
# -----------------------------------------------

# This script performs the following tasks:
# 1) Load hotel snapshot dataset from CSV
# 2) Perform basic data cleaning (handle missing values)
# 3) Calculate discount percentages for each record
# 4) Compute booking change per hotel & check-in date
# 5) Analyze discount effectiveness (which discounts lead to more bookings)
# 6) Build simple linear regression model to estimate impact of discount % on bookings
# 7) Identify discount "sweet spots" using binned analysis
# 8) Calculate revenue impact per discount level
# 9) Segment hotels using KMeans clustering
# 10) Visualize relationships between discount % and bookings


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load the dataset from local system
# -----------------------------
data = pd.read_csv("hotels_data.csv")

print("First 5 rows of data:")
print(data.head())
print("\nMissing values per column:")
print(data.isnull().sum())
print("\nData shape:", data.shape)
print("\nColumn names:", data.columns)
print("\nData description:")
print(data.describe())
print("\nInfo about data:")
print(data.info())

# -----------------------------
# 2. Basic Cleaning
# -----------------------------
# Replace -1 values with NaN
data = data.replace(-1, np.nan)

# Drop rows where important values are missing
data = data.dropna(subset=["Original Price", "Discount Price", "Available Rooms"])

#Drop duplicates
data = data.drop_duplicates()
print("drop duplicates",data.shape)

# -----------------------------
# 3. Add discount percentage column
# -----------------------------
# Formula = (Original Price - Discount Price) / Original Price
data["discount_pct"] = (data["Original Price"] - data["Discount Price"]) / data["Original Price"]

# -----------------------------
# 4. Calculate Booking Change
# -----------------------------
data["Snapshot Date"] = pd.to_datetime(data["Snapshot Date"])

# Group by Hotel and Checkin Date
group_cols = ["Hotel Name", "Checkin Date"]
sorted_data = data.sort_values("Snapshot Date")

first_snapshot = sorted_data.groupby(group_cols).first().reset_index()
last_snapshot = sorted_data.groupby(group_cols).last().reset_index()

# Merge first and last
book = first_snapshot.merge(last_snapshot, on=group_cols, suffixes=("_first", "_last"))

# Booking Change = Available Rooms (first) - Available Rooms (last)
book["booking_change"] = book["Available Rooms_first"] - book["Available Rooms_last"]

# -----------------------------
# 5. Discount Effectiveness
# -----------------------------
discount_effect = book.groupby("Discount Code_last")["booking_change"].mean()
discount_effect = discount_effect.sort_values(ascending=False)
print("\nDiscount Effectiveness (avg booking change):")
print(discount_effect.head())

# -----------------------------
# 6. Regression: discount % vs booking change
# -----------------------------
X = book[["discount_pct_last"]].fillna(0)
y = book["booking_change"].fillna(0)

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("\nRegression Results:")
print("Coefficient for discount %:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R2 Score:", r2_score(y, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred)))

# -----------------------------
# 7. Sweet Spot Analysis
# -----------------------------
book["discount_bin"] = pd.cut(book["discount_pct_last"], bins=[0,0.1,0.2,0.3,0.5,1.0])
sweet_spot = book.groupby("discount_bin")["booking_change"].mean()
print("\nAverage Bookings by Discount Bin:")
print(sweet_spot)

plt.figure(figsize=(6,4))
sweet_spot.plot(kind="bar", color="skyblue")
plt.ylabel("Avg Booking Change")
plt.title("Discount Sweet Spot Analysis")
plt.show()

# -----------------------------
# 8. Revenue Impact
# -----------------------------
book["revenue"] = book["booking_change"] * book["Discount Price_last"]
avg_rev = book.groupby("discount_bin")["revenue"].mean()
print("\nAverage Revenue by Discount Bin:")
print(avg_rev)

plt.figure(figsize=(6,4))
avg_rev.plot(kind="bar", color="orange")
plt.ylabel("Avg Revenue")
plt.title("Revenue by Discount Level")
plt.show()

# -----------------------------
# 9. Hotel Segmentation (Clustering)
# -----------------------------
hotel_features = data.groupby("Hotel Name").agg(
    avg_price=("Original Price","mean"),
    avg_discount=("discount_pct","mean"),
    stars=("Hotel Stars","median")
).fillna(0)

kmeans = KMeans(n_clusters=3, random_state=42)
hotel_features["cluster"] = kmeans.fit_predict(hotel_features)

print("\nHotel Clusters:")
print(hotel_features.head())

# -----------------------------
# 10. Scatter plot: Discount % vs Bookings
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(X, y, alpha=0.5, color="green")
plt.xlabel("Discount %")
plt.ylabel("Booking Change")
plt.title("Discount % vs Booking Change")
plt.show()
