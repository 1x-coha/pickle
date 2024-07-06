import streamlit as st
import pandas as pd
import numpy as np


# Data sources
data_dir = 'data/'
routines = data_dir + 'routines.csv'


# Create a list of strings from csv columns
def csv_list(csv, cols):
    df = pd.read_csv(csv)
    new_df = df[cols]
    list = new_df.values.tolist()
    return list


# Add a row to a csv
def csv_add_row(file_path, new_row, id_label):
    try:
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

        return True
    except Exception as e:
        st.error(f'Error: {e}')
        return False


# Sort a DF by ID ascending
def df_sort_by_id(df):
    df = df.sort_values(by='ID', ascending=True)
    return df


# Streamlit app title
st.title('Pickle')
':cucumber: *A training data tracker for robot operators*'


# Tabs
tab1, tab2, tab3, tab4 = st.tabs(['Plan', 'Collect', 'Train', 'Test'])

# Tab 1: Plan
with tab1:
    '## Routine'

    # Expander to display current csv contents
    with st.expander(':pencil: Edit routines data', expanded=False):
        df = pd.read_csv(routines)
        st.data_editor(df)

    # Expander to create a new routine
    with st.expander(':sparkles: New routine', expanded=False):
        # Input fields
        new_name = st.text_input('Name')
        new_url = st.text_input('Jira issue url')
        new_libs = st.text_input('Skill libraries')

        # Button to add new row to csv
        if st.button('Create'):
            # Add new data row as dict
            new_data = {
                'ID': '',
                'Name': new_name,
                'URL': new_url,
                'Libraries': ''
            }

            # Convert dict to df
            new_data = pd.DataFrame(new_data, index=[0])

            # Add new row
            if (csv_add_row(routines, new_data, 'ROU-')):
                st.success('New routine created')
            else:
                st.failure('Failed to create routine')
    
    # Select box to select project from list
    projects = csv_list(routines, ['ID','Name'])
    selected_project = st.selectbox('Selected project', projects)

    # TODO Button to delete or hide selected project
    st.button('Trash project')
