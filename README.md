# hotel_discount_info.yml

author: "Jayant_G"
project: "Hotel Discount Analysis & Optimization"
date: 2025

project_overview: >
  Hotels often run discount campaigns to attract customers, but not every discount strategy is effective.
  Some discounts boost room bookings, while others reduce revenue without increasing occupancy.
  This project analyzes hotel reservation snapshots to identify the most effective discount strategies
  across different hotels, dates, and star ratings.
  The goal is to help hotels maximize occupancy without giving away rooms too cheaply, optimize revenue,
  and understand how different types of hotels respond to discounts.

key_features:
  - "Data Cleaning & Preprocessing: Handle missing values and calculate discount percentages."
  - "Discount Effectiveness Analysis: Identify which discount codes result in highest booking potential and visualize average bookings."
  - "Price Elasticity Modeling: Build regression model to find sweet spots for discounts."
  - "Revenue Impact Analysis: Estimate revenue per discount level and compare across bins."
  - "Hotel Segmentation: Cluster hotels based on average price, discount strategy, and star ratings."
  - "Visualizations: Scatter plots and bar charts for bookings and revenue."

dataset_fields:
  - "Snapshot ID"
  - "Snapshot Date"
  - "Checkin Date"
  - "Days (length of stay)"
  - "Original Price"
  - "Discount Price"
  - "Discount Code"
  - "Available Rooms"
  - "Hotel Name"
  - "Hotel Stars"

technologies_used:
  - "Python 3"
  - "Pandas"
  - "NumPy"
  - "scikit-learn"
  - "Matplotlib"

how_to_use: >
  1. Clone the repository: git clone <your-repo-url>
  2. Install required packages: pip install pandas numpy scikit-learn matplotlib
  3. Place your dataset `hotels_data.csv` in the project folder.
  4. Run the Python script: python hotel_discount_analysis.py

insights_deliverables:
  - "Predictive model for expected bookings under different discount levels."
  - "Clusters of hotels with distinct discounting strategies."
  - "Visual dashboards for hotel managers to optimize discounts and maximize revenue."
