# -*- coding: utf-8 -*-



#load the packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the sample marketing data
data = pd.read_csv('samplepython.csv')

# Streamlit app title
st.title('Marketing Data Analysis')

# Sidebar - Dropdown to select metric (impressions or clicks)
selected_metric = st.sidebar.selectbox('Select Metric:', ('Impressions', 'Clicks','Conversions'))

# Group by category and calculate the total metric value
category_metrics = data.groupby('Category')[selected_metric].sum()

# Bar chart to display the results using Matplotlib
st.write(f'Total {selected_metric} by Category')

fig, ax = plt.subplots(figsize=(10, 6))
category_metrics.plot(kind='bar', ax=ax)
ax.set_xlabel('Category')
ax.set_ylabel(selected_metric)
st.pyplot(fig)
