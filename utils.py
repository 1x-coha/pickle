import pandas as pd
import numpy as np


# Create a list from a csv file
def csv_list(file, cols):
    df = pd.read_csv(file)
    new_df = df[cols]
    list = new_df.values.tolist()
    return list


# Add a row to a csv file
def csv_add_row(file_path, new_row, id_label):
    # Read existing CSV into a DataFrame
    df = pd.read_csv(file_path)

    # Extract numeric part of IDs, convert to integers, and get the maximum
    df['id_num'] = df['ID'].str.replace(id_label, '').astype(int)
    id_num = df['id_num'].max()

    # Increment the highest ID and format it with the prefix
    new_id = f"{id_label}{id_num + 1}"
    new_row['ID'] = new_id

    # Drop the temporary 'id_num' column
    df = df.drop(columns=['id_num'])

    # Add new row data to df
    df = pd.concat([df, new_row], ignore_index=True)

    # Write df to csv
    df.to_csv(file_path, index=False)


# Sort a DF by ID ascending
def df_sort_by_id(df):
    df = df.sort_values(by='ID', ascending=True)
    return df