import streamlit as st

def render(home_team, away_team, historical_data):
    subtab_home, subtab_away = st.tabs(["Home", "Away"])
    
    with subtab_home:
        st.header(f"Head-to-Head at Home for {home_team}")
        h2h_home = historical_data[(
            historical_data['Home'] == home_team) &
            (historical_data['Away'] == away_team)].sort_values(by= 'Date' , ascending=False  ) 
        st.table(h2h_home)
    
    with subtab_away:
        st.header(f"Head-to-Head at Away for {away_team}")
        h2h_away = historical_data[(
            historical_data['Home'] == home_team) & 
            (historical_data['Away'] == away_team)].sort_values(by= 'Date' , ascending=False )
        st.table(h2h_away)
