import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set_theme(style='dark')

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

def daily_orders_chart(daily_orders_df):
    st.header('Dicoding Collection Dashboard :sparkles:')
    st.subheader('Daily Orders')

    col1, col2 = st.columns(2)

    with col1:
        total_orders = daily_orders_df.order_count.sum()
        st.metric("Total orders", value=total_orders)

    with col2:
        total_revenue = format_currency(daily_orders_df.revenue.sum(), "AUD", locale='es_CO') 
        st.metric("Total Revenue", value=total_revenue)

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        daily_orders_df["order_date"],
        daily_orders_df["order_count"],
        marker='o', 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)

def product_performance_chart(sum_order_items_df):
    st.subheader("Best & Worst Performing Product")

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

    sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Number of Sales", fontsize=30)
    ax[0].set_title("Best Performing Product", loc="center", fontsize=50)
    ax[0].tick_params(axis='y', labelsize=35)
    ax[0].tick_params(axis='x', labelsize=30)

    sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.sort_values(by="quantity_x", ascending=True).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Number of Sales", fontsize=30)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Worst Performing Product", loc="center", fontsize=50)
    ax[1].tick_params(axis='y', labelsize=35)
    ax[1].tick_params(axis='x', labelsize=30)

    st.pyplot(fig)

def customer_demographic_chart(bygender_df, byage_df, bystate_df):
    st.subheader("Customer Demographics")

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(20, 10))

        sns.barplot(
            y="customer_count", 
            x="gender",
            data=bygender_df.sort_values(by="customer_count", ascending=False),
            palette=colors,
            ax=ax
        )
        ax.set_title("Number of Customer by Gender", loc="center", fontsize=50)
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(20, 10))
        
        sns.barplot(
            y="customer_count", 
            x="age_group",
            data=byage_df.sort_values(by="age_group", ascending=False),
            palette=colors,
            ax=ax
        )
        ax.set_title("Number of Customer by Age", loc="center", fontsize=50)
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="customer_count", 
        y="state",
        data=bystate_df.sort_values(by="customer_count", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of Customer by States", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)

def best_customer_chart(rfm_df):
    st.subheader("Best Customer Based on RFM Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        avg_recency = round(rfm_df.recency.mean(), 1)
        st.metric("Average Recency (days)", value=avg_recency)

    with col2:
        avg_frequency = round(rfm_df.frequency.mean(), 2)
        st.metric("Average Frequency", value=avg_frequency)

    with col3:
        avg_monetary = format_currency(rfm_df.monetary.mean(), "AUD", locale='es_CO') 
        st.metric("Average Monetary", value=avg_monetary)

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(35, 15))
    colors = ["#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9"]

    sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("customer_id", fontsize=30)
    ax[0].set_title("By Recency (days)", loc="center", fontsize=50)
    ax[0].tick_params(axis='y', labelsize=30)
    ax[0].tick_params(axis='x', labelsize=35)

    sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("customer_id", fontsize=30)
    ax[1].set_title("By Frequency", loc="center", fontsize=50)
    ax[1].tick_params(axis='y', labelsize=30)
    ax[1].tick_params(axis='x', labelsize=35)

    sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
    ax[2].set_ylabel(None)
    ax[2].set_xlabel("customer_id", fontsize=30)
    ax[2].set_title("By Monetary", loc="center", fontsize=50)
    ax[2].tick_params(axis='y', labelsize=30)
    ax[2].tick_params(axis='x', labelsize=35)

    st.pyplot(fig)
