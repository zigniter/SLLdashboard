from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np


def get_weight_facility(weight, dfw, select, facilitr):

    weightr1 = dfw[dfw[weight] > 2500]
    weightr2 = dfw[(dfw[weight] <= 2500) & (dfw[weight] >= 2000)]
   # weightr3 = dfw[dfw['bb1bwr'] == 2000]
    weightr3 = dfw[(dfw[weight] < 2000) & (
        dfw[weight] != 999) & (dfw[weight] != 999.90002)]

    #st.write(weightr3[weightr3['Facility_id4'] == "%s" % (select)]['pro_antibioni'])

    total_dataframe = pd.DataFrame({
        'Weights (grams)': ['>2500', '2000-2500', '<2000'],
        'Number of Neonates': (weightr1[weightr1[facilitr] == "%s" % (select)][facilitr].count(),
                               weightr2[weightr2[facilitr] == "%s" %
                                        (select)][facilitr].count(),
                               weightr3[weightr3[facilitr] == "%s" % (select)][facilitr].count())})
    return total_dataframe


def draw_2bars(df1, title1, dfsk, title2):
    fig = make_subplots(
        1, 2, specs=[[{'type': 'xy'}, {'type': 'xy'}]], subplot_titles=[title1, title2])

    fig.add_bar(x=df1[df1.columns.values[0]],
                y=df1[df1.columns.values[1]],
                color=df1.columns.values[0], row=1, col=1)
    fig.add_bar(x=dfsk[dfsk.columns.values[0]], y=dfsk[dfsk.columns.values[1]],
                color=df1.columns.values[0], row=1, col=2)
    fig.update_layout(title_text='Count')
    st.plotly_chart(fig)


def draw_2pies(weght_cat, title1, brst_fd, title2):
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=[title1, title2])
    fig.add_trace(go.Pie(labels=weght_cat[weght_cat.columns.values[0]], values=weght_cat[weght_cat.columns.values[1]], scalegroup='one',
                         name=title1), 1, 1)
    fig.add_trace(go.Pie(labels=brst_fd[brst_fd.columns.values[0]], values=brst_fd[brst_fd.columns.values[1]], scalegroup='one',
                         name=title2), 1, 2)
    st.plotly_chart(fig, use_container_width=True)


def draw_bar(total_dataframe, lable):
    state_total_graph = px.bar(
        total_dataframe,
        x=total_dataframe.columns.values[0],
        y=total_dataframe.columns.values[1],
        title=lable,
        color=total_dataframe.columns.values[0])
    st.plotly_chart(state_total_graph, use_container_width=True)


# def draw_pie(total_dataframe, lable):
 #   state_total_graph = px.pie(
  #      total_dataframe,
   # title=lable,
    #  color=total_dataframe.columns.values[0])
   # st.plotly_chart(state_total_graph)


def weght_category(weight,dfw):

    # four categories of weights

    weightr1 = dfw[dfw[weight] > 2500][weight]
    weightr2 = dfw[(dfw[weight] <= 2500) & (dfw[weight] >= 2000)][weight]
    # weightr3 = dfw[dfw['bb1bwr'] == 2000]['bb1bwr']
    weightr3 = dfw[(dfw[weight] < 2000) & (dfw[weight] != 999)
                   & (dfw[weight] != 999.90002)][weight]

    #st.write(dfw[(dfw['bb1bwr'] < 2000) & (dfw['bb1bwr']!=999) & (dfw['bb1bwr']!= 999.90002)]['death_live'])

    total_dataframe = pd.DataFrame({
        'Weights (grams)': ['>2500', '2000-2500', '<2000'],
        'Number of Neonates': (weightr1.count(), weightr2.count(), weightr3.count())})
    return total_dataframe


def breast_feed_f(breast, dfb, select, facilitr):
    # four categories of breast feeding hours
    dfbreast1 = dfb[dfb[breast]
                    == "<30 minutes"]
    dfbreast2 = dfb[dfb[breast]
                    == "30 minutes to < 1 hour"]
    dfbreast3 = dfb[dfb[breast]
                    == "1 hour to < 24 hours"]
    dfbreast4 = dfb[dfb[breast]
                    == "24+ hours"]

    total_dataframe = pd.DataFrame({
        'Feeding Time': ['<30 minutes', '30 minutes to < 1 hour', '1 hour to < 24 hours', '24+ hours'],
        'Number of Neonates': (dfbreast1[dfbreast1[facilitr] == "%s" % (select)][facilitr].count(), dfbreast2[dfbreast2[facilitr] == "%s" % (select)][facilitr].count(), dfbreast3[dfbreast3[facilitr] == "%s" % (select)][facilitr].count(), dfbreast4[dfbreast4[facilitr] == "%s" % (select)][facilitr].count())})
    return total_dataframe


