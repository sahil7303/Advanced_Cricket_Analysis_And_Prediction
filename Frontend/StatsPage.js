const players = [
  'Virat Kohli', 'Ruturaj Gaikwad', 'Riyan Parag', 'Travis Head', 'Sanju Samson',
  'Sai Sudharsan', 'K L Rahul', 'Nicholas Pooran', 'Sunil Narine', 'Abhishek Sharma',
  'Heinrich Klaasen', 'Rishabh Pant', 'Faf Du Plessis', 'Phil Salt', 'Yashasvi Jaiswal',
  'Shubman Gill', 'Rohit Sharma', 'Tilak Varma', 'Shivam Dube', 'Rajat Patidar',
  'Marcus Stoinis', 'Tristan Stubbs', 'Venkatesh Iyer', 'Jos Buttler', 'Shashank Singh',
  'Shreyas Iyer', 'Suryakumar Yadav', 'Prabhsimran Singh', 'Jake Fraser - McGurk', 'Abishek Porel',
  'Dinesh Karthik', 'Ishan Kishan', 'Daryl Mitchell', 'Nitish Kumar Reddy', 'Jonny Bairstow',
  'Sam Curran', 'Ravindra Jadeja', 'Cameron Green', 'Quinton De Kock', 'Ajinkya Rahane',
  'Tim David', 'Ayush Badoni', 'Axar Patel', 'Will Jacks', 'Andre Russell', 'Rachin Ravindra',
  'Aiden Markram', 'Hardik Pandya', 'Shahbaz Ahmed', 'Rilee Rossouw', 'David Miller',
  'Prithvi Shaw', 'Dhruv Jurel', 'Ashutosh Sharma', 'Rahul Tewatia', 'Jitesh Sharma',
  'Shai Hope', 'Abdul Samad', 'Rinku Singh', 'David Warner', 'Rahul Tripathi',
  'Angkrish Raghuvanshi', 'MS Dhoni', 'Shikhar Dhawan', 'Deepak Hooda', 'Naman Dhir',
  'Pat Cummins', 'Wriddhiman Saha', 'Krunal Pandya', 'Moeen Ali', 'Shahrukh Khan',
  'Ramandeep Singh', 'Mahipal Lomror', 'Shimron Hetmyer', 'Liam Livingstone', 'Nehal Wadhera',
  'Rovman Powell', 'Rashid Khan', 'Anuj Rawat', 'Ravichandran Ashwin', 'Arshad Khan',
  'Vijay Shankar', 'Harpreet Brar', 'Dewald Brevis', 'Mayank Agarwal', 'Rahmanullah Gurbaz',
  'Mitchell Marsh', 'Atharva Taide', 'Romario Shepherd', 'Glenn Maxwell', 'Sameer Rizwi',
  'Tom Kohler- Cadmore', 'Kuldeep Yadav', 'Sikandar Raza', 'Manish Pandey', 'Azmatullah Omarzai',
  'Nitish Rana', 'Devdutt Padikkal', 'Swapnil Singh', 'Mohammad Nabi', 'Shubham Dubey',
  'Karn Sharma', 'Rasikh Salam', 'Kane Williamson', 'Harpreet Bhatia', 'Suyash S Prabhudessai',
  'Jaydev Unadkat', 'Tanush Kotian', 'Bhuvneshwar Kumar', 'Yudhvir Singh', 'Rahul Chahar',
  'Shardul Thakur', 'Ashton Turner', 'Kagiso Rabada', 'Gulbadin Naib', 'Marco Jansen',
  'Saurav Chauhan', 'Sumit Kumar', 'Piyush Chawla', 'Sanvir Singh', 'Trent Boult',
  'Mitchell Santner', 'Gerald Coetzee', 'Sai Kishore', 'Harshal Patel', 'Mohammed Siraj',
  'Darshan Nalkande', 'Jasprit Bumrah', 'Umesh Yadav', 'Avesh Khan', 'Lalit Yadav',
  'Luke Wood', 'Arshin Atul Kulkarni', 'Mitchell Starc', 'Abhinav Manohar', 'Donovan Ferreira',
  'Vijayakanth Viyaskanth', 'Spencer Johnson', 'Anmolpreet Singh', 'Noor Ahmad',
  'Arshdeep Singh', 'Akash Madhwal', 'Matthew Wade', 'Ravi Bishnoi', 'Anrich Nortje',
  'Mohit Sharma', 'Anukul Roy', 'Reece Topley', 'Kumar Kushagra', 'Mukesh Kumar',
  'Ricky Bhui', 'Mohsin Khan', 'Richard Gleeson', 'Jhye Richardson', 'Anshul Kamboj',
  'Akash Deep', 'Shivam Singh', 'Naveen-Ul-Haq', 'B R Sharath', 'Vaibhav Arora',
  'Shams Mulani', 'Lockie Ferguson', 'Lizaad Williams', 'Keshav Maharaj', 'Manav Suthar',
  'Vyshak Vijaykumar', 'Ishant Sharma', 'Harshal Patel', 'Varun Chakaravarthy',
  'Jasprit Bumrah', 'T Natarajan', 'Harshit Rana', 'Avesh Khan', 'Arshdeep Singh',
  'Andre Russell', 'Pat Cummins', 'Yuzvendra Chahal', 'Sunil Narine', 'Tushar Deshpande',
  'Khaleel Ahmed', 'Mukesh Kumar', 'Mitchell Starc', 'Trent Boult', 'Kuldeep Yadav',
  'Sam Curran', 'Yash Dayal', 'Mohammed Siraj', 'Mustafizur Rahman', 'Naveen-Ul-Haq',
  'Matheesha Pathirana', 'Sandeep Sharma', 'Piyush Chawla', 'Gerald Coetzee', 'Mohit Sharma',
  'Axar Patel', 'Kagiso Rabada', 'Vaibhav Arora', 'Bhuvneshwar Kumar', 'Hardik Pandya',
  'Yash Thakur', 'Rashid Khan', 'Cameron Green', 'Ravi Bishnoi', 'Rahul Chahar',
  'Ishant Sharma', 'Mohsin Khan', 'Ravichandran Ashwin', 'Lockie Ferguson', 'Rasikh Salam',
  'Ravindra Jadeja', 'Noor Ahmad', 'Nuwan Thushara', 'Umesh Yadav', 'Jaydev Unadkat',
  'Mayank Markande', 'Mayank Yadav', 'Harpreet Brar', 'Nandre Burger', 'Sai Kishore',
  'Shahbaz Ahmed', 'Karn Sharma', 'Anrich Nortje', 'Krunal Pandya', 'Glenn Maxwell',
  'Swapnil Singh', 'Kuldeep Sen', 'Sandeep Warrier', 'Deepak Chahar', 'Shardul Thakur',
  'Simarjeet Singh', 'Akash Madhwal', 'Azmatullah Omarzai', 'Marcus Stoinis', 'Spencer Johnson',
  'Vyshak Vijaykumar', 'Reece Topley', 'Josh Little', 'Liam Livingstone', 'Tristan Stubbs',
  'Darshan Nalkande', 'Shreyas Gopal', 'Nitish Kumar Reddy', 'Keshav Maharaj', 'Mitchell Santner',
  'Maheesh Theekshana', 'Abhishek Sharma', 'Mohammad Nabi', 'Moeen Ali', 'Vidwath Kaverappa',
  'Will Jacks', 'Anshul Kamboj', 'Shashank Singh', 'Nathan Ellis', 'M Siddharth',
  'Vijayakanth Viyaskanth', 'Richard Gleeson', 'Matt Henry', 'Amit Mishra', 'Mayank Dagar',
  'Arshad Khan', 'Daryl Mitchell', 'Alzarri Joseph', 'Lizaad Williams', 'Mitchell Marsh',
  'Marco Jansen', 'Yudhvir Singh', 'Romario Shepherd', 'Shivam Dube', 'Washington Sundar',
  'Kwena Maphaka', 'Luke Wood', 'Akash Deep'
];



