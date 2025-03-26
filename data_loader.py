import pandas as pd

# load the EPL games datasets
def load_data():
    df_season = pd.read_csv('data/gamesPlayed.csv')
    upcoming_fixtures = pd.read_csv('data/upcomingFixtures.csv')
    historical_data = pd.read_csv('data/cleanedHistoricalData/mergedHistory2017-2024.csv')
    return df_season, upcoming_fixtures, historical_data
