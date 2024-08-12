import streamlit as st
import pandas as pd
import numpy as np
import json
import datetime
import pytz
from graphviz import Digraph

# Sidebar
with st.sidebar:
    'Hello USER! 🤡'
    with st.expander('My settings'):
        'Settings'
    'Some more stuff'

# Data sources

logs_file_path = 'data/logs.csv'

# App title
st.title('Pickle 🥒')

# Tabs
tab_1, tab_2 = st.tabs(['🔧Skills', '🪵Logs'])

# Skills tab
with tab_1:
    # Load csv file and convert to dictionary
    skills_csv_path = 'data/skills.csv'
    df = pd.read_csv(skills_csv_path)
    nodes = {row['id']: row for _, row in df.iterrows()}
    
    # Skill tree section
    with st.container(border=True):
        '### 🌳Skill tree'

        # Function to determine the style based on priority
        def get_node_style(priority):
            if priority == 'high':
                return {
                    'shape': 'box', 
                    'color': 'blue', 
                    'style': 'solid,bold', 
                    'fontcolor': 'white'}
            elif priority == 'mid':
                return {
                    'shape': 'box', 
                    'color': 'green', 
                    'style': 'dashed', 
                    'fontcolor': 'white'}
            else:  # low priority
                return {
                    'shape': 'box', 
                    'color': 'gray', 
                    'style': 'dotted', 
                    'fontcolor': 'white'}

        # Recursive function to add nodes and edges
        def add_nodes_edges(dot, parent_id):
            for node_id, node_data in nodes.items():
                if pd.isna(node_data['parent']) and parent_id is None:
                    # Handle root nodes (where parent is None)
                    label = f'{node_data["name"]}'
                    style = get_node_style(node_data['priority'])
                    dot.node(str(node_id), label=label, **style)
                    add_nodes_edges(dot, node_id)
                elif node_data['parent'] == parent_id:
                    # Handle child nodes
                    label = f'{node_data["name"]}'
                    style = get_node_style(node_data['priority'])
                    dot.node(str(node_id), label=label, **style)
                    dot.edge(str(parent_id), str(node_id), dir='back', color='white')
                    add_nodes_edges(dot, node_id)

        # Create the graph
        dot = Digraph(comment='Skill Tree')
        dot.attr(bgcolor='#0E1117')

        # Add nodes and edges starting from the root nodes (where parent is NaN or empty)
        add_nodes_edges(dot, None)

        # Render the graph
        st.graphviz_chart(dot)
    
    # Skill editor section
    with st.container(border=True):
        '### ⚒️Skill editor'

        # Create a mapping from name to id
        name_to_id = {f"{row['name']}": row['id'] for _, row in df.iterrows()}

        # Display the names in a selectbox
        selected_name = st.selectbox('Select a Skill to Edit', list(name_to_id.keys()))

        # Retrieve the corresponding node
        selected_id = name_to_id[selected_name]
        selected_node = nodes[selected_id]

        # Display the selected node details (for demonstration)
        st.write(f":gray[Skill ID:] {selected_id}")
        st.write(f":gray[Name:] {selected_node['name']}")
        st.write(f":gray[Description:] {selected_node['description']}")
        st.write(f":gray[Current Parent ID:] {selected_node['parent']}")

        # Selectbox to choose a new parent
        # Add an option for "No Parent" which means the skill becomes a root node
        parent_options = ["No Parent"] + [f"{row['id']}: {row['name']}" for _, row in df.iterrows() if row['id'] != selected_id]
        new_parent = st.selectbox("Select New Parent", parent_options)

        # Button to update the parent
        if st.button("Update Parent"):
            if new_parent == "No Parent":
                nodes[selected_id]['parent'] = None
            else:
                new_parent_id = int(new_parent.split(":")[0])
                nodes[selected_id]['parent'] = new_parent_id

            # Update the DataFrame with the new parent
            df.loc[df['id'] == selected_id, 'parent'] = nodes[selected_id]['parent']

            # Save the updated DataFrame to the CSV file
            df.to_csv(skills_csv_path, index=False)

            st.success(f"Parent updated to {new_parent}")

        # Optionally display the updated DataFrame or skill details
        st.write("Updated Skill Details:")
        st.write(f"Name: {selected_node['name']}")
        st.write(f"Description: {selected_node['description']}")
        st.write(f"New Parent ID: {nodes[selected_id]['parent']}")

        # Optional: Popover form to create a new skill
        st.popover('Create new skill')

    # Policies section
    with st.container(border=True):
        '### 🚀Policies'

# Logs tab
with tab_2:
    # pytz Time zones
    time_zones = {
        'Sunnyvale (PST)': pytz.timezone('America/Los_Angeles'),
        'Moss (CET)': pytz.timezone('Europe/Oslo')
    }

    # Placeholder for ailog files from directory
    log_files = [
        'ailog_E2-033_2024_07_22-18_33_13',
        'ailog_E2-033_2024_07_22-19_00_00',
        'ailog_E2-001_2024_07_22-20_00_00',
        'ailog_E2-045_2024_07_23-01_00_00',
        'ailog_E2-033_2024_07_24-05_00_00'
        ]
    
    # Time zone selector
    selected_time_zone = st.selectbox(
        'Select a time zone',
        time_zones,
        index=0
        )

    # Format file names into df
    logs_data = []
    for log in log_files:
        # Combine Date and Time into a single datetime object
        date_str = log[13:23].replace('_', '-')
        time_str = log[24:32].replace('_', ':')
        
        # Assume the datetime in the log is in UTC
        datetime_combined = pd.to_datetime(f"{date_str} {time_str}", utc=True)
        
        # Convert from UTC to PST and then remove the timezone information
        datetime_converted = datetime_combined.tz_convert(time_zones[selected_time_zone]).tz_localize(None)

        # Make row dict and append
        row = {
            'File': log,
            'Robot': log[6:12],
            'Datetime': datetime_converted  # Combined datetime in PST
            }
        logs_data.append(row)

    #Make pandas DataFrame
    df = pd.DataFrame(logs_data)

    # Display DataFrame in Streamlit
    st.dataframe(df)