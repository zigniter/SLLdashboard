
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
from streamlit_option_menu import option_menu
import shared.charts as ch


def pages(selectf, selectr, facilitr, checkf, dfkmc):

    dfsksk = dfkmc[dfkmc["q147skin_skin"] == 'yes']
    

    if checkf:

        st.markdown("## Facility level analysis at" + " %s" % (selectf))

        dfkmcfaci = dfkmc[dfkmc[facilitr] == "%s" % (selectf)]

        with st.expander("⏰ SLL CSV WorkBook"):
            showData = st.multiselect('Filter: ', dfkmcfaci.columns, default=[
                                      "Facility_id4", "q147skin_skin", "bweight2"])
            st.dataframe(dfkmcfaci[showData], use_container_width=True)

        # st.markdown("### Overall Weights in %s" % (select))
        totalweightr = ch.get_weight_facility('bweight2',dfkmc, selectf)

        # st.markdown("### Overall Breast Feeding in %s" % (select))
        totalbreastf = ch.breast_feed_f("q141breastfkmc", dfkmc, selectf)

        dfunderweightsksk = dfkmc[(dfkmc['q147skin_skin'] == "yes") & (
            dfkmc['bweight2'] < 2000) & (dfkmc['bweight2'] != 999) & (dfkmc['bweight2'] != 999.90002)]
       # dfgalst35sksk = dfkmc[(dfkmc['wks_gavebirthmthcg'] < 35) & ((dfkmc['q147skin_skin'] == "yes"))][[
         #   'Facility_id4', 'wks_gavebirthmthcg', 'q147skin_skin', 'bweight2']]

        ch.draw_bar(totalweightr, "Overall Weights")

        #ch.draw_bar(totalbreastf, "Overall Breast Feeding")


    else:

        st.markdown("## Region level analysis")
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            ch.cards(dfkmc[dfkmc['phase'] == 'Phase1']
                     ['phase'].count(), "<b>Phase One</b>")
        with middle_column:
            ch.cards(dfkmc[dfkmc['phase'] == 'Phase2']
                     ['phase'].count(), "<b>Phase Two</b>")
        with right_column:
            ch.cards(dfkmc[dfkmc['phase'] == 'Phase3']
                     ['phase'].count(), "<b>Phase Three</b>")
        st.markdown("""---""")

       # Trend - by Month
        trendbyM = pd.DataFrame({
            "Month": ['June', 'July', 'August', 'September', 'October', 'November'],
            "Count": [dfkmc[(dfkmc['date_outcome'] >= '2023-06-01') & (dfkmc['date_outcome'] <= '2023-06-30')]['date_outcome'].count(),
                      dfkmc[(dfkmc['date_outcome'] >= '2023-07-01') & (dfkmc['date_outcome'] <= '2023-07-31')]['date_outcome'].count(),
                      dfkmc[(dfkmc['date_outcome'] >= '2023-08-01') & (dfkmc['date_outcome'] <= '2023-08-31')]['date_outcome'].count(),
                      dfkmc[(dfkmc['date_outcome'] >= '2023-09-01') & (dfkmc['date_outcome'] <= '2023-09-30')]['date_outcome'].count(),
                      dfkmc[(dfkmc['date_outcome'] >= '2023-10-01') & (dfkmc['date_outcome'] <= '2023-10-31')]['date_outcome'].count(),
                      dfkmc[(dfkmc['date_outcome'] >= '2023-11-01') & (dfkmc['date_outcome'] <= '2023-11-30')]['date_outcome'].count()]

        })
        ch.draw_bar(trendbyM, "KMC Monthly Data")

        # Alive Neonates
        countNeonates = []
        for faci in dfkmc[facilitr].unique():
            countNeonates.append(ch.count_facility(dfkmc, faci, facilitr))
        dfl = pd.DataFrame({
            'Facility': dfkmc[facilitr].unique(),
            'Number of Neonates': countNeonates
        })

        # Skin to Skin
        countsk2sk = []
      
        for faci in dfsksk[facilitr].unique():
            countsk2sk.append(ch.count_facility(dfsksk, faci, facilitr))
        dfsk = pd.DataFrame({
            'Facility': dfsksk[facilitr].unique(),
            'Number of Neonates': countsk2sk
        })

        # Reason for transfer NICU
        # Signs and Symptoms

       

        weght_cat = ch.weght_category('bweight2',dfkmc)
        # draw_bar(weght_cat, "Number of Weight category")

        # Draw the barcharts
        cl1, cl2 = st.columns(2)
        with cl1:
            ch.draw_bar(dfl, "<b>Alive Neonates per Facility</b>")
        with cl2:
            ch.draw_bar(
                dfsk, "<b>skin-to-skin care initiated at KMC unit</b>")
     
     
