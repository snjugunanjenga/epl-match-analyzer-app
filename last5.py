import streamlit as st
import pandas as pd

def render(home_team, away_team, df_season, selected_date):
    subtab_home, subtab_away = st.tabs(["Home", "Away"])
    
    with subtab_home:
        st.header(f"Last 5 Games - Home Team: {home_team}")
        last_5_home = df_season[
            ((df_season['Home'] == home_team) | (df_season['Away'] == home_team)) & 
            (pd.to_datetime(df_season['Date']) <= pd.to_datetime(selected_date))
        ].sort_values(by='Date', ascending=False).head(5)
        st.table(last_5_home)
    
    with subtab_away:
        st.header(f"Last 5 Games - Away Team: {away_team}")
        last_5_away = df_season[
            ((df_season['Home'] == away_team) | (df_season['Away'] == away_team)) & 
            (pd.to_datetime(df_season['Date']) <= pd.to_datetime(selected_date))
        ].sort_values(by='Date', ascending=False).head(5)
        st.table(last_5_away)
