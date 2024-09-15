import pandas as pd

# Load the dataset (make sure the file path is correct)
df = pd.read_csv('../dataset/IPL_ball_by_ball_updated.csv')

# Extract unique values from 'striker' and 'non striker' columns
strikers = df['striker'].unique()
non_strikers = df['non_striker'].unique()

# Combine both and get unique batsmen
unique_batsmen = sorted(set(strikers).union(set(non_strikers)))

# Save the unique batsmen into a text file
with open('batsmen.txt', 'w') as f:
    for batsman in unique_batsmen:
        f.write(f"{batsman}\n")

print("Unique batsmen saved in 'batsmen.txt'")
