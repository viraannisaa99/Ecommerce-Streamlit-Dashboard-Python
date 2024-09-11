import pandas as pd

def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)

    datetime_columns = ["order_date", "delivery_date"]
    df.sort_values(by="order_date", inplace=True)
    df.reset_index(inplace=True)

    for column in datetime_columns:
        df[column] = pd.to_datetime(df[column])

    return df
