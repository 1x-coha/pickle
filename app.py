import streamlit as st
import pandas as pd
import numpy as np
from utils import csv_list_row_values, csv_add_row

# csv file paths
csv_files = {
    'projects': 'data/projects.csv'
}

# Streamlit app title
st.title('Robot Training :cucumber:')

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(['Plan', 'Collect', 'Train', 'Test'])

# Tab 1: Plan
with tab1:
    '## Project'

    # Fetch project names from csv
    projects = csv_list_row_values(csv_files['projects'], 'Name')

    # Create select box
    selected_project = st.selectbox('Selected project', projects)

    # Expander to display current csv contents
    with st.expander('Show projects table', expanded=False):
        df = pd.read_csv(csv_files['projects'])
        st.write(df)

    # Expander to add new project
    with st.expander('Create a new project', expanded=False):
        # Input fields
        new_name = st.text_input('Name')
        new_url = st.text_input('Jira issue url')

        # Button to add new row to csv
        if st.button('Create'):
            # Add new data row
            new_data = {
                'Name': new_name,
                'Jira issue': new_url
            }
            csv_add_row(csv_files['projects'], new_data)
            st.success('New project created')
        
    # TODO Button to delete or hide selected project
    st.button('Archive project')
    