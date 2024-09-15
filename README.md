# Advanced-Cricket-Analysis-And-Prediction

The Player Performance Analytics & Prediction Web App is designed to analyze and predict a cricket player’s performance in future matches. By leveraging machine learning models, the app compares a player’s performance in two matches—one win and one loss—against the same team, identifying key metrics such as runs, strike rate, wickets, and economy. Using these insights, the app forecasts the player’s expected performance in the next match and predicts fantasy points, assisting users in fantasy leagues, sports teams, and betting platforms.

## Features :
   1) See Players **Latest Stats**
   2) Predict the player's performance **against a Team** at a **specific Venue**

## Run Locally

To run this project locally, follow these steps:

1. **Clone the Repository:**

2. **Navigate to the Project Directory:**
   ```bash
   cd Advanced_Cricket_Analysis_And_Prediction
   ```
3. **Install the Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask Backend(which contains the model for prediction):**
   ```bash
   python Perdiction_backend/api.py
   ```

    To test the API do post call to `http://127.0.0.1:8000/player_stats` with json body like:
    ```
    {
      "player_name": player,
      "venue": venue,
      "opponent": team
    }
    ```
6. **Run the Node Backend(to get the player's current stats, team logo, player image etc.) :**
   1) go to `cd Stats_page_backend` folder
   2) Run the following command
   ```bash
     node app.js
   ```

   To test the API go to `http://localhost:3000/player/Harshal%20Patel`
7. **Access the App in Your Browser:**

Open the `index.html` file located inside the `Frontend` folder in your browser.

This will load the website front-end, allowing you to input player details and view predictions fetched from the API.

## Working of the Model
![Workflow](https://github.com/user-attachments/assets/040c0c7a-87cb-4858-a2ee-f62b2d3fd2c8)


## Screenshots:-
<img src="https://github.com/user-attachments/assets/4f1f451e-fe26-43c2-98e7-446e42aaf28a" width=auto>
<img src="https://github.com/user-attachments/assets/3804873e-aa18-4407-8da6-c511132bd2f4" width=auto>
<img src="https://github.com/user-attachments/assets/22f6b9d7-43ba-4e78-a986-e43cea85ec19" width=auto>

## Get the Figma design at
`https://www.figma.com/design/gXKwUrluXQXtEDWr3GwqMz/testingweb?node-id=0-1&node-type=canvas&t=RX3lQetclyUkMqVs-0`

