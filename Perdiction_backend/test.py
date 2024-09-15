# from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
import json

# class NumpyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.float32):
#             return float(obj)
#         return super(NumpyEncoder, self).default(obj)

# app = Flask(__name__)

# @app.route('/player_stats', methods=['POST'])
# def player_stats():
#     try:
#         # Extracting input from the request
#         data = request.json
        
#         # Getting the input data
#         player_name = data.get('player_name')
#         venue = data.get('venue')
#         opponent = data.get('opponent')
        
#         # Load your dataset
#         X_dataframe = pd.read_csv('/home/harsh-patel/Desktop/projects/Advance-Cricket-Analysis-And-Prediction/player_performance_data_optimized.csv')
        
#         # Filter the dataframe based on player, opponent, and venue
#         X_values = X_dataframe[
#             (X_dataframe['Player'] == player_name) &
#             (X_dataframe['Opponent Team'] == opponent) &
#             (X_dataframe['Venue'] == venue)
#         ]
        
#         # Check if X_values is empty
#         if X_values.empty:
#             return jsonify({'error': 'No data found for the given player, opponent, and venue'}), 400
        
#         # Extract the required X features
#         x = X_values[['Avg Run', 'Avg Run WV', 'Strike Rate', 'Strike Rate WV', 
#                       'Economy', 'Economy WV', 'Wickets per Match', 
#                       'Wickets per Match WV', 'Bowling Avg', 'Bowling Avg WV', 
#                       'Win Percentage']]
        
#         # Load the trained model
#         loaded_model = joblib.load('xgboost_model.pkl')
        
#         # Convert to numpy array
#         x = x.values  # Convert pandas DataFrame to numpy array
        
#         # Predict the player stats using the loaded model
#         prediction = loaded_model.predict(x)
        
#         # Convert each prediction to a Python native type (e.g., int or float) to avoid serialization issues
#         run, strike_rate, economy, bowling_avg, wickets_per_match = [int(i) for i in prediction[0]]
        
#         # Return the response as JSON (using the custom encoder)
#         return jsonify({
#             'run': (run),
#             'strike_rate': (strike_rate),
#             'economy': (economy),
#             'bowling_avg': (bowling_avg),
#             'wickets_per_match': (wickets_per_match),
#          }), 200
    
#     except Exception as e:
#         # Handle errors
#         return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

if True :
        player_name="DA Warner"
        opponent="Rajasthan Royals"
        venue="Eden Gardens, Kolkata"
        # Load your dataset
        X_dataframe = pd.read_csv('/home/harsh-patel/Desktop/projects/Advance-Cricket-Analysis-And-Prediction/player_performance_data_optimized.csv')
        
        # Filter the dataframe based on player, opponent, and venue
        X_values = X_dataframe[
            (X_dataframe['Player'] == player_name) &
            (X_dataframe['Opponent Team'] == opponent) &
            (X_dataframe['Venue'] == venue)
        ]
        
        # Check if X_values is empty
        if X_values.empty:
            return jsonify({'error': 'No data found for the given player, opponent, and venue'}), 400
        
        # Extract the required X features
        x = X_values[['Avg Run', 'Avg Run WV', 'Strike Rate', 'Strike Rate WV', 
                      'Economy', 'Economy WV', 'Wickets per Match', 
                      'Wickets per Match WV', 'Bowling Avg', 'Bowling Avg WV', 
                      'Win Percentage']]
        
        # Load the trained model
        loaded_model = joblib.load('xgboost_model.pkl')
        
        # Convert to numpy array
        x = x.values  # Convert pandas DataFrame to numpy array
        
        # Predict the player stats using the loaded model
        prediction = loaded_model.predict(x)
        
        # Convert each prediction to a Python native type (e.g., int or float) to avoid serialization issues
        run, strike_rate, economy, bowling_avg, wickets_per_match = [int(i) for i in prediction[0]]
        print(run)
        print(type(run))
        