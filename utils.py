import pandas as pd
import numpy as np

# Create a list from a csv file
def csv_list_row_values(file, row_name):
    csv = pd.read_csv(file)
    list = csv[row_name].tolist()
    return list

# Add a row to a csv file
def csv_add_row(file, new_data):
    # Read existing CSV into a DataFrame
    df = pd.read_csv(file)

    # currently broken