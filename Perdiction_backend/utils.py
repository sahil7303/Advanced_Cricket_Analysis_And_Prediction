import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ball_by_ball= pd.read_csv('dataset/IPL_ball_by_ball_updated.csv')

def total_run(player_name, venue, opponent_team):
    # Filter rows where the player is the striker, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['bowling_team'] == opponent_team)]
    
    # Sum the runs_off_bat for the filtered rows
    total_runs = player_data['runs_off_bat'].sum()
    
    return total_runs

def total_matches(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['bowling_team'] == opponent_team)]
    

    return len(player_data['match_id'].unique())

def avg_run(player_name, venue, opponent_team) :
    TR=total_run(player_name, venue, opponent_team)
    TM=total_matches(player_name, venue, opponent_team)
    if TM !=0 :
       avgrun= TR/TM
       return avgrun
    else :
        return 10

#y
def total_run_y(player_name, venue, opponent_team,match_id):
    # Filter rows where the player is the striker, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['bowling_team'] == opponent_team) 
                               & (ball_by_ball['match_id']==match_id)]
    
    # Sum the runs_off_bat for the filtered rows
    total_runs = player_data['runs_off_bat'].sum()
    
    return total_runs

def total_matches_y(player_name, venue, opponent_team,match_id) :
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['bowling_team'] == opponent_team)
                               & (ball_by_ball['match_id']==match_id)]
    

    return len(player_data['match_id'].unique())

def avg_run_y(player_name, venue, opponent_team,match_id) :
    TR=total_run_y(player_name, venue, opponent_team,match_id)
    TM=total_matches_y(player_name, venue, opponent_team,match_id)
    if TM !=0 :
       avgrun= TR/TM
       return avgrun
    else :
        return 10



def total_run_WV(player_name, venue, opponent_team):
    # Filter rows where the player is the striker, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['bowling_team'] == opponent_team)]
    
    # Sum the runs_off_bat for the filtered rows
    total_runs = player_data['runs_off_bat'].sum()
    
    return total_runs

def total_matches_WV(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['bowling_team'] == opponent_team)]
    

    return len(player_data['match_id'].unique())

def avg_run_WV(player_name, venue, opponent_team) :
    TR=total_run_WV(player_name, venue, opponent_team)
    TM=total_matches_WV(player_name, venue, opponent_team)
    if TM !=0 :
       avgrun= TR/TM
       return avgrun
    else :
        return 10


def total_bowls_faced(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['bowling_team'] == opponent_team)]
    return len(player_data['match_id'])
def strike_rate(player_name, venue, opponent_team) :
    if total_bowls_faced(player_name, venue, opponent_team)!=0 :
     SR=int (total_run(player_name, venue, opponent_team)/total_bowls_faced(player_name, venue, opponent_team)*100)
     return SR
    else :
        return 70
#y
def total_bowls_faced_y(player_name, venue, opponent_team,match_id) :
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['bowling_team'] == opponent_team)
                                & (ball_by_ball['match_id']==match_id)]
    return len(player_data['match_id'])
def strike_rate_y(player_name, venue, opponent_team,match_id) :
    if total_bowls_faced_y(player_name, venue, opponent_team,match_id)!=0 :
     SR=int (total_run_y(player_name, venue, opponent_team,match_id)/total_bowls_faced_y(player_name, venue, opponent_team,match_id)*100)
     return SR
    else :
        return 70

def total_bowls_faced_WV(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['bowling_team'] == opponent_team)]
    return len(player_data['match_id'])
def strike_rate_WV(player_name, venue, opponent_team) :
    if total_bowls_faced(player_name, venue, opponent_team)!=0 :
     SR=int (total_run_WV(player_name, venue, opponent_team)/total_bowls_faced_WV(player_name, venue, opponent_team)*100)
     return SR
    else :
        return 70

