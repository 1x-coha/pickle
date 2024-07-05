import streamlit as st
import pandas as pd
import numpy as np
from utils import csv_list, csv_add_row

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

    # Expander to display current csv contents
    with st.expander('Show projects table', expanded=False):
        df = pd.read_csv(csv_files['projects'])
        st.write(df)

    # Expander to add new project
    with st.expander('Create a new project', expanded=False):
        # Input fields
        new_name = st.text_input('Name')
        new_url = st.text_input('Jira issue url')
        new_libs = st.text_input('Skill libraries')

        # Button to add new row to csv
        if st.button('Create'):
            # Add new data row
            new_data = {
                'ID': '',
                'Name': new_name,
                'URL': new_url,
                'Libraries': ''
            }
            new_data = pd.DataFrame(new_data, index=[0])
            csv_add_row(csv_files['projects'], new_data, 'PRO-')
            st.success('New project created')
    
    # Select box to select project from list
    projects = csv_list(csv_files['projects'], ['ID','Name'])
    selected_project = st.selectbox('Selected project', projects)

    # TODO Button to delete or hide selected project
    st.button('Trash project')