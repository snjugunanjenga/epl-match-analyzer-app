import pandas as pd

def calculate_standings(df):
    standings = pd.DataFrame(columns=['Team', 'Played', 'Won', 'Drawn', 'Lost', 'GoalsFor', 'GoalsAgainst', 'Goal Diff', 'Points'])
    
    teams = pd.concat([df['Home'], df['Away']]).unique()
    for team in teams:
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
    standings['Position'] = range(1, len(standings) + 1)
    return standings[['Position', 'Team', 'Played', 'Won', 'Drawn', 'Lost', 'GoalsFor', 'GoalsAgainst', 'Goal Diff', 'Points']]

import pandas as pd

# Load the data
df = pd.read_csv('data/gamesPlayed.csv')
historical_data = pd.read_csv('data/cleanedHistoricalData/mergedHistory2017-2024.csv')

def calculate_win_loss_draw(team, df):
    """
    Calculates the win, draw, and loss count for a given team
    from the provided dataframe (df).
    
    Parameters:
        team (str): Name of the team.
        df (pd.DataFrame): DataFrame containing match data.
                           Expected columns: 'Home', 'Away', 'HomeScore', 'AwayScore'
    
    Returns:
        wins (int): Total wins.
        draws (int): Total draws.
        losses (int): Total losses.
    """
    # Matches where the team played at home
    home_matches = df[df['Home'] == team]
    home_wins = home_matches[home_matches['HomeScore'] > home_matches['AwayScore']].shape[0]
    home_draws = home_matches[home_matches['HomeScore'] == home_matches['AwayScore']].shape[0]
    home_losses = home_matches[home_matches['HomeScore'] < home_matches['AwayScore']].shape[0]
    
    # Matches where the team played away
    away_matches = df[df['Away'] == team]
    away_wins = away_matches[away_matches['AwayScore'] > away_matches['HomeScore']].shape[0]
    away_draws = away_matches[away_matches['AwayScore'] == away_matches['HomeScore']].shape[0]
    away_losses = away_matches[away_matches['AwayScore'] < away_matches['HomeScore']].shape[0]
    
    wins = home_wins + away_wins
    draws = home_draws + away_draws
    losses = home_losses + away_losses
    
    return wins, draws, losses

def calculate_goal_difference(team, df):
    """
    Calculates the goal difference for a given team from the provided dataframe.
    
    Parameters:
        team (str): Name of the team.
        df (pd.DataFrame): DataFrame containing match data.
                           Expected columns: 'Home', 'Away', 'HomeScore', 'AwayScore'
    
    Returns:
        goal_diff (int): Goal difference (Goals scored - Goals conceded).
        goals_scored (int): Total goals scored by the team.
        goals_conceded (int): Total goals conceded by the team.
    """
    # Matches where the team played at home
    home_matches = df[df['Home'] == team]
    home_goals_scored = home_matches['HomeScore'].sum()
    home_goals_conceded = home_matches['AwayScore'].sum()
    
    # Matches where the team played away
    away_matches = df[df['Away'] == team]
    away_goals_scored = away_matches['AwayScore'].sum()
    away_goals_conceded = away_matches['HomeScore'].sum()
    
    goals_scored = home_goals_scored + away_goals_scored
    goals_conceded = home_goals_conceded + away_goals_conceded
    goal_diff = goals_scored - goals_conceded
    
    return goal_diff, goals_scored, goals_conceded

def head_to_head(team_a, team_b, historical_data):
    """
    Returns a dataframe containing the head-to-head matches between team_a and team_b
    from the historical dataset.
    
    Parameters:
        team_a (str): First team name.
        team_b (str): Second team name.
        historical_data (pd.DataFrame): DataFrame containing historical match data.
                                      Expected columns: 'Home', 'Away', 'Date', 'HomeScore', 'AwayScore'
    
    Returns:
        h2h_df (pd.DataFrame): DataFrame of head-to-head matches sorted by date (descending).
    """
    h2h_df = historical_data[
        ((historical_data['Home'] == team_a) & (historical_data['Away'] == team_b)) |
        ((historical_data['Home'] == team_b) & (historical_data['Away'] == team_a))
    ]
    h2h_df = h2h_df.sort_values(by='Date', ascending=False)
    return h2h_df