def total_run_conceded(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    total_run=player_data["runs_off_bat"].sum()+player_data["extras"].sum()
    return total_run
def total_overs_bowled(player_name, venue, opponent_team):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    
    # Extract the 'ball' column, which represents balls like 0.1, 0.2, etc.
    # Convert them to over numbers by taking the integer part
    overs_bowled = player_data['ball'].apply(lambda x: int(str(x).split('.')[0])) +player_data['match_id'].apply(lambda x: int(str(x).split('.')[0]))*10

    # Count the unique over numbers to get the total overs bowled
    total_overs = len(overs_bowled.unique())
    
    return total_overs

def economy(player_name, venue, opponent_team) :
    if total_overs_bowled(player_name, venue, opponent_team) !=0 :
     eco=total_run_conceded(player_name, venue, opponent_team)/total_overs_bowled(player_name, venue, opponent_team)
     return eco
    else :
        return 16
#y
def total_run_conceded_y(player_name, venue, opponent_team,match_id) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)
                               & (ball_by_ball['match_id']==match_id)]
    total_run=player_data["runs_off_bat"].sum()+player_data["extras"].sum()
    return total_run
def total_overs_bowled_y(player_name, venue, opponent_team,match_id):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)
                               & (ball_by_ball['match_id']==match_id)]
    
    # Extract the 'ball' column, which represents balls like 0.1, 0.2, etc.
    # Convert them to over numbers by taking the integer part
    overs_bowled = player_data['ball'].apply(lambda x: int(str(x).split('.')[0])) +player_data['match_id'].apply(lambda x: int(str(x).split('.')[0]))*10

    # Count the unique over numbers to get the total overs bowled
    total_overs = len(overs_bowled.unique())
    
    return total_overs

def economy_y(player_name, venue, opponent_team,match_id) :
    if total_overs_bowled_y(player_name, venue, opponent_team,match_id) !=0 :
     eco=total_run_conceded_y(player_name, venue, opponent_team,match_id)/total_overs_bowled_y(player_name, venue, opponent_team,match_id)
     return eco
    else :
        return 16

def total_run_conceded_WV(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    total_run=player_data["runs_off_bat"].sum()+player_data["extras"].sum()
    return total_run
def total_overs_bowled_WV(player_name, venue, opponent_team):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    
    # Extract the 'ball' column, which represents balls like 0.1, 0.2, etc.
    # Convert them to over numbers by taking the integer part
    overs_bowled = player_data['ball'].apply(lambda x: int(str(x).split('.')[0])) +player_data['match_id'].apply(lambda x: int(str(x).split('.')[0]))*10

    # Count the unique over numbers to get the total overs bowled
    total_overs = len(overs_bowled.unique())
    
    return total_overs


def economy_WV(player_name, venue, opponent_team) :
    if total_overs_bowled_WV(player_name, venue, opponent_team) !=0 :
     eco=total_run_conceded_WV(player_name, venue, opponent_team)/total_overs_bowled_WV(player_name, venue, opponent_team)
     return eco
    else :
        return 16


def wickets_taken(player_name, venue, opponent_team):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    
    # Count the number of rows where 'wicket_type' is not null
    wickets = player_data['wicket_type'].notna().sum()
    
    return wickets

def total_matches_bowler(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    

    return len(player_data['match_id'].unique())

def wickets_per_match(player_name, venue, opponent_team):
    if total_matches_bowler(player_name, venue, opponent_team)!=0 :
      wpm = wickets_taken(player_name, venue, opponent_team)/total_matches_bowler(player_name, venue, opponent_team)
      return wpm
    else :
        return 0

#y
def wickets_taken_y(player_name, venue, opponent_team,match_id):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)
                               & (ball_by_ball['match_id']==match_id)]
    
    # Count the number of rows where 'wicket_type' is not null
    wickets = player_data['wicket_type'].notna().sum()
    
    return wickets

def total_matches_bowler_y(player_name, venue, opponent_team,match_id) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)
                               & (ball_by_ball['match_id']==match_id)]
    

    return len(player_data['match_id'].unique())

def wickets_per_match_y(player_name, venue, opponent_team,match_id):
    if total_matches_bowler_y(player_name, venue, opponent_team,match_id)!=0 :
      wpm = wickets_taken_y(player_name, venue, opponent_team,match_id)/total_matches_bowler_y(player_name, venue, opponent_team,match_id)
      return wpm
    else :
        return 0

def wickets_taken_WV(player_name, venue, opponent_team):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    
    # Count the number of rows where 'wicket_type' is not null
    wickets = player_data['wicket_type'].notna().sum()
    
    return wickets

