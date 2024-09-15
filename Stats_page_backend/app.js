const express = require('express');
const fs = require('fs');
const cors = require('cors'); 
const app = express();
const port = 3000;

app.use(cors());
// Function to read JSON files
const readJsonFile = (filePath) => {
  const data = fs.readFileSync(filePath, 'utf8');
  return JSON.parse(data);
};

// Load data from JSON files
const batsmenData = readJsonFile('./batsman.json');
const bowlersData = readJsonFile('./bowler.json');

// Helper function to find player by name
const findPlayerByName = (name) => {
  const batsman = batsmenData.find(player => player.Player.toLowerCase() === name.toLowerCase());
  const bowler = bowlersData.find(player => player.Player.toLowerCase() === name.toLowerCase());
  
  // Combine both batsman and bowler data if available
  return { batsman, bowler };
};

// API endpoint to get player data by name
app.get('/player/:name', (req, res) => {
  const playerName = req.params.name;
  const playerData = findPlayerByName(playerName);

  if (playerData.batsman || playerData.bowler) {
    res.json(playerData);
  } else {
    res.status(404).json({ error: 'Player not found' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
