# retail-dashboard

# Retail Analytics & Customer Segmentation Dashboard

## Project Overview

This project analyzes a dataset of **1,800 customer purchase records** to uncover sales trends, product performance, and customer retention patterns. The core of the project is a **Python-based interactive dashboard** built with Streamlit and Plotly, which allows users to filter data dynamically.

The primary business goals were:

1.  **RFM Segmentation:** Classifying customers based on Recency, Frequency, and Monetary value.
2.  **Sales Trend Analysis:** Understanding revenue patterns over time.
3.  **Payment Behavior:** Analyzing how customers prefer to pay.

-----

## Key Data Insights

Based on the analysis of the `Customer Purchase History` dataset, the following key trends were identified:

### 1\. Customer Retention (RFM Analysis)

  * **High Churn Risk:** A staggering **91% of customers** are one-time buyers.
  * **Segment Distribution:**
      * **Potential Loyalists:** The largest segment. These are recent buyers who need nurturing to encourage a second purchase.
      * **At Risk / Lost:** A significant portion of the base has not purchased in over a year.
      * **Champions:** Only a tiny fraction (\<1%) are high-frequency, high-spend repeat customers.
  * **Actionable Insight:** The business needs a post-purchase email marketing campaign to convert the massive volume of "Potential Loyalists" into repeat buyers.

### 2\. Product Performance

  * **Top Performer:** **Tablets** are the highest revenue-generating category, contributing approximately **$533k**.
  * **Balanced Portfolio:** Unlike typical retail scenarios following the Pareto Principle (80/20 rule), revenue here is well-distributed across all 5 categories (Tablets, Laptops, Monitors, Desks, Phones). No single product dominates the sales.

### 3\. Payment Behavior

  * **Even Split:** Payment preferences are remarkably evenly distributed (\~20% each) across **Cash, Credit Card, Debit Card, Gift Card, and Online Payments**.
  * **Insight:** Customers are comfortable with all provided payment gateways; no specific method acts as a friction point.

-----

## Dashboard Features

The interactive dashboard includes:

  * **KPI Metrics:** Real-time display of Total Revenue, Average Order Value (AOV), and Active Customer count.
  * **Dynamic Filters:** Sidebar dropdown to filter analysis by Product Category.
  * **Interactive Charts:**
      * 📈 **Revenue Trend (Area Chart):** Visualizes daily sales performance.
      * 💳 **Payment Distribution (Donut Chart):** Shows the share of each payment method.
      * 👥 **Customer Segments (Bar Chart):** Displays the count of customers in each RFM tier.

-----

## Tech Stack

  * **Language:** Python
  * **Data Processing:** Pandas, NumPy
  * **Visualization:** Plotly Express
  * **Web Framework:** Streamlit

-----

## How to Run Locally

Follow these steps to run the dashboard on your own machine:

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/retail-dashboard.git
cd retail-dashboard
```

**2. Install dependencies**
Ensure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

**3. Run the App**

```bash
streamlit run app.py
```

The dashboard will open automatically in your default web browser at `http://localhost:8501`.

-----

## Project Structure

```text
├── app.py                 # Main application code
├── data.csv               # Raw dataset (Customer Purchase History)
├── requirements.txt       # Python libraries required
└── README.md              # Project documentation
```

-----

## 🔮 Future Improvements

  * **Predictive Analytics:** Implement a Machine Learning model to predict which "Potential Loyalists" are most likely to churn.
  * **Basket Analysis:** Analyze which products are frequently bought together (e.g., Monitor + Desk).
  * **Drill-down:** Add ability to click on a specific RFM segment to see the list of customer emails for marketing export.
