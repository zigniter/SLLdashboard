
from cachetools import TTLCache
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np
#sys.path.insert(1, "C:/past/your/coppied/path/here/streamlit_option_menu")

from streamlit_option_menu import option_menu
import time
# Folders I created and importing the python files in those folders
# the way libraries imported
import shared.charts as ch
import records.ld as ldd
import records.nicu as nc
import records.kmc as kc
import records.followup as fup
from file_uploader import fileUploader as fu
import reports as rd




st.set_page_config(page_title="Dashboard", page_icon="chart_with_upwards_trend", layout="wide")

theme_plotly = None  # None or Streamlit


# Style
with open('css/style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- READ Files ----


@st.cache(allow_output_mutation=True)

def get_data_from_csv(dataset):
    df = pd.read_csv(dataset)
    return df

@st.cache_data
def get_data_from_excel(dataset):
    df = pd.read_excel(dataset)
    return df


dfldAll = get_data_from_excel("data/server/LD.xlsx")
dfnicuAll = get_data_from_excel("data/server/NICU.xlsx")
dfkmcAll = get_data_from_excel("data/server/KMC.xlsx")
dffollowAll = get_data_from_excel("data/server/followup.xlsx")

def regionalData(region, facility):
    # Sort the dataframe by facility name
    dfld = dfldAll[dfldAll['Region_faci']==region].sort_values(by=facility)
    dfnicu = dfnicuAll[dfnicuAll['Region_faci'] == region].sort_values(by=facility)
    dfkmc = dfkmcAll[dfkmcAll['Region_faci'] == region].sort_values(by=facility)
    dffollow = dffollowAll[dffollowAll['Region_faci'] == region].sort_values(by=facility)
    return dfld, dfnicu, dfkmc, dffollow

def switch(regionf):
    if regionf=='Amhara':
        facilityR = 'Facility_id1'
    elif regionf=='Oromia':
        facilityR = 'Facility_id2'
    elif regionf=='Sidama' or regionf=='SNNP' or regionf=='South West':
        facilityR = 'Facility_id3'
    elif regionf=='Tigray':
        facilityR = 'Facility_id4'
    return facilityR
# Reasons for transfer to the NICU

# Signs and Symptoms

# side bar
st.sidebar.image("image/sll_croped.jpg")


def sideBar():

    # ---- SIDEBAR ----
    checkUpload = st.sidebar.checkbox("Upload CSV File")
    # Select type of Report
    checkreport = st.sidebar.checkbox("Generate Report")

    # Select Region
    region = np.array([ 'Tigray','Amhara', 'Oromia', 'Sidama', 'SNNP', 'South West'])
    selectR = st.sidebar.selectbox('Select Region', region)
    #st.write("String 1:", selectR)
    st.header('_Dashboard_ for :blue[region]: '+selectR)

    # Select Facility
    
    facilityR = switch(selectR)

    dfld, dfnicu, dfkmc, dffollow = regionalData(selectR, facilityR)

    # DataFrames for the variables to make agreggagetd values
    dfalive = dfld[dfld['death_live'] == 'Alive']
    dfaliveAll = dfldAll[dfldAll['death_live'] == 'Alive']


    if checkUpload:
        fu()
    elif checkreport:
        # Select type of Report
        report = np.array(['Select', 'Summary', 'Phase', 'Recorded', 'KPIs'])
        selectReport = st.sidebar.selectbox('Select Report', report)

        if selectReport == 'Summary':
            rd.displaySummary(dfldAll, dfnicuAll, dfkmcAll, dffollowAll, selectR, facilityR)
        if selectReport == 'Recorded':
            rd.displayRecorded(dfld, dfnicu, dfkmc, dffollow, selectR, facilityR)
        if selectReport == 'Phase':
            rd.dispPhases(dfldAll, selectR, facilityR)
        if selectReport == 'KPIs':
            rd.displayKPIs(dfaliveAll, dfnicuAll, selectR, facilityR)
    else:
        
        # Select Facility
        checkfacility = st.sidebar.checkbox(
            "Show Analysis by Facility", False, key=1)
        select = st.sidebar.selectbox(
            'Select a Facility', pd.unique(dfalive[facilityR]))
        facility_data = dfalive[dfalive[facilityR] == select]
        # File uploader at sidebar
        # Horizontal menu

        selected = option_menu(None, ["LD", "NICU", "KMC", 'Follow'],
                               menu_icon="cast", default_index=0, orientation="horizontal",
                               styles={
            "container": {"padding": "0!important", "background-color": "#oaoaoa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#777"},
            "nav-link-selected": {"background-color": "#ff488b"},
        })

        
        if selected == 'LD':
            ldd.pages(select, selectR, facilityR, checkfacility, dfalive)
        elif selected == 'NICU':
            nc.pages(select, selectR, facilityR, checkfacility, dfnicu)
        elif selected == 'KMC':
            kc.pages(select,selectR, facilityR, checkfacility, dfkmc)
        elif selected == 'Follow':
            fup.pages(select, selectR, facilityR, checkfacility, dffollow)

# Starting point
sideBar()


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
