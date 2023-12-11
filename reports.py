import numpy as np
import pandas as pd
import streamlit as st
import datetime



#dfld = pd.read_csv("data\\ld_dataset_050723.csv")
#dfnicu = pd.read_csv("data\\nicu_dataset_300623.csv")

def displaySummary(dfldAll, dfnicuAll, dfkmcAll, dffollowAll, region, facilityR):


    dfld = dfldAll[dfldAll['Region_faci']==region].sort_values(by= facilityR)
    dfnicu = dfnicuAll[dfnicuAll['Region_faci'] == region].sort_values(by=facilityR)
    dfkmc = dfkmcAll[dfkmcAll['Region_faci'] == region].sort_values(by=facilityR)
    dffollow = dffollowAll[dffollowAll['Region_faci'] ==
                        region].sort_values(by=facilityR)

    st.write("Summary Data Generated from Tigray")
    summary = pd.DataFrame({
        'Form': ('LD', 'NICU', 'KMC', 'Followup'),
        'ERA': (dfld[dfld['death_live'] == 'Alive']['_index'].count(), dfnicu['_index'].count(), dfkmc['_index'].count(), dffollow['_index'].count()),
        '% National': (dfld[dfld['death_live'] == 'Alive']['_index'].count()/dfldAll[dfldAll['death_live'] == 'Alive']['_index'].count()*100, dfnicu['_index'].count()/dfnicuAll['_index'].count()*100, dfkmc['_index'].count()/dfkmcAll['_index'].count()*100, dffollow['_index'].count()/dffollowAll['_index'].count()*100)
    })

    st.write(summary)

def recordAll(df):
   
    rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for facility in df['Facility_id4'].unique():
        for fct in df['Facility_id4']:
          #  datea = df['datetime_first_opened']
           # st.header('_Dashboard_ for :blue[region]: '+datea)
           # dateb = datetime.datetime.strptime(datea, "%Y-%m-%d")
            if (dateb == 7):
                if (fct == 'Adidaero PH') & (facility == 'Adidaero PH'):
                    rec1 += 1
                if (fct == 'Adigudom PH') & (facility == 'Adigudom PH'):
                    rec2 += 1
                if (fct == 'Adishehu PH') & (facility == 'Adishehu PH'):
                    rec3 += 1
                if (fct == 'Edaga-ar PH') & (facility == 'Edaga-ar PH'):
                    rec4 += 1
                if (fct == 'Hagerese PH') & (facility == 'Hagerese PH'):
                    rec5 += 1
                if (fct == 'Mekoni PH') & (facility == 'Mekoni PH'):
                    rec6 += 1
                if (fct == 'Mulu Asefa PH') & (facility == 'Mulu Asefa PH'):
                    rec7 += 1
                if (fct == 'Seleklek PH') & (facility == 'Seleklek PH'):
                    rec8 += 1
                if (fct == 'Wukromar PH') & (facility == 'Wukromar PH'):
                    rec9 += 1
                
    dfldrec = [rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9]
        
    return dfldrec
# Requires modification for better efficiency 
def recordKPIs(dfout, dfin):
    
    rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for facility in dfout['Facility_id4'].unique():
        for fct in dfin:
            if (fct == 'Adidaero PH') & (facility == 'Adidaero PH'):
                rec1 += 1
            if (fct == 'Adigudom PH') & (facility == 'Adigudom PH'):
                rec2 += 1
            if (fct == 'Adishehu PH') & (facility == 'Adishehu PH'):
                rec3 += 1
            if (fct == 'Edaga-ar PH') & (facility == 'Edaga-ar PH'):
                rec4 += 1
            if (fct == 'Hagerese PH') & (facility == 'Hagerese PH'):
                rec5 += 1
            if (fct == 'Mekoni PH') & (facility == 'Mekoni PH'):
                rec6 += 1
            if (fct == 'Mulu Asefa PH') & (facility == 'Mulu Asefa PH'):
                rec7 += 1
            if (fct == 'Seleklek PH') & (facility == 'Seleklek PH'):
                rec8 += 1
            if (fct == 'Wukromar PH') & (facility == 'Wukromar PH'):
                rec9 += 1
    dfldrec = [rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9]
    return dfldrec

