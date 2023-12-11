
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
from streamlit_option_menu import option_menu
import shared.charts as ch


def pages(selectf, selectr, facilitr, checkf, dfalive):

    dfsksk = dfalive[dfalive["skin_skin1sthr"] == 'yes']
    #st.write(dfsksk[dfsksk[facilitr] == 'Adidaero PH'][facilitr].count())
    # What has the provider give to the Neonates
    dfresus = dfalive[dfalive['pro_resusc'] == 'yes']
    dfantib = dfalive[dfalive['pro_antibioNI'] == 'yes']
    dfcpap = dfalive[dfalive['pro_CPAP'] == 'yes']
    dfo2 = dfalive[dfalive['pro_O2respdis'] == 'yes']
    dfmgso4 = dfalive[dfalive['pro_MgSO4mt'] == 'yes']
    dfplastic = dfalive[dfalive['pro_wrapbyplastb1'] == 'yes']

    if checkf:

        st.markdown("## Facility level analysis at" + " %s" % (selectf))

        dfalivefaci = dfalive[dfalive[facilitr] == "%s" % (selectf)]

        with st.expander("⏰ SLL CSV WorkBook"):
            showData = st.multiselect('Filter: ', dfalivefaci.columns, default=[
                                      "Facility_id4", "skin_skin1sthr", "bb1bWr", "wks_gavebirthmthcg"])
            st.dataframe(dfalivefaci[showData], use_container_width=True)

        # st.markdown("### Overall Weights in %s" % (select))
        totalweightr = ch.get_weight_facility('bb1bWr',dfalive, selectf, facilitr)

        # st.markdown("### Overall Breast Feeding in %s" % (select))
        totalbreastf = ch.breast_feed_f("hrsaft_birthbreast", dfalive, selectf, facilitr)

        dfunderweightsksk = dfalive[(dfalive['skin_skin1sthr'] == "yes") & (
            dfalive['bb1bWr'] < 2000) & (dfalive['bb1bWr'] != 999) & (dfalive['bb1bWr'] != 999.90002)]
        dfgalst35sksk = dfalive[(dfalive['wks_gavebirthmthcg'] < 35) & ((dfalive['skin_skin1sthr'] == "yes"))][[
            facilitr, 'wks_gavebirthmthcg', 'skin_skin1sthr', 'bb1bWr']]

        ch.draw_bar(totalweightr, "Overall Weights")

        ch.draw_bar(totalbreastf, "Overall Breast Feeding")

        st.write("## Count total Number")
        ch.count_number_of(dfalive, dfsksk, dfresus,
                           dfantib, dfcpap, dfo2, dfmgso4, dfunderweightsksk, selectf, facilitr)

        st.write("## Important KPIs")

        ch.count_imporotant_KPIs(dfunderweightsksk, dfgalst35sksk, selectf, facilitr)

    else:

        st.markdown("## Region level analysis")
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            ch.cards(dfalive[dfalive['phase'] == 'Phase1']
                     ['phase'].count(), "<b>Phase One</b>")
        with middle_column:
            ch.cards(dfalive[dfalive['phase'] == 'Phase2']
                     ['phase'].count(), "<b>Phase Two</b>")
        with right_column:
            ch.cards(dfalive[dfalive['phase'] == 'Phase3']
                     ['phase'].count(), "<b>Phase Three</b>")
        st.markdown("""---""")

        # Trend - by Month
        trendbyM = pd.DataFrame({
            "Month": ['June', 'July', 'August', 'September', 'October', 'November'],
            "Count": [dfalive[(dfalive['today_rec'] >= '2023-06-01') & (dfalive['today_rec'] <= '2023-06-30')]['today_rec'].count(),
                      dfalive[(dfalive['today_rec'] >= '2023-07-01') & (dfalive['today_rec'] <= '2023-07-31')]['today_rec'].count(),
                      dfalive[(dfalive['today_rec'] >= '2023-08-01') & (dfalive['today_rec'] <= '2023-08-31')]['today_rec'].count(),
                      dfalive[(dfalive['today_rec'] >= '2023-09-01') & (dfalive['today_rec'] <= '2023-09-30')]['today_rec'].count(),
                      dfalive[(dfalive['today_rec'] >= '2023-10-01') & (dfalive['today_rec'] <= '2023-10-31')]['today_rec'].count(),
                      dfalive[(dfalive['today_rec'] >= '2023-11-01') & (dfalive['today_rec'] <= '2023-11-30')]['today_rec'].count()]
        
        })
        ch.draw_bar(trendbyM, "LD Monthly Data")
        # Alive Neonates
        countAlive = []
        for faci in dfalive[facilitr].unique():
            countAlive.append(ch.count_facility(dfalive, faci, facilitr))
        dfl = pd.DataFrame({
            'Facility': dfalive[facilitr].unique(),
            'Number of Neonates': countAlive
        })

        countsk2sk = []
      
        for faci in dfsksk[facilitr].unique():
            countsk2sk.append(ch.count_facility(dfsksk, faci, facilitr))
        # Skin to Skin
        dfsk = pd.DataFrame({
            'Facility': dfsksk[facilitr].unique(),
            'Number of Neonates': countsk2sk
        })

        # Reason for transfer NICU
        # Signs and Symptoms

       

        weght_cat = ch.weght_category('bb1bWr', dfalive)
        # draw_bar(weght_cat, "Number of Weight category")

        # Draw the barcharts
        cl1, cl2 = st.columns(2)
        with cl1:
            ch.draw_bar(dfl, "<b>Alive Neonates per Facility</b>")
        with cl2:
            ch.draw_bar(
            dfsk, "<b>Neonates kept skin to skin with mother with in the first hour after birth</b>")
        # draw_pie(dfsk, "<b>Babies kept skin to skin with mother with in the first hour after birth</b>")
        brst_fd = ch.breast_feed(dfalive)
        # draw_bar(brst_fd, "Breast Feeding category")

        # draw_2bars(dfl, "<b>Alive Neonates per Facility</b>", dfsk,
        #           "<b>Skin to Skin</b>")
        ch.draw_2pies(weght_cat, '<b>Weight Category</b>',
                      brst_fd, '<b>Breast Feeding</b>')