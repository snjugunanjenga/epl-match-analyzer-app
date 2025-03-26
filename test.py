import pandas as pd

# Load the data
df = pd.read_csv('data/gamesPlayed.csv')
historical_data = pd.read_csv('data/cleanedHistoricalData/mergedHistory2017-2024.csv')

def calculate_home_performance_ratio(team, historical_data):
    # Filter home matches for the specified team
    home_matches = historical_data[historical_data['Home'] == team]
    
    # Calculate wins, draws, and losses
    wins = len(home_matches[home_matches['HomeScore'] > home_matches['AwayScore']])
    draws = len(home_matches[home_matches['HomeScore'] == home_matches['AwayScore']])
    losses = len(home_matches[home_matches['HomeScore'] < home_matches['AwayScore']])
    
    # Calculate goals scored and goals conceded
    goals_scored = home_matches['HomeScore'].sum()
    goals_conceded = home_matches['AwayScore'].sum()
    
    # Calculate goal difference (GD)
    goal_difference = goals_scored - goals_conceded
    
    # Calculate win-draw-loss ratio
    total_matches = wins + draws + losses
    if total_matches > 0:
        win_draw_loss_ratio = (wins / total_matches, draws / total_matches, losses / total_matches)
    else:
        win_draw_loss_ratio = (0, 0, 0)  # Avoid division by zero if no matches

    return win_draw_loss_ratio, goal_difference

# Example usage
sample_team = 'Arsenal'  # Replace with an actual team from your dataset
home_performance = calculate_home_performance_ratio(sample_team, historical_data)
print(f"Win-Draw-Loss Ratio: {home_performance[0]}, Goal Difference: {home_performance[1]}")
