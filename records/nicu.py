
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
from streamlit_option_menu import option_menu
import shared.charts as ch
import altair as alt

def pages(selectf, selectr, facilitr, checkf, dfnicu):

 

    if checkf:

        st.markdown("## Facility level analysis at" + " %s" % (selectf))

        dfnicufaci = dfnicu[dfnicu["Facility_id4"] == "%s" % (selectf)]

        with st.expander("SLL CSV WorkBook"):
            showData = st.multiselect('Filter: ', dfnicufaci.columns, default=[
                                      "Facility_id4", "q132skin_skin", "bweight2","dur_day_night_m"])
            st.dataframe(dfnicufaci[showData], use_container_width=True)

        # st.markdown("### Overall Weights in %s" % (select))
        totalweightr = ch.get_weight_facility('bweight2', dfnicu, selectf)

        # st.markdown("### Overall Breast Feeding in %s" % (select))
        #totalbreastf = ch.breast_feed_f("q124breastf", dfnicu, selectf)

        dfunderweightsksk = dfnicu[(dfnicu['q132skin_skin'] == "yes") & (
            dfnicu['bweight2'] < 2000) & (dfnicu['bweight2'] != 999) & (dfnicu['bweight2'] != 999.90002)]
       

        ch.draw_bar(totalweightr, "Overall Weights")

        #ch.draw_bar(totalbreastf, "Overall Breast Feeding")

      

    else:

        st.markdown("## Region level analysis")

        # Display the three phases
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            ch.cards(dfnicu[dfnicu['phase'] == 'Phase1']
                     ['phase'].count(), "<b>Phase One</b>")
        with middle_column:
            ch.cards(dfnicu[dfnicu['phase'] == 'Phase2']
                     ['phase'].count(), "<b>Phase Two</b>")
        with right_column:
            ch.cards(dfnicu[dfnicu['phase'] == 'Phase3']
                     ['phase'].count(), "<b>Phase Three</b>")
        st.markdown("""---""")

        # Trend - by Month
        trendbyM = pd.DataFrame({
            "Month": ['June', 'July', 'August', 'September', 'October', 'November'],
            "Count": [dfnicu[(dfnicu['today_rec'] >= '2023-06-01') & (dfnicu['today_rec'] <= '2023-06-30')]['today_rec'].count(),
                      dfnicu[(dfnicu['today_rec'] >= '2023-07-01') & (dfnicu['today_rec'] <= '2023-07-31')]['today_rec'].count(),
                      dfnicu[(dfnicu['today_rec'] >= '2023-08-01') & (dfnicu['today_rec'] <= '2023-08-31')]['today_rec'].count(),
                      dfnicu[(dfnicu['today_rec'] >= '2023-09-01') & (dfnicu['today_rec'] <= '2023-09-30')]['today_rec'].count(),
                      dfnicu[(dfnicu['today_rec'] >= '2023-10-01') & (dfnicu['today_rec'] <= '2023-10-31')]['today_rec'].count(),
                      dfnicu[(dfnicu['today_rec'] >= '2023-11-01') & (dfnicu['today_rec'] <= '2023-11-30')]['today_rec'].count()]

        })
        ch.draw_bar(trendbyM, "NICU Monthly Data")
        # Alive Neonates

        # Neonates addmited to NICU

        countNeonates = []
        for faci in dfnicu[facilitr].unique():
            countNeonates.append(ch.count_facility(dfnicu, faci, facilitr))
    
        dfadmit = pd.DataFrame({
            'Facility': dfnicu[facilitr].unique(),
            # , ch.count_facility(dfnicu, "Hagerese PH"), ch.count_facility(dfnicu, "Adidaero PH"), ch.count_facility(dfnicu, "Wukromar PH"), ch.count_facility(dfnicu, "Seleklek PH"))
            'Number of Neonates': countNeonates
        })
        # Weight Category
        weight_cat = ch.weght_category('bweight2', dfnicu)

        # New Admission vs Readmission
        dfweight = pd.DataFrame({
            'Admission': dfnicu['adm_stat'].unique(),
            'Number of Neonates': (dfnicu[dfnicu['adm_stat'] == "New admission"]['adm_stat'].count(), dfnicu[dfnicu['adm_stat'] == "Readmission"]['adm_stat'].count())
        })
      
        # Skin to Skin
        countsk2sk = []
        for faci in dfnicu[facilitr].unique():
            countsk2sk.append(ch.count_facility(dfnicu[dfnicu['q132skin_skin'] == 'yes'], faci, facilitr))
        dfsk = pd.DataFrame({
            'Facility': dfnicu[facilitr].unique(),
            'Number of Neonates': countsk2sk
        })
 
        #['dur_day_night_m']+dfnicu[dfnicu['dur_day_night_z'] != None]['dur_day_night_z']
        dfnicu['dur_day_night'] = dfnicu['dur_day_night_m'] + dfnicu['dur_day_night_z']
      
        dfdur = pd.DataFrame({
            'Hours': dfnicu[dfnicu['dur_day_night'].notnull()]['dur_day_night'],
            'Facility': dfnicu[dfnicu['dur_day_night'].notnull(
            )][facilitr]
        })

        # Draw the barcharts
        cl1, cl2 = st.columns(2)

        with cl1:
            ch.draw_bar(dfadmit, "<b>Neonates Admitted to NICU</b>")
        with cl2:
            ch.draw_bar(dfweight, "<b> New Admissioin vs Readmited Neonates</b>")

        cl3, cl4 = st.columns(2)

        with cl3:
            ch.draw_bar(weight_cat, "<b>Weight Category of Neonates addmitted to NICU</b>")
        with cl4:
            ch.draw_bar(dfsk, "<b>Neonates Received STS at NICU</b>")
       
        #st.write(dfnicu['dur_day_night'])
