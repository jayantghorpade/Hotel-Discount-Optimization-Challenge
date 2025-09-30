---  
# hotel_discount_info.yml

# Hotel Discount Optimization Analysis

**Author:** Jayant_G,
**Project:** Hotel Discount Analysis & Optimization
**Date:** 2025

## Project Overview

Hotels often run discount campaigns to attract customers, but not every discount strategy is effective. Some discounts boost room bookings, while others reduce revenue without increasing occupancy. This project analyzes hotel reservation snapshots to identify the most effective discount strategies across different hotels, dates, and star ratings.

The goal is to help hotels **maximize occupancy without giving away rooms too cheaply**, optimize revenue, and understand how different types of hotels respond to discounts.

## Key Features

1. **Data Cleaning & Preprocessing:**

   * Handle missing values and placeholders.
   * Calculate discount percentages for each hotel snapshot.

2. **Discount Effectiveness Analysis:**

   * Identify which discount codes result in the highest booking potential.
   * Visualize average bookings per discount.

3. **Price Elasticity Modeling:**

   * Build a simple linear regression model to estimate the relationship between discount percentage and bookings.
   * Identify “sweet spots” where discounts maximize bookings without excessive revenue loss.

4. **Revenue Impact Analysis:**

   * Estimate revenue per discount level.
   * Compare revenue across discount bins to optimize pricing.

5. **Hotel Segmentation:**

   * Cluster hotels based on average price, discount strategy, and star ratings.
   * Identify patterns such as “Luxury hotels that rarely discount” vs. “Mid-range hotels that aggressively discount.”

6. **Visualizations:**

   * Scatter plots showing the relationship between discount % and booking changes.
   * Bar charts for booking changes and revenue by discount levels.

## Dataset

#The dataset contains hotel snapshots with the following fields:

* Snapshot ID
* Snapshot Date
* Checkin Date
* Days (length of stay)
* Original Price
* Discount Price
* Discount Code
* Available Rooms
* Hotel Name
* Hotel Stars

Each row represents the state of available rooms and discounts at a given snapshot.

## Technologies Used

* Python 3
* Pandas & NumPy for data analysis
* scikit-learn for linear regression and clustering
* Matplotlib for visualizations

## How to Use

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   ```
2. Install required packages:

   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```
3. Place your dataset `hotels_data.csv` in the project folder.
4. Run the Python script:

   ```bash
   python hotel_discount_analysis.py
   ```

## Insights & Deliverables

* Predictive model for expected bookings under different discount levels.
* Clusters of hotels with distinct discounting strategies.
* Visual dashboards for hotel managers to optimize discounts and maximize revenue.

---

