import streamlit as st
from components.data_processing import (
    create_daily_orders_df,
    create_sum_order_items_df,
    create_bygender_df,
    create_byage_df,
    create_bystate_df,
    create_rfm_df
)
from components.charts import (
    daily_orders_chart,
    product_performance_chart,
    customer_demographic_chart,
    best_customer_chart
)
from components.utils import load_and_prepare_data

# Load cleaned data
all_df = load_and_prepare_data("all_data.csv")

# Filter data (rentang waktu)
min_date = all_df["order_date"].min()
max_date = all_df["order_date"].max()

start_date, end_date = st.date_input(
    label='Rentang Waktu', min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Load data sesuai dengan rentang waktu
main_df = all_df[(all_df["order_date"] >= str(start_date)) & 
                (all_df["order_date"] <= str(end_date))]

# Menyiapkan seluruh dataframe
daily_orders_df    = create_daily_orders_df(main_df)
sum_order_items_df = create_sum_order_items_df(main_df)
bygender_df        = create_bygender_df(main_df)
byage_df           = create_byage_df(main_df)
bystate_df         = create_bystate_df(main_df)
rfm_df             = create_rfm_df(main_df)

# Show Charts
daily_orders_chart(daily_orders_df)
product_performance_chart(sum_order_items_df)
customer_demographic_chart(bygender_df, byage_df, bystate_df)
best_customer_chart(rfm_df)

st.caption('Copyright © 2024')
