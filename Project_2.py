#!/usr/bin/env python
# coding: utf-8

# In[19]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# In[20]:


def load_data():
    return pd.read_excel('Vrinda Store Data Analysis(1).xlsx')

data = load_data()
data['Date'] = pd.to_datetime(data['Date'])
data.head()

Analytical Insights

Sales Trends and Seasonality:
Periodic Analysis: Identifying how sales fluctuate over time (daily, weekly, monthly) can reveal patterns such as peak shopping times or seasonal trends.
Growth Trends: Observing whether there is an overall upward or downward trend in sales can indicate the health and growth of the business.

Customer Demographics:
Target Audience: The age and gender distribution provides insights into the primary customer base of the store. This can inform targeted marketing and product selection.
Market Expansion Opportunities: Understanding which demographics are underrepresented in the customer base could reveal new market opportunities.

Product Performance:
Category Sales: Analysis of sales by category helps identify which products are the most popular and profitable. This can guide inventory management and promotional strategies.
Price Points: Examining the range of transaction values can offer insights into the spending habits of customers.

Geographic Reach:
Regional Performance: The distribution of sales across different regions indicates where the business is performing well and where there may be room for market penetration.
Logistics Optimization: Sales concentration in certain areas could suggest where to focus logistics and distribution resources.

Order Status and Efficiency:
Operational Efficiency: The breakdown of order statuses (like 'Delivered', 'Pending') provides an understanding of the operational efficiency and can highlight areas for improvement in the supply chain or customer service.
Customer Experience: A high rate of order fulfillment (Delivered status) is typically indicative of a positive customer experience.

Sales Channels:
Channel Effectiveness: If the dataset includes sales channels (e.g., online, in-store, third-party platforms), analyzing which channels are most effective can inform marketing and sales strategies.

Revenue Streams:
Main Revenue Drivers: Identifying the main drivers of revenue (e.g., specific products, customer segments, regions) can help focus business efforts and resources.
Revenue Fluctuations: Understanding the causes of any significant fluctuations in revenue can aid in strategic planning and risk management.
# # Date Filter

# 

# In[21]:


# Sidebar for date range selection
st.sidebar.header('Filters')
date_range = st.sidebar.date_input("Select Date Range", [])

# Filtering data based on date range
if date_range:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])
    data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]


# # Sales Over Time

# In[22]:


import matplotlib.dates as mdates

# Plot Sales Over Time
st.write("Sales Over Time:")
sales_over_time = data.groupby('Date')['Amount'].sum()

plt.figure(figsize=(10, 5))
plt.plot(sales_over_time, marker='o', color='royalblue', linestyle='-')
plt.title('Sales Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.grid(True)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=15))
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)


# Objective:
# To analyze the sales data over time to identify trends, patterns, and seasonal variations that can inform business strategy and decision-making.
# 
# Analysis:
# 
# Data Utilized: Sales data, including order dates and sales amounts, were compiled and organized to analyze trends over various time frames (daily, monthly, quarterly, or annually).
# Trend Identification: A time-series analysis was performed to observe the trajectory of sales over the specified periods. This includes identifying upward or downward trends and noting any significant changes or anomalies.
# Seasonality Assessment: The analysis focused on uncovering seasonal patterns, such as increased sales during holidays or specific months, which could indicate consumer buying behavior aligned with seasonal events or promotions.
# 
# Interpretations:
# 
# Overall Sales Trends: The direction of the sales trend (increasing, decreasing, or stable) over time provides a high-level view of business growth or decline. An upward trend indicates growing sales and possibly an expanding customer base, while a downward trend might suggest a need for strategic revision.
# Seasonal Fluctuations: Identifying periods of higher sales can indicate consumer preferences tied to specific times of the year. For instance, a surge in sales during the holiday season can highlight the effectiveness of holiday promotions.
# Anomalies and Irregularities: Any unexpected spikes or drops in sales could be linked to external events, operational changes, or marketing campaigns, warranting further investigation.
# 
# Managerial Implication:
# 
# Strategic Planning and Forecasting: Insights from sales trends are crucial for forecasting future sales, budget allocation, and inventory management. Understanding peak sales periods ensures adequate stock and staffing levels.
# Marketing and Promotional Strategies: Knowledge of seasonal trends can guide the timing and nature of marketing campaigns. Aligning promotions with high-sales periods can maximize revenue, while targeted strategies during low-sales periods can help stimulate demand.
# Business Growth Analysis: Long-term sales trends are indicators of business health and market position. They can inform decisions on expansion, diversification, and investment.
# Response to Market Dynamics: Quick identification of anomalies allows for a rapid response to market changes or operational challenges, ensuring that the business remains agile and customer-focused.

# # Sales By Category

# In[23]:


