import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL of the website (e.g., FBref or Understat)
base_url = "https://fbref.com/en/comps/9/{year}/Premier-League-Stats"

# Define the years you want to scrape
years = list(range(2017, 2025))

# List to store all match data
matches_data = []

# Function to scrape match details for a specific season
def scrape_season(year):
    url = base_url.format(year=year)
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data for {year}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract match information from the page
    table = soup.find('table', {'id': 'results2021-2022'})  # Update the table ID based on the page's structure
    if table:
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 0:
                date = cells[0].get_text()
                home_team = cells[1].get_text()
                away_team = cells[2].get_text()
                score = cells[3].get_text().split('–')
                home_goals, away_goals = score[0], score[1]
                
                # Optional: Add events like goals, yellow cards, etc.
                # For simplicity, I'll skip these for now, but you can add similar logic for those fields.
                
                # Store the match data
                match_data = {
                    "Date": date,
                    "Home Team": home_team,
                    "Away Team": away_team,
                    "Home Goals": home_goals,
                    "Away Goals": away_goals,
                    # Add more fields as needed (e.g., match events)
                }
                matches_data.append(match_data)

# Scrape data for all specified years
for year in years:
    print(f"Scraping data for season: {year}")
    scrape_season(year)
    time.sleep(2)  # Pause to avoid hitting the server too frequently

# Convert the data to a DataFrame
df = pd.DataFrame(matches_data)

# Save to a CSV file
df.to_csv('epl_match_data_2017_2024.csv', index=False)

print("Scraping complete! Data saved to 'epl_match_data_2017_2024.csv'.")
