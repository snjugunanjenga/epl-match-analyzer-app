import streamlit as st
from data_loader import load_data
from utils import calculate_standings
import analysis, last5, h2h
import pandas as pd 

# Load data
df_season, upcoming_fixtures, historical_data = load_data()

def main():
    st.title("Premier League Match Analyzer")

    # Sidebar for date and team selection
    st.sidebar.title("Match Selection")
    last_date = df_season['Date'].max()
    selected_date = st.sidebar.date_input("Select Match Date", pd.to_datetime(last_date))
    home_team = st.sidebar.selectbox("Select Home Team", sorted(df_season['Home'].unique()))
    away_team = st.sidebar.selectbox("Select Away Team", sorted(df_season['Away'].unique()))

    # Filter matches up to the selected date
    df_filtered = df_season[pd.to_datetime(df_season['Date']) <= pd.to_datetime(selected_date)]
    
    # Calculate standings
    standings = calculate_standings(df_filtered)
    st.subheader(f"Standings as of: {selected_date}")
    st.table(standings)

    # Create main tabs
    tab_analysis, tab_last5, tab_h2h = st.tabs(["Analysis", "Last 5 Games", "Head-to-Head"])

    # Render each tab using imported modules
    with tab_analysis:
        analysis.render(home_team, away_team, df_filtered, historical_data)
    with tab_last5:    
        last5.render(home_team, away_team, df_season, selected_date)
    with tab_h2h:
        h2h.render(home_team, away_team, historical_data)

    st.subheader('Upcoming Fixtures')
    next_10_fixtures = upcoming_fixtures.head(10)
    st.table(next_10_fixtures)

    
    st.sidebar.button('predict Score')

    st.sidebar.button('Analyze')

    st.sidebar.button('predict more')

if __name__ == "__main__":
    main()