# Sales by Category
st.write("Sales by Category:")
sales_by_category = data.groupby('Category')['Amount'].sum()

plt.figure(figsize=(10, 6))
sales_by_category.plot(kind='bar', color='skyblue')
plt.title('Sales by Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')
st.pyplot(plt)


# Objective:
# To evaluate the sales performance across different product categories, aiming to identify which categories are most popular, profitable, and contribute significantly to the overall revenue.
# 
# Analysis:
# 
# Data Utilization: The analysis involved grouping sales data by product categories and summing up the sales amounts within each category.
# Category Comparison: The total sales for each category were compared to identify which categories are the top performers and which are underperforming.
# Sales Contribution: The contribution of each category to the total sales was assessed to understand their relative importance to the business’s revenue.
# 
# Interpretations:
# 
# Top Performing Categories: Identifying categories with the highest sales can reveal customer preferences and market trends. These categories are likely driving the bulk of the revenue and might be reflective of effective product placement or marketing.
# Underperforming Categories: Categories with lower sales may indicate a lack of customer interest or market saturation. These require further analysis to determine if they should be maintained, improved, or phased out.
# Market Trends and Preferences: Fluctuations in category popularity can signal changing market trends or shifts in consumer preferences, necessitating adjustments in inventory or marketing strategies.
# 
# Managerial Implication:
# 
# Inventory Management: Insights from category sales performance can guide inventory stocking decisions, ensuring that high-demand products are adequately stocked while reducing excess inventory in less popular categories.
# Marketing Focus: Marketing efforts can be strategically aligned with the top-performing categories to maximize their revenue potential. For underperforming categories, reevaluation of marketing strategies or product improvements might be necessary.
# Product Development and Diversification: Understanding which categories are popular can inform product development strategies, potentially leading to the introduction of new products within these categories or diversification into related areas.
# Pricing Strategies: Sales data by category can inform pricing strategies, such as adjusting prices to optimize sales in competitive categories or using promotional offers to boost interest in less popular categories.

# # Customer Demographics

# In[24]:


# Customer Demographics
st.write("Customer Demographics:")

