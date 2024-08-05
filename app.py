import streamlit as st
import pandas as pd
import numpy as np
import json

# Sidebar
with st.sidebar:
    'Hello USER!'
    with st.expander('My settings'):
        'Settings'
    'Some more stuff'

# Data sources
skills_file_path = 'data/skills.json'
logs_file_path = 'data/logs.csv'

# App title
st.title('Pickle :cucumber:')

# Tabs
tab_1, tab_2 = st.tabs([':books: Skills', ':wood: Logs'])

# Skills tab
with tab_1:
    # Load skills file and store data
    with open(skills_file_path, 'r') as file:
        skill_tree = json.load(file)

    # Skill Tree section
    st.header(':deciduous_tree: Skill Tree')
    with st.container(border=True, height=500):
        st.write(skill_tree)

    # Create a new skill TODO
    st.popover('Create new skill')

    # Skill section
    st.header(':wrench: Skill Editor')
    with st.container():
        
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
        
    if selected_skill:
        # Rename TODO
        with st.popover('Rename'):
            name_input = st.text_input('Enter a new name', placeholder=selected_skill)
            st.button(
                f'Rename to :orange[**{name_input}**]',
                disabled=name_input=='',
                )

        # Re-parent TODO
        with st.popover('Re-parent'):
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
        with st.popover('Delete'):
            ':red[Are you sure you want to delete this skill?]'
            st.button(f'Yes, delete :orange[**{selected_skill}**]')

    # Policies section
    st.header(':rocket: Policies')
    with st.container(border=True):
        ''

# Logs tab
with tab_2:
    col_1, col_2 = st.columns(2)

    with col_1:
        '#### Logs'
        with st.container(border=True, height=300):
            button = []
            for i in range(20):
                button.append(st.button(f"`Ailog_E2-123_12-34-56_12-34-56_{i}`"))
            
    with col_2:
        '#### Details'
        with st.container(border=True, height=300):
            f'**Ailog_E2-123_12-34-56_12-34-56_**'





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