import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ball_by_ball = pd.read_csv('dataset/IPL_ball_by_ball_updated.csv')

# Helper function to filter data once and reuse
def filter_player_data(player_name, venue, opponent_team):
    player_data_bowler_WV = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                                         (ball_by_ball['batting_team'] == opponent_team)]
    player_data_batsman_WV = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                                          (ball_by_ball['bowling_team'] == opponent_team)]

    # Filter for the venue
    player_data_bowler = player_data_bowler_WV[ball_by_ball['venue'] == venue]
    player_data_batsman = player_data_batsman_WV[ball_by_ball['venue'] == venue]
    
    return player_data_bowler, player_data_batsman, player_data_bowler_WV, player_data_batsman_WV

# Total runs calculation for batsman
def total_run(player_data_batsman):
    return player_data_batsman['runs_off_bat'].sum()

# Total matches calculation for batsman
def total_matches(player_data_batsman):
    return len(player_data_batsman['match_id'].unique())

# Average run calculation
def avg_run(player_data_batsman):
    TR = total_run(player_data_batsman)
    TM = total_matches(player_data_batsman)
    return TR / TM if TM != 0 else 10

# Bowls faced and strike rate calculation
def total_bowls_faced(player_data_batsman):
    return len(player_data_batsman)

def strike_rate(player_data_batsman):
    balls_faced = total_bowls_faced(player_data_batsman)
    return int(total_run(player_data_batsman) / balls_faced * 100) if balls_faced != 0 else 70

# Runs conceded and overs bowled calculation for bowlers
def total_run_conceded(player_data_bowler):
    return player_data_bowler["runs_off_bat"].sum() + player_data_bowler["extras"].sum()

def total_overs_bowled(player_data_bowler):
    overs_bowled = player_data_bowler['ball'].apply(lambda x: int(str(x).split('.')[0]))
    return len(overs_bowled.unique())

def economy(player_data_bowler):
    overs_bowled = total_overs_bowled(player_data_bowler)
    return total_run_conceded(player_data_bowler) / overs_bowled if overs_bowled != 0 else 16

# Wickets and bowling average calculation
def wickets_taken(player_data_bowler):
    return player_data_bowler['wicket_type'].notna().sum()

def bowling_avg(player_data_bowler):
    wickets = wickets_taken(player_data_bowler)
    return total_run_conceded(player_data_bowler) / wickets if wickets != 0 else 65

# Wickets per match calculation
def total_matches_bowler(player_data_bowler):
    return len(player_data_bowler['match_id'].unique())

def wickets_per_match(player_data_bowler):
    TM = total_matches_bowler(player_data_bowler)
    return wickets_taken(player_data_bowler) / TM if TM != 0 else 0

# Win percentage calculation
def win_percentage(player_data_bowler, player_data_batsman):
    win_baller = player_data_bowler[player_data_bowler['bowling_team'] == player_data_bowler['winner']]['match_id'].nunique()
    win_batsman = player_data_batsman[player_data_batsman['batting_team'] == player_data_batsman['winner']]['match_id'].nunique()
    
    total_matches_bowler = player_data_bowler['match_id'].nunique()
    total_matches_batsman = player_data_batsman['match_id'].nunique()
    
    WP_baller = win_baller / total_matches_bowler if total_matches_bowler != 0 else 0
    WP_batsman = win_batsman / total_matches_batsman if total_matches_batsman != 0 else 0
    
    ans = max(WP_baller, WP_batsman)
    
    return int(ans * 100) if ans != 0 else 40

# Use the above functions to calculate values for both within-venue and without-venue scenarios
def calculate_features(player_name, venue, opponent_team):
    player_data_bowler, player_data_batsman, player_data_bowler_WV, player_data_batsman_WV = filter_player_data(player_name, venue, opponent_team)

    # Calculate all features within venue
    print(f"Total runs (with venue): {total_run(player_data_batsman)}")
    print(f"Avg runs (with venue): {avg_run(player_data_batsman)}")
    print(f"Strike rate (with venue): {strike_rate(player_data_batsman)}")
    print(f"Economy (with venue): {economy(player_data_bowler)}")
    print(f"Bowling avg (with venue): {bowling_avg(player_data_bowler)}")
    print(f"Wickets per match (with venue): {wickets_per_match(player_data_bowler)}")
    print(f"Win percentage (with venue): {win_percentage(player_data_bowler, player_data_batsman)}")

    # Calculate all features without venue
    print(f"Total runs (without venue): {total_run(player_data_batsman_WV)}")
    print(f"Avg runs (without venue): {avg_run(player_data_batsman_WV)}")
    print(f"Strike rate (without venue): {strike_rate(player_data_batsman_WV)}")
    print(f"Economy (without venue): {economy(player_data_bowler_WV)}")
    print(f"Bowling avg (without venue): {bowling_avg(player_data_bowler_WV)}")
    print(f"Wickets per match (without venue): {wickets_per_match(player_data_bowler_WV)}")
    print(f"Win percentage (without venue): {win_percentage(player_data_bowler_WV, player_data_batsman_WV)}")

# Example usage
calculate_features('S Dhawan', 'Rajiv Gandhi International Stadium, Uppal', 'Royal Challengers Bangalore')
