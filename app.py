import streamlit as st
import pandas as pd
import numpy as np
from dataclasses import dataclass
from enum import Enum


# Data sources
data_dir = 'data/'
projects = data_dir + 'projects.csv'

@dataclass
class Skill:
    Uid: str
    Name: str
    Libraries: dict
    Created: str
    Models: str

@dataclass
class Library:
    Uid: str
    Name: str
    Skills: dict

@dataclass
class Log:
    Uid: str
    Name: str
    FileName: str
    Captions: int
    FeaturizedFrames: int
    Created: str

class SkillType(Enum):
    GENERAL = 'General Skill'
    UNIQUE = 'Unique Skill'
    RECOVERY = 'Recovery Skill'


with st.sidebar:
    'Hello USER!'
    with (st.expander('My settings')):
        'Settings'
    ''
    'Here are some links to other tools:'
    'Aiviz'
    'Air Fryer'
    'FastCaption'


# App title
st.title('Pickle :cucumber:')


# Library selection
st.selectbox('Select a skill library',['My library'])


# Skills dashboard
skills = [
    Skill(Uid: 'SKI-1', Name: 'Skill 1', Libraries: 'My Library', '', ''),
    Skill(Uid: 'SKI-2', Name: 'Skill 2', Libraries: 'My Library', '', '')
]

for skill in skills:
    st.write()