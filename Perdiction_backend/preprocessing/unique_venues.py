import pandas as pd

# Load the dataset (assuming it's a CSV file)
# Replace 'your_dataset.csv' with the path to your ball-by-ball dataset
df = pd.read_csv('../dataset/IPL_ball_by_ball_updated.csv')


# Extract unique teams from the 'batting team' column
unique_venue = sorted(df['venue'].unique())

# Save the unique teams into a text file
with open('venues.txt', 'w') as f:
    for venue in unique_venue:
        f.write(f"{venue}\n")

print("Unique venues saved in 'unique_venues.txt'")