def total_matches_bowler_WV(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    

    return len(player_data['match_id'].unique())

def wickets_per_match_WV(player_name, venue, opponent_team):
    if total_matches_bowler_WV(player_name, venue, opponent_team)!=0 :
      wpm = wickets_taken_WV(player_name, venue, opponent_team)/total_matches_bowler_WV(player_name, venue, opponent_team)
      return wpm
    else :
        return 0
    

def total_run_conceded(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    total_run=player_data["runs_off_bat"].sum()+player_data["extras"].sum()
    return total_run

def wickets_taken(player_name, venue, opponent_team):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    
    # Count the number of rows where 'wicket_type' is not null
    wickets = player_data['wicket_type'].notna().sum()
    
    return wickets

def bowling_avg(player_name, venue, opponent_team):
    if wickets_taken(player_name, venue, opponent_team) !=0 :
     ba=total_run_conceded(player_name, venue, opponent_team)/wickets_taken(player_name, venue, opponent_team)
     return ba
    else :
      return 65

#y
def total_run_conceded_y(player_name, venue, opponent_team,match_id) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)
                               & (ball_by_ball['match_id']==match_id)]
    total_run=player_data["runs_off_bat"].sum()+player_data["extras"].sum()
    return total_run

def wickets_taken_y(player_name, venue, opponent_team,match_id):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['venue'] == venue) &
                               (ball_by_ball['batting_team'] == opponent_team)
                               & (ball_by_ball['match_id']==match_id)]
    
    # Count the number of rows where 'wicket_type' is not null
    wickets = player_data['wicket_type'].notna().sum()
    
    return wickets

def bowling_avg_y(player_name, venue, opponent_team,match_id):
    if wickets_taken_y(player_name, venue, opponent_team,match_id) !=0 :
     ba=total_run_conceded_y(player_name, venue, opponent_team,match_id)/wickets_taken_y(player_name, venue, opponent_team,match_id)
     return ba
    else :
      return 65

def total_run_conceded_WV(player_name, venue, opponent_team) :
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    total_run=player_data["runs_off_bat"].sum()+player_data["extras"].sum()
    return total_run

def wickets_taken_WV(player_name, venue, opponent_team):
    # Filter rows where the player is the bowler, at the specific venue, and against the opponent team
    player_data = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    
    # Count the number of rows where 'wicket_type' is not null
    wickets = player_data['wicket_type'].notna().sum()
    
    return wickets

def bowling_avg_WV(player_name, venue, opponent_team):
    if wickets_taken_WV(player_name, venue, opponent_team) !=0 :
     ba=total_run_conceded_WV(player_name, venue, opponent_team)/wickets_taken_WV(player_name, venue, opponent_team)
     return ba
    else :
      return 65

def win_percentage(player_name, venue, opponent_team) :
    player_data_bowler = ball_by_ball[(ball_by_ball['bowler'] == player_name) &
                               (ball_by_ball['batting_team'] == opponent_team)]
    player_data_batsman = ball_by_ball[(ball_by_ball['striker'] == player_name) &
                               (ball_by_ball['bowling_team'] == opponent_team)]
    
    win_baller = []
    if not player_data_bowler.empty:
        for idx, datapoint in player_data_bowler.iterrows():
            if datapoint['bowling_team'] == datapoint['winner']:
                win_baller.append(datapoint['match_id'])
    
    wins_num_bowler = len(set(win_baller))
    total_matches_bowler = len(player_data_bowler['match_id'].unique())
    
    win_batsman = []
    if not player_data_batsman.empty:
        for idx, datapoint in player_data_batsman.iterrows():
            if datapoint['batting_team'] == datapoint['winner']:
                win_batsman.append(datapoint['match_id'])
    
    wins_num_batsman = len(set(win_batsman))
    total_matches_batsman = len(player_data_batsman['match_id'].unique())
    
    WP_baller = 0
    if total_matches_bowler:
        WP_baller = wins_num_bowler / total_matches_bowler
    
    WP_batsman = 0
    if total_matches_batsman:
        WP_baller = wins_num_batsman / total_matches_batsman
    
    ans = max(WP_baller, WP_batsman)

    if ans == 0:
        return 40
    else:
        return int(ans * 100)