# Age Distribution
plt.figure(figsize=(10, 5))
plt.hist(data['Age'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Age Distribution of Customers', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.grid(axis='y')
st.pyplot(plt)

# Gender Distribution
gender_count = data['Gender'].value_counts()

plt.figure(figsize=(10, 5))
gender_count.plot(kind='bar', color=['salmon', 'lightblue'])
plt.title('Gender Distribution of Customers', fontsize=16)
plt.xlabel('Gender', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.xticks(rotation=0)
st.pyplot(plt)


# Objective:
# To analyze the demographic profile of the customer base, focusing on age and gender distribution. This analysis aims to understand the composition of the store's clientele and inform targeted marketing and product strategies.
# 
# Analysis:
# 
# Data Utilization: The dataset includes customer age and gender, which were used to assess the demographic spread of the customer base.
# Age Distribution Analysis: The age data was categorized into meaningful groups (e.g., 18-25, 26-35, etc.) to observe predominant age segments.
# Gender Distribution Analysis: The proportion of customers across different gender groups was calculated to understand gender-wise division in the customer base.
# 
# Interpretations:
# 
# Predominant Age Groups: Identifying which age groups are most prevalent among customers helps in understanding the primary market. For instance, a younger customer base might indicate a trend towards more contemporary or trendy products.
# Age-Related Trends: Different age groups might exhibit unique buying patterns, preferences, and spending behavior. Such insights are crucial for tailoring product offerings, marketing messages, and customer experience.
# Gender Insights: Understanding the gender split is vital for developing gender-specific marketing strategies and product lines. It can also highlight whether the store's product range appeals equally to all genders or if there are opportunities to broaden the appeal.
# 
# Managerial Implication:
# 
# Targeted Marketing Initiatives: Insights into the age and gender demographics enable the creation of targeted marketing campaigns. For instance, digital marketing strategies might be more effective for a younger audience, while traditional media could be better for older demographics.
# Product Assortment and Development: The demographic data can guide decisions about product assortment, ensuring that the products align with the preferences of the predominant customer segments. This can also influence new product development, ensuring that new offerings resonate with the target audience.
# Customer Engagement and Loyalty Programs: Tailoring customer engagement strategies and loyalty programs to suit the dominant demographic groups can enhance customer retention and satisfaction. For example, loyalty programs for a younger demographic might focus on digital rewards and social media engagement.
# Inclusive Business Practices: A balanced gender distribution might suggest a broader appeal of the store's offerings. However, a skewed distribution could indicate the need for more inclusive marketing and product diversification to attract underrepresented groups.

# # Geographic Distribution

# In[25]:


# Geographic Distribution of Sales
st.write("Geographic Distribution of Sales:")
sales_by_state = data.groupby('ship-state')['Amount'].sum()

plt.figure(figsize=(12, 6))
sales_by_state.plot(kind='bar', color='purple')
plt.title('Geographic Distribution of Sales', fontsize=16)
plt.xlabel('State', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.xticks(rotation=90)
plt.grid(axis='y')
st.pyplot(plt)


# Objective:
# To examine the distribution of sales across various geographic regions, specifically by analyzing sales data across different states. This analysis aims to identify key markets, regional sales performance, and potential areas for market expansion.
# 
# Analysis:
# 
# Data Utilization: Sales data was grouped by the shipping state (or region) to assess the total sales volume in each area.
# Regional Sales Comparison: A comparative analysis of sales across different states provided an understanding of which regions contribute most to the overall sales and which are underperforming.
# Market Penetration and Reach: The data was also used to gauge the store's market penetration in various regions, identifying both well-established markets and regions with potential growth opportunities.
# 
# Interpretations:
# 
# High-Performance Regions: States with high sales volumes indicate strong market presence and customer base. These regions might be driving the majority of the revenue and can be considered the store's stronghold markets.
# Areas for Growth: Regions with lower sales figures may represent untapped or underpenetrated markets, suggesting potential areas for business expansion or increased marketing efforts.
# Regional Preferences and Trends: Variations in sales across regions can highlight regional market trends, customer preferences, and demand patterns, which can be crucial for region-specific strategies.
# 
# Managerial Implication:
# 
# Resource Allocation and Marketing: Insights into regional sales performance can guide the allocation of resources, including marketing budgets, inventory, and logistics. Focusing efforts on high-performing regions can maximize ROI, while targeted strategies can be developed for regions with growth potential.
# Strategic Expansion Planning: Understanding geographic sales distribution aids in identifying potential new markets for expansion. Decisions about opening new physical stores, optimizing distribution channels, or tailoring online marketing strategies can be informed by these insights.
# Customized Regional Strategies: Recognizing that different regions may have varying preferences and needs, businesses can customize their product offerings, marketing messages, and customer service approaches to resonate with regional market characteristics.
# Supply Chain Optimization: Analysis of sales by region can also inform supply chain strategies, helping to optimize distribution and logistics for efficiency and cost-effectiveness. This includes decisions on warehousing locations, shipping methods, and inventory management tailored to regional demand.
# Competitive Analysis: Understanding the store's performance in various regions relative to competitors can highlight competitive strengths and weaknesses. This allows for strategic positioning and targeted competitive actions in specific regions.

# # Order Status Summary

# In[26]:


# Order Status Summary
st.write("Order Status Summary:")
status_count = data['Status'].value_counts()

plt.figure(figsize=(8, 8))
status_count.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Order Status Summary', fontsize=16)
plt.ylabel('')  # Hide the y-label
st.pyplot(plt)


# Objective:
# To assess the distribution of order statuses within the dataset, such as 'Delivered', 'Pending', 'Canceled', etc. This analysis aims to understand the efficiency of order processing and fulfillment, as well as customer satisfaction levels.
# 
# Analysis:
# 
# Data Utilization: The analysis involved categorizing orders based on their status and calculating the frequency of each status.
# Status Distribution: The distribution of order statuses was visualized using a pie chart, providing a clear and immediate understanding of the proportion of each status category.
# Operational Insight: The count and proportion of each order status offered insights into the operational aspects of order processing, delivery efficiency, and potential bottlenecks.
# 
# Interpretations:
# 
# Order Fulfillment Efficiency: A high proportion of 'Delivered' orders suggests effective order processing and fulfillment operations. It indicates that the majority of customers are receiving their orders as expected.
# Potential Operational Issues: A significant number of orders in statuses like 'Pending', 'Canceled', or other non-delivery statuses could indicate issues in the supply chain, inventory management, or customer service.
# Customer Experience: The status distribution can be a key indicator of customer satisfaction. High fulfillment rates generally correlate with positive customer experiences, while a significant number of delayed or canceled orders might lead to customer dissatisfaction.
# 
# Managerial Implication:
# 
# Process Optimization: Identifying bottlenecks or inefficiencies in order processing can lead to targeted improvements in logistics, inventory management, and customer service.
# Customer Communication: For orders that are in 'Pending' or similar statuses, proactive communication strategies can be implemented to manage customer expectations and enhance satisfaction.
# Policy and Strategy Review: High rates of order cancellations or returns might necessitate a review of policies, product quality, or customer engagement strategies.
# Predictive Analysis for Demand Planning: Understanding the patterns in order statuses can assist in predictive analysis for better demand planning and inventory control.

# # Interactive Tables

# In[27]:


st.write("Data Overview:")
st.dataframe(data.head())

