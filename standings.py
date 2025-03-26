import pandas as pd
import streamlit as st

# Load the cleaned dataset from CSV
df_season = pd.read_csv('data\cleaned_data25.csv')

def calculate_standings(df):
    standings = pd.DataFrame(columns=['Team', 'Played', 'Won', 'Drawn', 'Lost', 'GoalsFor', 'GoalsAgainst', 'Goal Diff', 'Points'])
    
    teams = pd.concat([df['Home'], df['Away']]).unique()  # Get unique teams
    for team in teams:
        # Filter matches where the team played at home or away
        home_matches = df[df['Home'] == team]
        away_matches = df[df['Away'] == team]
        
        played = len(home_matches) + len(away_matches)
        won = len(home_matches[home_matches['HomeScore'] > home_matches['AwayScore']]) + \
              len(away_matches[away_matches['AwayScore'] > away_matches['HomeScore']])
        drawn = len(home_matches[home_matches['HomeScore'] == home_matches['AwayScore']]) + \
                len(away_matches[away_matches['AwayScore'] == away_matches['HomeScore']])
        lost = played - (won + drawn)
        goals_for = home_matches['HomeScore'].sum() + away_matches['AwayScore'].sum()
        goals_against = home_matches['AwayScore'].sum() + away_matches['HomeScore'].sum()
        goal_diff = goals_for - goals_against
        points = won * 3 + drawn
        
        # Add the team's stats to the standings DataFrame
        standings = pd.concat([standings, pd.DataFrame({
            'Team': [team],
            'Played': [played],
            'Won': [won],
            'Drawn': [drawn],
            'Lost': [lost],
            'GoalsFor': [goals_for],
            'GoalsAgainst': [goals_against],
            'Goal Diff': [goal_diff],
            'Points': [points]
        })], ignore_index=True)
    
    standings.sort_values(by='Points', ascending=False, inplace=True)
    standings['Position'] = range(1, len(standings) + 1)  # Add position numbers from 1 to N
    standings = standings[['Position', 'Team', 'Played', 'Won', 'Drawn', 'Lost', 'GoalsFor', 'GoalsAgainst', 'Goal Diff', 'Points']]  # Reorder columns
    return standings

def main():
    st.title("Premier League Match Analyzer")
    
    st.title("Premier League Standings")
    
    # Get the last match date from the dataset
    last_date = df_season['Date'].max()
    
    # Sidebar for date selection, pre-selecting the last match day
    selected_date = st.sidebar.date_input("Select Match Date", pd.to_datetime(last_date))
    
    # home team
    home_Team = st.sidebar.text_input("Select Home team")

    
    # Away team
    Away_Team = st.sidebar.text_input("Select Away team")

    # Filter matches up to the selected date
    df_filtered = df_season[pd.to_datetime(df_season['Date']) <= pd.to_datetime(selected_date)]
    
    # Calculate standings based on the filtered data
    standings = calculate_standings(df_filtered)
    
    st.subheader(f"Standings as of: {selected_date}")
    st.table(standings)

    # Main Tabs
    tab1, tab2, tab3 = st.tabs(["Analysis", "Last 5 Games", "Head-to-Head"])
    
    # Analysis Tab
    with tab1:
        subtab1, subtab2 = st.tabs(["Home", "Away"])
        
        with subtab1:
            st.header(f"Analysis - Home Team: {home_team}")
            # Insert your code for Home Team Analysis here
            # For example, display stats, recent performance, etc.
            
        with subtab2:
            st.header(f"Analysis - Away Team: {away_team}")
            # Insert your code for Away Team Analysis here
            # For example, display stats, recent performance, etc.
    
    # Last 5 Games Tab
    with tab2:
        subtab1, subtab2 = st.tabs(["Home", "Away"])
        
        with subtab1:
            st.header(f"Last 5 Games - Home Team: {home_team}")
            # Filter last 5 games for home team
            home_team_matches = df_season[
                ((df_season['Home'] == home_team) | (df_season['Away'] == home_team)) &
                (pd.to_datetime(df_season['Date']) <= pd.to_datetime(selected_date))
            ].sort_values(by='Date', ascending=False).head(5)
            st.table(home_team_matches)
            
        with subtab2:
            st.header(f"Last 5 Games - Away Team: {away_team}")
            # Filter last 5 games for away team
            away_team_matches = df_season[
                ((df_season['Home'] == away_team) | (df_season['Away'] == away_team)) &
                (pd.to_datetime(df_season['Date']) <= pd.to_datetime(selected_date))
            ].sort_values(by='Date', ascending=False).head(5)
            st.table(away_team_matches)
    
    # Head-to-Head Tab
    with tab3:
        subtab1, subtab2 = st.tabs(["Home", "Away"])
        
        with subtab1:
            st.header(f"Head-to-Head at Home for {home_team}")
            # Filter head-to-head matches where home_team was at home
            h2h_home = df_season[
                (df_season['Home'] == home_team) & 
                (df_season['Away'] == away_team) &
                (pd.to_datetime(df_season['Date']) <= pd.to_datetime(selected_date))
            ].sort_values(by='Date', ascending=False)
            st.table(h2h_home)
            
        with subtab2:
            st.header(f"Head-to-Head at Home for {away_team}")
            # Filter head-to-head matches where away_team was at home
            h2h_away = df_season[
                (df_season['Home'] == away_team) & 
                (df_season['Away'] == home_team) &
                (pd.to_datetime(df_season['Date']) <= pd.to_datetime(selected_date))
            ].sort_values(by='Date', ascending=False)
            st.table(h2h_away)

if __name__ == "__main__":
    main()
