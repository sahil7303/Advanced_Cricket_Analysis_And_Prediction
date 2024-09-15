import pandas as pd
import csv
from calculate_feature import total_run, avg_run, strike_rate, economy, bowling_avg, wickets_per_match, win_percentage

# Load ball-by-ball data
ball_by_ball = pd.read_csv('dataset/IPL_ball_by_ball_updated.csv')
players_list=set(ball_by_ball["striker"]).union(set(ball_by_ball["non_striker"])).union(set(ball_by_ball["bowler"]))
team_list=set(ball_by_ball["batting_team"])
stadium_list=set(ball_by_ball['venue'])

# Function to filter player data within and without the venue
def filter_player_data(player_name, venue, opponent_team):
    player_data_bowler_WV = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                                         (ball_by_ball['batting_team'] == opponent_team)]
    player_data_batsman_WV = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                                          (ball_by_ball['bowling_team'] == opponent_team)]

    # Filter for the venue
    player_data_bowler = player_data_bowler_WV[ball_by_ball['venue'] == venue]
    player_data_batsman = player_data_batsman_WV[ball_by_ball['venue'] == venue]
    
    return player_data_bowler, player_data_batsman, player_data_bowler_WV, player_data_batsman_WV

# Use the optimized function to calculate values for both within-venue and without-venue scenarios
def calculate_features(player_name, venue, opponent_team):
    player_data_bowler, player_data_batsman, player_data_bowler_WV, player_data_batsman_WV = filter_player_data(player_name, venue, opponent_team)

    if player_data_bowler.empty and player_data_batsman.empty and player_data_bowler_WV.empty and player_data_batsman_WV.empty:
        return None
    
    # Calculate all features within venue
    results_with_venue = {
        'Total runs': total_run(player_data_batsman),
        'Avg runs': avg_run(player_data_batsman),
        'Strike rate': strike_rate(player_data_batsman),
        'Economy': economy(player_data_bowler),
        'Bowling avg': bowling_avg(player_data_bowler),
        'Wickets per match': wickets_per_match(player_data_bowler),
        'Win percentage': win_percentage(player_data_bowler, player_data_batsman)
    }

    # Calculate all features without venue
    results_without_venue = {
        'Total runs WV': total_run(player_data_batsman_WV),
        'Avg runs WV': avg_run(player_data_batsman_WV),
        'Strike rate WV': strike_rate(player_data_batsman_WV),
        'Economy WV': economy(player_data_bowler_WV),
        'Bowling avg WV': bowling_avg(player_data_bowler_WV),
        'Wickets per match WV': wickets_per_match(player_data_bowler_WV),
        'Win percentage WV': win_percentage(player_data_bowler_WV, player_data_batsman_WV)
    }

    return results_with_venue, results_without_venue

# Create a CSV file and write data
with open('player_performance_data_optimized.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=[
        'Player', 'Opponent Team', 'Venue', 'Avg Run', 'Avg Run WV', 'Strike Rate', 
        'Strike Rate WV', 'Economy', 'Economy WV', 'Wickets per Match', 'Wickets per Match WV', 
        'Bowling Avg', 'Bowling Avg WV', 'Win Percentage'
    ])
    
    # Write the header row
    writer.writeheader()
    
    # Loop over players, teams, and venues to calculate values and write to CSV
    for player_name in players_list:
        for opponent_team in team_list:
            for venue in stadium_list:
                # Calculate the metrics
                results = calculate_features(player_name, venue, opponent_team)

                if results is None:
                    continue
                
                results_with_venue, results_without_venue = results
                
                # Write data to CSV
                row = {
                    'Player': player_name,
                    'Opponent Team': opponent_team,
                    'Venue': venue,
                    'Avg Run': results_with_venue['Avg runs'],
                    'Avg Run WV': results_without_venue['Avg runs WV'],
                    'Strike Rate': results_with_venue['Strike rate'],
                    'Strike Rate WV': results_without_venue['Strike rate WV'],
                    'Economy': results_with_venue['Economy'],
                    'Economy WV': results_without_venue['Economy WV'],
                    'Wickets per Match': results_with_venue['Wickets per match'],
                    'Wickets per Match WV': results_without_venue['Wickets per match WV'],
                    'Bowling Avg': results_with_venue['Bowling avg'],
                    'Bowling Avg WV': results_without_venue['Bowling avg WV'],
                    'Win Percentage': results_with_venue['Win percentage']
                }
                
                # Write row to CSV
                writer.writerow(row)

print("CSV file 'player_performance_data_optimized.csv' created successfully.")