function fetchData(playerName) {
// Fetch player data from the API
fetch(`http://localhost:3000/player/${playerName}`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Get player name from the API response
    const playerName = data.batsman ? data.batsman.Player : data.bowler.Player;
    const playerImg = data.batsman ? data.batsman.Image : data.bowler.Image;
    const teamLogo = data.batsman ? data.batsman.Logo : data.bowler.Logo;
    const batsmanRun = data.batsman ? data.batsman.Runs : 0;
    const batsmanInnings = data.batsman ? data.batsman.Inns : 0;
    const batsmanHS = data.batsman ? data.batsman.HS : 0;
    const batsmanAvgScore = data.batsman ? data.batsman.Avg : 0;
    const bowlerEconomy = data.bowler ? data.bowler.Econ : 0;
    const bowlerWicket = data.bowler ? data.bowler.Wkts : 0;
    const bowlingAvg = data.bowler ?  data.bowler.Avg: 0;
    const bowlerInnings = data.bowler ? data.bowler.Inns:0;
    

    // Set the player name in the HTML
    document.getElementById('player-name').textContent = playerName;
    document.getElementById('player-name1').textContent = playerName;
    document.getElementById('runs').textContent = batsmanRun;
    document.getElementById('inningsData').textContent = batsmanInnings;
    document.getElementById('hs').textContent = batsmanHS;
    document.getElementById('avg').textContent = batsmanAvgScore;
    document.getElementById('runsGiven').textContent = bowlerEconomy;
    document.getElementById('wickets').textContent = bowlerWicket;
    document.getElementById('bowAvg').textContent = bowlingAvg;
    document.querySelector("#playerImg").src = playerImg;
    document.querySelector("#teamLogo").src = teamLogo;
  })
  .catch(error => {
    console.error('Error fetching player data:', error);
  });
};


// Function to populate the dropdown with player names
function populatePlayerDropdown() {
  const dropdown = document.getElementById('player-dropdown');

  players.forEach(player => {
    const option = document.createElement('option');
    option.value = player;
    option.textContent = player;
    dropdown.appendChild(option);
  });
}

function playerChanged() {
  const selectedPlayer = document.getElementById('player-dropdown').value;
  console.log(selectedPlayer);
  const formattedPlayerName = selectedPlayer.replace(/\s+/g, '%20');
  fetchData(formattedPlayerName);
}

window.onload=function(){
  populatePlayerDropdown();
  populateOpponentsDropdown();
  populateVenuesDropdown();
  fetchData();
}