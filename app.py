import streamlit as st
import pandas as pd
import numpy as np
import json
import datetime

# Sidebar
with st.sidebar:
    'Hello USER! 🤡'
    with st.expander('My settings'):
        'Settings'
    'Some more stuff'

# Data sources
skills_file_path = 'data/skills.json'
logs_file_path = 'data/logs.csv'

# App title
st.title('Pickle 🥒')

# Tabs
tab_1, tab_2 = st.tabs(['📚 Skills', '🪵 Logs'])

# Skills tab
with tab_1:
    with st.container():
        # Load skills file and store data
        with open(skills_file_path, 'r') as file:
            skill_tree = json.load(file)

        # Skill Tree section
        st.header('🌳 Skill Tree')
        with st.container(border=True, height=500):
            st.write(skill_tree)

        # Create a new skill TODO
        st.popover('Create new skill')

        # Function: Flatten dictionary
        def flatten_dict(d, parent_key='', sep=' > '):
            items = []
            for k, v in d.items():
                new_key = parent_key + sep + k if parent_key else k
                items.append(k)
                if isinstance(v, dict) and v:
                    items.extend(flatten_dict(v, new_key, sep=sep))
            return items
        
        # Flatten the skill tree and make a list
        flattened_skill_tree = flatten_dict(skill_tree)
        flattened_skill_tree = sorted(set(flattened_skill_tree))
        skill_list = flattened_skill_tree

        # Skill selector
        selected_skill = st.selectbox(
            'Which skill would you like to edit?', 
            skill_list,
            index=None,
            placeholder='Choose a skill'
            )
        
    # Rename TODO
    with st.popover('Rename', disabled=selected_skill==None):
        selected_skill
        name_input = st.text_input('Enter a new name', placeholder=selected_skill)
        st.button(
            f'Rename to :orange[**{name_input}**]',
            disabled=name_input=='',
            )

    # Re-parent TODO
    with st.popover('Re-parent', disabled=selected_skill==None):
        skill_list_filtered = [skill for skill in flattened_skill_tree if skill != selected_skill]
        selected_parent_skill = st.selectbox(
            'Select a new parent',
            skill_list_filtered,
            index=None,
            placeholder='Current parent skill???'
            )
        st.button(
            f'Re-parent under :orange[**{selected_parent_skill}**]',
            disabled=selected_parent_skill==None
            )
        
    # Delete TODO
    with st.popover('Delete', disabled=selected_skill==None):
        ':red[Are you sure you want to delete this skill?]'
        st.button(f'Yes, delete :orange[**{selected_skill}**]')

    # Policies section
    st.header('🚀 Policies')
    with st.container(border=True):
        ''

# Logs tab
with tab_2:
    # Placeholder for ailog files from directory
    log_files = [
        'ailog_E2-033_2024_07_22-18_33_13',
        'ailog_E2-033_2024_07_22-19_00_00',
        'ailog_E2-001_2024_07_22-20_00_00',
        'ailog_E2-045_2024_07_23-01_00_00',
        'ailog_E2-033_2024_07_24-05_00_00'
        ]
    
    # Format file names into df
    logs_data = []
    for log in log_files:
        row = {
            'File': log,
            'Robot': log[6:12],
            'Date': pd.to_datetime(log[13:23].replace('_', '-')),
            'Time': pd.to_datetime(log[24:32].replace('_', ':'))
        }
        logs_data.append(row)
    df = pd.DataFrame(logs_data)
    df_configured = st.dataframe(
        logs_data, 
        column_config={
            'Date': st.column_config.DateColumn(),
            'Time': st.column_config.TimeColumn()
            }
        )

    # Column visibility selection
    visible_columns = st.multiselect(
        'Select columns to show',
        options=df.columns,
        default=['Robot', 'Date', 'Time']
    )
    
    # Write logs dataframe
    st.data_editor(
        df_configured,
        disabled=['File', 'Robot', 'Date', 'Time']
        )

    # Logs table
    if 'logs_data' not in st.session_state:
        st.session_state.logs_data = logs_data

    event = st.dataframe(
        st.session_state.logs_data[visible_columns], 
        key='data',
        on_select='rerun',
        selection_mode='multi-row'
        )
    
    st.write(event)




if False:
    '# ---Old stuff for code reference---'

    # Tabs
    tab_1, tab_2, tab_3, tab_4 = st.tabs(['Log Collection', 'Model Training', 'Policy Testing', 'Data Editor'])

    # Logs tab
    with tab_1:
        logs_data = pd.read_csv(logs)
        st.dataframe(logs_data)

    # Data table editor tab
    with tab_4:
        editor_selection = st.selectbox('Select a table to edit', 
                ['Projects', 
                'Skill libraries',
                'Skills',
                '',
                'Logs',
                'Robots'])

        if(editor_selection == 'Projects'):
            pass
        elif(editor_selection == 'Skill Libraries'):
            pass
        elif(editor_selection == 'Logs'):
            st.data_editor(logs_data)
        elif(editor_selection == 'Models'):
            pass
        elif(editor_selection == 'Base models'):
            pass
        elif(editor_selection == 'Robots'):
            pass
        elif(editor_selection == 'Skills'):
            pass

    # Log Collection section
    '## Logs'
    st.multiselect('Select logs',[
        'Log 1',
        'Log 2',
        'Log 3'
        ])

    # Model Training section
    '## Model'
    st.selectbox('Select a base model',[
        'Wander',
        'Anytask'
        ])