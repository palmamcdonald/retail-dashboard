import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

st.set_page_config(page_title="Retail Dashboard", layout="wide")

try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    st.error("File not found. Please ensure data.csv is in the repository.")
    st.stop()

df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

ref_date = df['PurchaseDate'].max() + datetime.timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'PurchaseDate': lambda x: (ref_date - x.max()).days,
    'CustomerID': 'count',
    'TotalPrice': 'sum'
}).rename(columns={'PurchaseDate': 'Recency', 'CustomerID': 'Frequency', 'TotalPrice': 'Monetary'})

rfm['R_Score'] = pd.qcut(rfm['Recency'].rank(method='first'), 5, labels=[5, 4, 3, 2, 1])
rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])

def score_freq(x):
    if x == 1: return 1
    elif x == 2: return 3
    else: return 5
rfm['F_Score'] = rfm['Frequency'].apply(score_freq)

def get_segment(row):
    score = int(row['R_Score']) + int(row['F_Score']) + int(row['M_Score'])
    if score >= 13: return 'Champions'
    elif score >= 10: return 'Loyal'
    elif score >= 7: return 'Promising'
    elif score >= 5: return 'At Risk'
    else: return 'Lost'

rfm['Segment'] = rfm.apply(get_segment, axis=1)

st.sidebar.header("Filters")
categories = ['All'] + sorted(df['ProductCategory'].unique().tolist())
selected_category = st.sidebar.selectbox("Category", categories)

if selected_category != 'All':
    df = df[df['ProductCategory'] == selected_category]

total_revenue = df['TotalPrice'].sum()
avg_order = df['TotalPrice'].mean()
total_customers = df['CustomerID'].nunique()

st.title("Retail Analytics Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Avg Order Value", f"${avg_order:,.0f}")
col3.metric("Active Customers", total_customers)

st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    daily_sales = df.groupby('PurchaseDate')['TotalPrice'].sum().reset_index()
    fig_trend = px.area(daily_sales, x='PurchaseDate', y='TotalPrice', title="Revenue Trend")
    st.plotly_chart(fig_trend, use_container_width=True)

with c2:
    payment_counts = df.groupby('PaymentMethod')['TotalPrice'].sum().reset_index()
    fig_pie = px.pie(payment_counts, values='TotalPrice', names='PaymentMethod', title="Payment Distribution")
    st.plotly_chart(fig_pie, use_container_width=True)

segment_counts = rfm['Segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'Count']
fig_seg = px.bar(segment_counts, x='Segment', y='Count', color='Segment', title="Customer Segments")
st.plotly_chart(fig_seg, use_container_width=True)