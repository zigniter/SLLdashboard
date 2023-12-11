
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
from streamlit_option_menu import option_menu
import shared.charts as ch


def pages(selectf, selectr, facilitr, checkf, dffollow):

    dffollowAlive = dffollow[(dffollow['outcome_28'] == "Alive")|(dffollow['outcome_28'] == "Sick at the interview time")]
    dflbw = dffollow[(dffollow['bweight2']<=2500)&(dffollow['bweight2']!=999.9)&(dffollow['bweight2']!=0)]
    dfsksk_c = dffollow[dffollow["ssc_c"] == "yes"]
    dfsksk_l24 = dffollow[dffollow["ssc_l24"] == "yes"]



    if checkf:

        st.markdown("## Facility level analysis at" + " %s" % (selectf))

        dffollowfaci = dffollow[dffollow[facilitr] == "%s" % (selectf)]

        with st.expander("⏰ SLL CSV WorkBook"):
            showData = st.multiselect('Filter: ', dffollowfaci.columns, default=[
                                      "Facility_id4", "ssc_c", "ssc_l24","bweight2"])
            st.dataframe(dffollowfaci[showData], use_container_width=True)

        # st.markdown("### Overall Weights in %s" % (select))
        totalweightr = ch.get_weight_facility('bweight2', dffollow, selectf,facilitr)

        # st.markdown("### Overall Breast Feeding in %s" % (select))
        totalbreastf = ch.breast_feed_f("br_milkf", dffollow, selectf, facilitr)

        dfunderweightsksk = dffollow[(dffollow['ssc_c'] == '1') & (
            dffollow['bweight2'] < 2000) & (dffollow['bweight2'] != 999) & (dffollow['bweight2'] != 999.90002)]
       # dfgalst35sksk = dffollow[(dffollow['wks_gavebirthmthcg'] < 35) & ((dffollow['q147skin_skin'] == "yes"))][[
        #   'Facility_id4', 'wks_gavebirthmthcg', 'q147skin_skin', 'bweight2']]

        ch.draw_bar(totalweightr, "Overall Weights")

        #ch.draw_bar(totalbreastf, "Overall Breast Feeding")


    else:

        st.markdown("## Region level analysis")
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            ch.cards(dffollow[dffollow['phase'] == 'Phase1']
                     ['phase'].count(), "<b>Phase One</b>")
        with middle_column:
            ch.cards(dffollow[dffollow['phase'] == 'Phase2']
                     ['phase'].count(), "<b>Phase Two</b>")
        with right_column:
            ch.cards(dffollow[dffollow['phase'] == 'Phase3']
                     ['phase'].count(), "<b>Phase Three</b>")
        st.markdown("""---""")

       # Trend - by Month
        trendbyM = pd.DataFrame({
            "Month": ['June', 'July', 'August', 'September', 'October', 'November'],
            "Count": [dffollow[(dffollow['today_f'] >= '2023-06-01') & (dffollow['today_f'] <= '2023-06-30')]['today_f'].count(),
                      dffollow[(dffollow['today_f'] >= '2023-07-01') & (dffollow['today_f'] <= '2023-07-31')]['today_f'].count(),
                      dffollow[(dffollow['today_f'] >= '2023-08-01') & (dffollow['today_f'] <= '2023-08-31')]['today_f'].count(),
                      dffollow[(dffollow['today_f'] >= '2023-09-01') & (dffollow['today_f'] <= '2023-09-30')]['today_f'].count(),
                      dffollow[(dffollow['today_f'] >= '2023-10-01') & (dffollow['today_f'] <= '2023-10-31')]['today_f'].count(),
                      dffollow[(dffollow['today_f'] >= '2023-11-01') & (dffollow['today_f'] <= '2023-11-30')]['today_f'].count()]

        })
        ch.draw_bar(trendbyM, "NICU Monthly Data")

        # Delete null values
        dffollow[facilitr] = dffollow[dffollow[facilitr].notnull()][facilitr]
       
        # Total Follow up
        countNeonates = []
        for faci in dffollow[facilitr].unique():
            countNeonates.append(ch.count_facility(dffollow, faci, facilitr))
        dffu = pd.DataFrame({
            'Facility': dffollow[facilitr].unique(),
            'Number of Neonates': countNeonates
        })
        
        # Alive Neonates 
        countAlived = []
        for faci in dffollow[facilitr].unique():
            countAlived.append(ch.count_facility(dffollow, faci, facilitr))
        dfl = pd.DataFrame({
            'Facility': dffollow[facilitr].unique(),
            'Number of Neonates': countAlived
        })

        # Skin to Skin
        countsk2sk = []
      
        for faci in dfsksk_c[facilitr].unique():
            countsk2sk.append(ch.count_facility(dfsksk_c, faci, facilitr))
        dfsk = pd.DataFrame({
            'Facility': dfsksk_c[facilitr].unique(),
            'Number of Neonates': countsk2sk
        })
       
        # Low birth Weight
        countsklbw = []
      
        for faci in dflbw[facilitr].unique():
            countsklbw.append(ch.count_facility(dflbw, faci, facilitr))
        dflbw = pd.DataFrame({
            'Facility': dflbw[facilitr].unique(),
            'Number of Neonates': countsklbw
        })


        # Reason for transfer NICU
        # Signs and Symptoms

        weght_cat = ch.weght_category('bweight2', dffollow)
        # draw_bar(weght_cat, "Number of Weight category")

        # Draw the barcharts
        cl1, cl2 =st.columns(2)
        with cl1:
            ch.draw_bar(dffu, "<b>Total Follow-up per Facility</b>")
        with cl2:
            ch.draw_bar(
                dfsk, "<b>Skin to skin care after discharge</b>")
    
        cl3, cl4 =st.columns(2)
        with cl3:
            ch.draw_bar(dfl, "<b>Total Alive Babies</b>")
        with cl4:
            ch.draw_bar(
                dflbw, "<b>Low Birth Weight</b>")
