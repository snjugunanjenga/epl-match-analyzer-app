import streamlit as st
from utils import calculate_win_loss_draw, calculate_goal_difference, head_to_head

def render(home_team, away_team, df_season, historical_data):
    subtab_home, subtab_away = st.tabs(["Home", "Away"])

    # Home Team Analysis
    with subtab_home:
        st.header(f"Home Team Analysis: {home_team}")

        # Win/Draw/Loss
        wins, draws, losses = calculate_win_loss_draw(home_team, df_season)
        st.write(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")

        # Goal Difference
        goal_diff, goals_scored, goals_conceded = calculate_goal_difference(home_team, df_season)
        st.write(f"Goal Difference: {goal_diff} (Scored: {goals_scored}, Conceded: {goals_conceded})")

        # Head-to-Head Record
        h2h_matches = head_to_head(home_team, away_team, historical_data)
        st.subheader(f"Head-to-Head Record against {away_team}")
        st.write(h2h_matches)

    # Away Team Analysis
    with subtab_away:
        st.header(f"Away Team Analysis: {away_team}")

        # Win/Draw/Loss
        wins, draws, losses = calculate_win_loss_draw(away_team, df_season)
        st.write(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")

        # Goal Difference
        goal_diff, goals_scored, goals_conceded = calculate_goal_difference(away_team, df_season)
        st.write(f"Goal Difference: {goal_diff} (Scored: {goals_scored}, Conceded: {goals_conceded})")

        # Head-to-Head Record
        h2h_matches = head_to_head(away_team, home_team, historical_data)
        st.subheader(f"Head-to-Head Record against {home_team}")
        st.write(h2h_matches)