def displayRecorded(dfld, dfnicu, dfkmc, dffollow, region, facilityR):
    st.write("Data recorded in Tigray")
    dfldalive = dfld[dfld['death_live']=='Alive']
    
    recld = recordAll(dfldalive)
    recnicu = recordAll(dfnicu)
    rekmc = recordAll(dfkmc)
    refollowup = recordAll(dffollow)
    # delete the null value
    dffacil = dfld[dfld[facilityR].notnull()][facilityR]
  

    Recorded = pd.DataFrame({
        'Hospitals': dffacil.unique(),
        ('LD', 'Rec'): recld,
        ('LD', 'Expe(%)'): ('', '', '', '', '', '', '', '', ''),
        ('NICU', 'Rec'): recnicu,
        ('NICU', 'Expe(%)'): ('', '', '', '', '', '', '', '', ''),
        ('KMC', 'Rec'): rekmc,
        ('KMC', 'Expe(%)'): ('', '', '', '', '', '', '', '', ''),
        ('Follo Up', 'Rec'): refollowup,
        ('Follo Up', 'Expe(%)'): ('', '', '', '', '', '', '', '', '')
    })
    Recorded = Recorded.sort_values(by=[('LD', 'Rdfldec')])

    st.write(Recorded)

def dispPhases(dfldAll, region, facilityR):
    dfld = dfldAll[dfldAll['Region_faci'] ==
                   region].sort_values(by=facilityR)
    dfldAllPh1 = dfldAll[dfldAll['phase'] == 'Phase1']
    dfldAllPh2 = dfldAll[dfldAll['phase'] == 'Phase2']
    dfldAllPh3 = dfldAll[dfldAll['phase'] == 'Phase3']

    st.write("Skin to Skin and Breast Feeding by Phase")
    pahses = pd.DataFrame({
        'Form': ('Phase 1', 'Phase 2', 'Phase 3'),
        'STSimm LD': (dfldAllPh1[dfldAllPh1['pro_bymthch'] == 'yes']['pro_bymthch'].count(),
        dfldAllPh2[dfldAllPh2['pro_bymthch'] == 'yes']['pro_bymthch'].count(),
            dfldAllPh3[dfldAllPh3['pro_bymthch'] == 'yes']['pro_bymthch'].count()),
        'STSimm Rep': (dfldAllPh1[(dfldAllPh1['pro_bymthch'] == 'yes') & (dfldAllPh1['Region_faci'] ==
                                                                          region)]['pro_bymthch'].count(),
                       dfldAllPh2[(dfldAllPh2['pro_bymthch'] == 'yes') & (dfldAllPh2['Region_faci'] ==
                                                                          region)]['pro_bymthch'].count(),
                       dfldAllPh3[(dfldAllPh3['pro_bymthch'] == 'yes') & (dfldAllPh3['Region_faci'] ==
                                                                          region)]['pro_bymthch'].count()),
        'P2(%)': ((dfldAllPh1[(dfldAllPh1['pro_bymthch'] == 'yes') & (dfldAllPh1['Region_faci'] ==
                                                                          region)]['pro_bymthch'].count()/dfldAllPh1[dfldAllPh1['pro_bymthch'] == 'yes']['pro_bymthch'].count())*100,
                       (dfldAllPh2[(dfldAllPh2['pro_bymthch'] == 'yes') & (dfldAllPh2['Region_faci'] ==
                                                                          region)]['pro_bymthch'].count()/dfldAllPh2[dfldAllPh2['pro_bymthch'] == 'yes']['pro_bymthch'].count())*100,
                       (dfldAllPh3[(dfldAllPh3['pro_bymthch'] == 'yes') & (dfldAllPh3['Region_faci'] ==
                                                                           region)]['pro_bymthch'].count()/dfldAllPh3[dfldAllPh3['pro_bymthch'] == 'yes']['pro_bymthch'].count())*100),
        'STS1sthour LD': (dfldAllPh1[dfldAllPh1['skin_skin1sthr'] == 'yes']['skin_skin1sthr'].count(),
                      dfldAllPh2[dfldAllPh2['skin_skin1sthr']
                                 == 'yes']['skin_skin1sthr'].count(),
                      dfldAllPh3[dfldAllPh3['skin_skin1sthr'] == 'yes']['skin_skin1sthr'].count()),
        'STS1sthour Rep': (dfldAllPh1[(dfldAllPh1['skin_skin1sthr'] == 'yes') & (dfldAllPh1['Region_faci'] ==
                                                                          region)]['skin_skin1sthr'].count(),
                       dfldAllPh2[(dfldAllPh2['skin_skin1sthr'] == 'yes') & (dfldAllPh2['Region_faci'] ==
                                                                          region)]['skin_skin1sthr'].count(),
                       dfldAllPh3[(dfldAllPh3['skin_skin1sthr'] == 'yes') & (dfldAllPh3['Region_faci'] ==
                                                                          region)]['skin_skin1sthr'].count()),
        'P1(%)': ((dfldAllPh1[(dfldAllPh1['skin_skin1sthr'] == 'yes') & (dfldAllPh1['Region_faci'] ==
                                                                           region)]['skin_skin1sthr'].count()/dfldAllPh1[dfldAllPh1['skin_skin1sthr'] == 'yes']['skin_skin1sthr'].count())*100,
                       (dfldAllPh2[(dfldAllPh2['skin_skin1sthr'] == 'yes') & (dfldAllPh2['Region_faci'] ==
                                                                           region)]['skin_skin1sthr'].count()/dfldAllPh2[dfldAllPh2['skin_skin1sthr'] == 'yes']['skin_skin1sthr'].count())*100,
                       (dfldAllPh3[(dfldAllPh3['skin_skin1sthr'] == 'yes') & (dfldAllPh3['Region_faci'] ==
                                                                           region)]['skin_skin1sthr'].count()/dfldAllPh3[dfldAllPh3['skin_skin1sthr'] == 'yes']['skin_skin1sthr'].count())*100),
        'Cue of BF': (dfldAllPh1[dfldAllPh1['advise_bf'] == 'yes']['advise_bf'].count(),
                          dfldAllPh2[dfldAllPh2['advise_bf']
                                     == 'yes']['advise_bf'].count(),
                          dfldAllPh3[dfldAllPh3['advise_bf'] == 'yes']['advise_bf'].count()),
        'Cue of BF Rep': (dfldAllPh1[(dfldAllPh1['advise_bf'] == 'yes') & (dfldAllPh1['Region_faci'] ==
                                                                                 region)]['advise_bf'].count(),
                           dfldAllPh2[(dfldAllPh2['advise_bf'] == 'yes') & (dfldAllPh2['Region_faci'] ==
                                                                                 region)]['advise_bf'].count(),
                           dfldAllPh3[(dfldAllPh3['advise_bf'] == 'yes') & (dfldAllPh3['Region_faci'] ==
                                                                                 region)]['advise_bf'].count()),
        'P3(%)': ((dfldAllPh1[(dfldAllPh1['advise_bf'] == 'yes') & (dfldAllPh1['Region_faci'] ==
                                                                         region)]['advise_bf'].count()/dfldAllPh1[dfldAllPh1['advise_bf'] == 'yes']['advise_bf'].count())*100,
                  (dfldAllPh2[(dfldAllPh2['advise_bf'] == 'yes') & (dfldAllPh2['Region_faci'] ==
                                                                         region)]['advise_bf'].count()/dfldAllPh2[dfldAllPh2['advise_bf'] == 'yes']['advise_bf'].count())*100,
                  (dfldAllPh3[(dfldAllPh3['advise_bf'] == 'yes') & (dfldAllPh3['Region_faci'] ==
                                                                         region)]['advise_bf'].count()/dfldAllPh3[dfldAllPh3['advise_bf'] == 'yes']['advise_bf'].count())*100),
        'BF1sthour': (dfldAllPh1[(dfldAllPh1['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh1['hrsaft_birthbreast'] == '< 30 minutes')]['hrsaft_birthbreast'].count(),
                      dfldAllPh2[(dfldAllPh2['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh1['hrsaft_birthbreast'] == '< 30 minutes')]['advise_bf'].count(),
                      dfldAllPh3[(dfldAllPh3['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh1['hrsaft_birthbreast'] == '< 30 minutes')]['advise_bf'].count()),
        'BF1sthour Rep': (dfldAllPh1[((dfldAllPh1['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh1['hrsaft_birthbreast'] == '< 30 minutes')) & (dfldAllPh1['Region_faci'] ==
                                                                           region)]['advise_bf'].count(),
                          dfldAllPh2[((dfldAllPh2['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh2['hrsaft_birthbreast'] == '< 30 minutes')) & (dfldAllPh2['Region_faci'] ==
                                                                           region)]['advise_bf'].count(),
                          dfldAllPh3[((dfldAllPh3['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh3['hrsaft_birthbreast'] == '< 30 minutes')) & (dfldAllPh3['Region_faci'] ==
                                                                           region)]['advise_bf'].count()),
        'P4(%)': ((dfldAllPh1[((dfldAllPh1['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh1['hrsaft_birthbreast'] == '< 30 minutes')) & (dfldAllPh1['Region_faci'] ==
                                                                    region)]['advise_bf'].count()/dfldAllPh1[dfldAllPh1['advise_bf'] == 'yes']['advise_bf'].count())*100,
                  (dfldAllPh2[((dfldAllPh2['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh2['hrsaft_birthbreast'] == '< 30 minutes')) & (dfldAllPh2['Region_faci'] ==
                                                                    region)]['advise_bf'].count()/dfldAllPh2[dfldAllPh2['advise_bf'] == 'yes']['advise_bf'].count())*100,
                  (dfldAllPh3[((dfldAllPh3['hrsaft_birthbreast'] == '30 minutes to < 1 hour') | (dfldAllPh3['hrsaft_birthbreast'] == '< 30 minutes')) & (dfldAllPh3['Region_faci'] ==
                                                                    region)]['advise_bf'].count()/dfldAllPh3[dfldAllPh3['advise_bf'] == 'yes']['advise_bf'].count())*100)


 })

    st.write(pahses)

def displayKPIs(dfldAll, dfnicuAll, region, facilityR):
    # all alive babies in LD
    dfld = dfldAll[dfldAll['Region_faci']==region].sort_values(by=facilityR)
    # all babies addmited to NICU
    dfnicu = dfnicuAll[dfnicuAll['Region_faci'] == region].sort_values(by=facilityR)

    
    dfldalive = dfld[dfld['death_live']=='Alive']
    # STS - National
    dfstsAll = dfldAll[dfldAll['skin_skin1sthr']=="yes"]['_index']
    # STS - Tigray
    dfsts = dfldalive[dfldalive['skin_skin1sthr'] == "yes"][facilityR]
    stsrec = recordKPIs(dfldalive, dfsts)
    # Percentage of Tigray Represetaion
    repsts = dfsts.count()/dfstsAll.count()*100

    # Breast Feeding - National
    dfbfAll = dfldAll[(dfldAll['hrsaft_birthbreast'].notnull()) & (
        dfldAll['hrsaft_birthbreast'] != '1 hour to < 24 hours')]['_index']
    # Breast Feeding - Tigray
    dfbf = dfldalive[(dfldalive['hrsaft_birthbreast'].notnull()) & (
        dfldalive['hrsaft_birthbreast'] != '1 hour to < 24 hours')][facilityR]
    bfrec = recordKPIs(dfldalive, dfbf)
    # Percentage of Tigray Represetaion
    repbf = dfbf.count()/dfbfAll.count()*100
    
    # CPAP at NICU - National
    dfcpapAll = dfnicuAll[dfnicuAll['q117pro_CPAP'] == 'yes']['_index']
    # CPAP at NICU - Tigray
    dfcpap = dfnicu[dfnicu['q117pro_CPAP'] == 'yes'][facilityR]
    cpaprec = recordKPIs(dfldalive, dfcpap)
    # Percentage of Tigray Represetaion
    repcpap = dfcpap.count()/dfcpapAll.count()*100

    # Resuscitate LD - National
    dfrescldAll = dfldAll[dfldAll['pro_resusc']=="yes"]['_index']
    # Resuscitate LD - Tigray
    dfrescld = dfldalive[dfldalive['pro_resusc'] == "yes"][facilityR]
    rescrecld = recordKPIs(dfldalive, dfrescld)
    # Percentage of Tigray Represetaion
    represcld = dfrescld.count()/dfrescldAll.count()*100

    # Resuscitate NICU - National
    dfrescnicuAll = dfnicuAll[dfnicuAll['q115pro_resusc'] == "yes"]['_index']
    # Resuscitate NICU 
    dfrescnicu = dfnicu[dfnicu['q115pro_resusc'] == "yes"][facilityR]
    rescrecnicu = recordKPIs(dfldalive, dfrescnicu)
    # Percentage of Tigray Represetaion
    represcnicu = dfrescnicu.count()/dfrescnicuAll.count()*100

    # Two cues of Brest Feeding - National
    df2cueAll = dfldAll[dfldAll['advise_bf'] == 'yes']['_index']
    # Two cues of Brest Feeding - Tigray
    df2cue = dfldalive[dfldalive['advise_bf'] == 'yes'][facilityR]
    bf2cue = recordKPIs(dfldalive, df2cue)
    # Percentage of Tigray Represetaion
    repbf2cue = df2cue.count()/df2cueAll.count()*100


    # Wrapped  with plastic bag at LD - National
    dfplsldAll = dfldAll[dfldAll['pro_wrapbyplastb1'] == "yes"]['_index']
    # Wrapped  with plastic bag at LD - Tigray
    dfplsld = dfldalive[dfldalive['pro_wrapbyplastb1'] == "yes"][facilityR]
    plsld = recordKPIs(dfldalive, dfplsld)
    # Percentage of Tigray Represetaion
    repplsld = dfplsld.count()/dfplsldAll.count()*100

    # Wrapped  with plastic bag at NICU - National
    dfplsnAll = dfnicuAll[dfnicuAll['q123wrap_plastb'] == "yes"]['_index']
    # Wrapped  with plastic bag at NICU - Tigray
    dfplsn = dfnicu[dfnicu['q123wrap_plastb'] == "yes"][facilityR]
    plsnicu = recordKPIs(dfldalive, dfplsn)
    # Percentage of Tigray Represetaion
    repplsnicu = dfplsn.count()/dfplsnAll.count()*100


    # Antibiotics given at NICU - National
    dfantibAll = dfnicuAll[dfnicuAll['q116pro_gantib'] == 'yes']['_index']
    # Antibiotics given at NICU - Tigray
    dfantib = dfnicu[dfnicu['q116pro_gantib'] == 'yes'][facilityR]
    antib = recordKPIs(dfldalive, dfantib)
    # Percentage of Tigray Represetaion
    repantib = dfantib.count()/dfantibAll.count()*100

    st.write("Key evaluation indicators report: Representaion")
    # Create a dataframe - National vs Tigray

    dfkpis = pd.DataFrame({'Indicators': ('Proportion STS contact with in first 1hr',
                                          'Proportion BF initiated with in the first 1 hr', 'Proportion CPAP provision at  NICU', 'Provider resuscitated the new born LD', 'Provider resuscitated the new born NICU', 'Advised at least two cues of BF', 'Wrapped  with plastic bag at LD', 'Wrapped  with plastic bag at NICU', 'Antibiotics given at NICU '),
                           "National":  [dfstsAll.count(), dfbfAll.count(), dfcpapAll.count(), dfrescldAll.count(), dfrescnicuAll.count(), df2cueAll.count(), dfplsldAll.count(), dfplsnAll.count(), dfantibAll.count()],
                           "Rep":  [dfsts.count(), dfbf.count(), dfcpap.count(), dfrescld.count(), dfrescnicu.count(), df2cue.count(), dfplsld.count(), dfplsn.count(), dfantib.count()],
                           "Percent(%)":  [repsts, repbf, repcpap, represcld, represcnicu, repbf2cue, repplsld, repplsnicu, repantib]
                           })
    st.write(dfkpis)
    
    st.write("Key evaluation indicators report: Per Facility")
    # Create a dataframe - Each Facility

    dfkpis = pd.DataFrame({'Indicators': ('Proportion STS contact with in first 1hr',
                                          'Proportion BF initiated with in the first 1 hr', 'Proportion CPAP provision at  NICU', 'Provider resuscitated the new born LD', 'Provider resuscitated the new born NICU', 'Advised at least two cues of BF', 'Wrapped  with plastic bag at LD', 'Wrapped  with plastic bag at NICU', 'Antibiotics given at NICU '),
                           dfld[facilityR].unique()[0]:  [stsrec[0], bfrec[0], cpaprec[0], rescrecld[0], rescrecnicu[0], bf2cue[0], plsld[0], plsnicu[0], antib[0]],
                           dfld[facilityR].unique()[1]:  [stsrec[1], bfrec[1], cpaprec[1], rescrecld[1], rescrecnicu[1], bf2cue[1], plsld[1], plsnicu[1], antib[1]],
                           dfld[facilityR].unique()[2]:  [stsrec[2], bfrec[2], cpaprec[2], rescrecld[2], rescrecnicu[2], bf2cue[2], plsld[2], plsnicu[2], antib[2]],
                           dfld[facilityR].unique()[3]:  [stsrec[3], bfrec[3], cpaprec[3], rescrecld[3], rescrecnicu[3], bf2cue[3], plsld[3], plsnicu[3], antib[3]],
                           dfld[facilityR].unique()[4]:  [stsrec[4], bfrec[4], cpaprec[4], rescrecld[4], rescrecnicu[4], bf2cue[4], plsld[4], plsnicu[4], antib[4]],
                           dfld[facilityR].unique()[5]:  [stsrec[5], bfrec[5], cpaprec[5], rescrecld[5], rescrecnicu[5], bf2cue[5], plsld[5], plsnicu[5], antib[5]],
                           dfld[facilityR].unique()[6]:  [stsrec[6], bfrec[6], cpaprec[6], rescrecld[6], rescrecnicu[6], bf2cue[6], plsld[6], plsnicu[6], antib[6]],
                           dfld[facilityR].unique()[7]:  [stsrec[7], bfrec[7], cpaprec[7], rescrecld[7], rescrecnicu[7], bf2cue[7], plsld[7], plsnicu[7], antib[7]],
                           dfld[facilityR].unique()[8]:  [stsrec[8], bfrec[8], cpaprec[8], rescrecld[8], rescrecnicu[8], bf2cue[8], plsld[8], plsnicu[8], antib[8]],
                           'Total': [sum(stsrec), sum(bfrec), sum(cpaprec), sum(rescrecld), sum(rescrecnicu), sum(bf2cue), sum(plsld), sum(plsnicu), sum(antib)]
                           })
    st.write(dfkpis)

