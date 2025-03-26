# EPL Match Analyzer App

This project is a Streamlit-based application for analyzing and predicting English Premier League (EPL) match outcomes. The app provides comprehensive analysis on:
- Seasonal performance (current season data)
- Recent form (last 5 games)
- Historical performance (from past seasons)
- Head-to-head comparisons between teams

## Features

- **Seasonal Analysis:** View team performance statistics, including wins, draws, losses, goals scored, goals conceded, and goal difference.
- **Recent Form:** Analyze the last 5 games for selected teams.
- **Head-to-Head Analysis:** Compare head-to-head records between any two teams using both historical and current season data.
- **Standings Calculation:** Compute league standings based on match outcomes.
- **Prediction:** A button is available for future enhancements to predict upcoming match results.

## Project Structure


- **data/**: Contains CSV files with match data.  
  - `gamesPlayed.csv`: Data for the current season.  
  - `upcomingFixtures.csv`: Data for upcoming fixtures.  
  - `cleanedHistoricalData/mergedHistory2017-2024.csv`: Historical match data from 2017 to 2024.

- **app/**: Contains the Streamlit application files.  
  - `main.py`: The entry point for the Streamlit app.  
  - `analysis.py`: Functions for analyzing team performance and head-to-head records.  
  - `last5.py`: Functions to analyze the last 5 games for teams.  
  - `h2h.py`: Functions for head-to-head analysis.

- **data_loader.py**: Module to load data from CSV files.  
- **utils.py**: Contains utility functions such as calculating standings, win/draw/loss, and goal difference.

## Data Sources and Extraction

The data used in this project comes from CSV files located in the `data/` directory:
- **gamesPlayed.csv**: Contains match results for the current season with columns such as `Date`, `Home`, `Score`, `Away`, `Venue`, `Referee`, `HomeScore`, and `AwayScore`.
- **upcomingFixtures.csv**: Contains fixture information for upcoming matches.
- **mergedHistory2017-2024.csv**: Contains historical match data for head-to-head analysis, including match results from 2017 to 2024.

The data is loaded using the function defined in `data_loader.py`:

```python


## How to Run the App
- Clone the repository: