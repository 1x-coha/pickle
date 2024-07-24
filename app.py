import streamlit as st
import pandas as pd
import numpy as np
from dataclasses import dataclass

# Data sources
data_dir = 'data/'
projects = data_dir + 'projects.csv'
logs = data_dir + 'logs.csv'

@dataclass
class Skill:
    Name: str
    Date: str
    Models: str 
    Libraries: str 

@dataclass
class Library:
    Name: str
    Date: str
    Skills: str

@dataclass
class Log:
    Name: str
    Date: str
    File: str
    Captions: int
    Featurized: int

# Sidebar
with st.sidebar:
    'Hello USER!'
    with (st.expander('My settings')):
        'Settings'
    'Some more stuff'

# App title
st.title('Pickle :cucumber:')

# Library selection
st.selectbox('Select a skill library',['My library'])

# Tabs
tab_1, tab_2, tab_3 = st.tabs(['Logs', 'Training', 'Testing'])

# Logs tab
with tab_1:
    logs_data = pd.read_csv(logs)
    st.dataframe(logs_data)
