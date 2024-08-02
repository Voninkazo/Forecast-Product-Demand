import streamlit as st
import pandas as pd

st.title("Filter data")

# Load data from CSV file
data = pd.read_csv('data/car_parts_monthly_sales.csv')

# Create multiselect widgets for filtering by age and city
selected_age = st.multiselect('Select age(s) to filter:', data['parts_id'].unique())
selected_city = st.multiselect('Select city(s) to filter:', data['volume'].unique())

# Text input for filtering by name
search_term = st.text_input('Search by volume:', '')

# Date picker for filtering by registration date
selected_date = st.date_input('Select a date:', 'today')

if selected_age and selected_city:
    # Filter the dataframe based on both selected age and city
    filtered_data = data[(data['parts_id'].isin(selected_age)) & (data['volume'].isin(selected_city))]
elif selected_age or selected_city:
    # Filter the dataframe based on either selected age or city
    filtered_data = data[(data['parts_id'].isin(selected_age)) | (data['volume'].isin(selected_city))]
elif search_term:
    # Filter the dataframe based on the search term
    try:
        search_number = int(search_term)
        filtered_data = data[data['volume'] == search_number]
    except ValueError:
        filtered_data = data[data['volume'].str.contains(search_term, case=False)]
elif selected_date:
    # Filter the dataframe based on the selected date
    filtered_data = data[data['date'] == selected_date]
else:
    filtered_data = data

st.write(filtered_data)