def breast_feed(dfb):
    # four categories of breast feeding hours
    dfbreast1 = dfb[dfb["hrsaft_birthbreast"]
                    == "<30 minutes"]["hrsaft_birthbreast"]
    dfbreast2 = dfb[dfb["hrsaft_birthbreast"]
                    == "30 minutes to < 1 hour"]["hrsaft_birthbreast"]
    dfbreast3 = dfb[dfb["hrsaft_birthbreast"]
                    == "1 hour to < 24 hours"]["hrsaft_birthbreast"]
    dfbreast4 = dfb[dfb["hrsaft_birthbreast"]
                    == "24+ hours"]["hrsaft_birthbreast"]

    total_dataframe = pd.DataFrame({
        'Weights (grams)': ['<30 minutes', '30 minutes to < 1 hour', '1 hour to < 24 hours', '24+ hours'],
        'Number of Neonates': (dfbreast1.count(), dfbreast2.count(), dfbreast3.count(), dfbreast4.count())})
    return total_dataframe


def cards(i, sline):

    wch_colour_box = (0, 204, 102)
    wch_colour_font = (0, 0, 0)
    fontsize = 24
    valign = "center"
    iconname = "fas fa-calculator"

    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]},
		                                              {wch_colour_box[1]},
		                                              {wch_colour_box[2]}, 0.75);
		                        color: rgb({wch_colour_font[0]},
		                                   {wch_colour_font[1]},
		                                   {wch_colour_font[2]}, 0.75);
		                        font-size: {fontsize}px;
		                        border-radius: 7px;
		                        padding-left: 12px;
		                        padding-top: 18px;
		                        padding-bottom: 18px;
		                        line-height:25px;'>
		                        <i class='{iconname} fa-xs'></i> {i}
		                        </style><BR><span style='font-size: 14px;
		                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(lnk + htmlstr, unsafe_allow_html=True)


# --- MAINPAGE ---
#st.title(":bar_chart: SLL DATA VISUALISATION")


# top KPI's


def count_facility(dff,facility,facilitr):
    dff1 = dff[dff[facilitr] == facility]
    return dff1[facilitr].count()


def count_number_of(dflv, dfskin, dfres, dfanti, dfcp, dfo, dfmgs, dfplastic, select, facilitr):
    col3, col4, col5 = st.columns(3)
    col6, col7, col8 = st.columns(3)
    col9, col10, col11 = st.columns(3)

    with col3:
        cards(dflv[dflv[facilitr] == "%s" % (select)]
                  [facilitr].count(), "<b>Alive</b>")
    with col4:
        cards(dfskin[dfskin[facilitr] == "%s" % (select)]
              [facilitr].count(), "<b>Skin to Skin</b>")
    with col5:
        cards(dfres[dfres[facilitr] == "%s" %
                    (select)][facilitr].count(), "<b>Resuscitate</b>")
    with col6:
        cards(dfanti[dfanti[facilitr] == "%s" %
                     (select)][facilitr].count(), "<b>Antibiotics</b>")
    with col7:
        cards(dfcp[dfcp[facilitr] == "%s" %
                   (select)][facilitr].count(), "<b>CPAP</b>")
    with col8:
        cards(dfo[dfo[facilitr] == "%s" % (select)]
              [facilitr].count(), "<b>Oxygen</b>")

    with col9:
        cards(dfmgs[dfmgs[facilitr] == "%s" %
                    (select)][facilitr].count(), "<b>MGSO4</b>")
    with col10:
        cards(dfplastic[dfplastic[facilitr] == "%s" % (select)]
              [facilitr].count(), "<b>Plastic</b>")


def count_imporotant_KPIs(dfunderweightsksk, dfgalst35sksk, select, facilitr):
    col12, col13, col14 = st.columns(3)
    with col12:
        cards(dfunderweightsksk[dfunderweightsksk[facilitr] == "%s" % (select)]
              [facilitr].count(), "<b>Underweight - Skin to Skin <1 hr</b>")
    with col13:
        cards(dfgalst35sksk[dfgalst35sksk[facilitr] == "%s" % (select)]
              [facilitr].count(), "<b>GA <35w - Skin to Skin <1hr</b>")
