import pandas as pd

# Load both datasets
ball_by_ball_df = pd.read_csv('dataset/IPL_ball_by_ball_updated.csv')
matches_df = pd.read_csv('dataset/matches_updated_mens_ipl.csv')

# Merge the 'winner' column from matches dataset to ball_by_ball dataset using 'match_id'
# Assuming 'matchId' in matches_df corresponds to 'match_id' in ball_by_ball_df
merged_df = ball_by_ball_df.merge(matches_df[['matchId', 'winner']], left_on='match_id', right_on='matchId', how='left')

# Drop the 'matchId' column as it may be redundant after merging
merged_df = merged_df.drop(columns=['matchId'])

# Save the merged dataset
merged_df.to_csv('dataset/ball_by_ball_with_winner.csv', index=False)

print("Winner column added and saved to 'ball_by_ball_with_winner.csv'")
