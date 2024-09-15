// Array of players
const players = [
    "A Badoni", "A Chandila", "A Chopra", "A Choudhary", 
    "A Dananjaya", "A Flintoff", "A Kumble", "A Manohar", "A Mishra", 
    "A Mithun", "A Mukund", "A Nehra", "A Nel", "A Nortje", 
    "A Singh", "A Symonds", "A Tomar", "A Uniyal", "A Zampa", 
    "AA Bilakhia", "AA Chavan", "AA Jhunjhunwala", "AA Kazi", "AA Noffke", 
    "AB Agarkar", "AB Barath", "AB Dinda", "AB McDonald", "AB de Villiers", 
    "AC Blizzard", "AC Gilchrist", "AC Thomas", "AC Voges", 
    "AD Hales", "AD Mascarenhas", "AD Mathews", "AD Nath", "AD Russell", 
    "AF Milne", "AG Murtaza", "AG Paunikar", "AJ Finch", "AJ Hosein", 
    "AJ Turner", "AJ Tye", "AK Markram", "AL Menaria", "AM Nayar", 
    "AM Rahane", "AM Salvi", "AN Ahmed", "AN Ghosh", "AP Dole", 
    "AP Majumdar", "AP Tare", "AR Bawne", "AR Patel", "AS Joseph", 
    "AS Rajpoot", "AS Raut", "AS Roy", "AS Yadav", "AT Carey", 
    "AT Rayudu", "AU Rashid", "AUK Pathan", "Abdul Basith", "Abdul Samad", 
    "Abdur Razzak", "Abhishek Sharma", "Abishek Porel", "Akash Deep", 
    "Akash Madhwal", "Akash Singh", "Aman Hakim Khan", "Anand Rajan", 
    "Anirudh Singh", "Ankit Sharma", "Ankit Soni", "Anmolpreet Singh", 
    "Anuj Rawat", "Anureet Singh", "Arjun Tendulkar", "Arshad Khan", 
    "Arshdeep Singh", "Atharva Taide", "Avesh Khan", "Azhar Mahmood", 
    "B Akhil", "B Chipli", "B Geeves", "B Indrajith", "B Kumar", 
    "B Laughlin", "B Lee", "B Sai Sudharsan", "B Stanlake", "B Sumanth", 
    "BA Bhatt", "BA Stokes", "BAW Mendis", "BB McCullum", "BB Samantray", 
    "BB Sran", "BCJ Cutting", "BE Hendricks", "BJ Haddin", "BJ Hodge", 
    "BJ Rohrer", "BMAJ Mendis", "BR Dunk", "BW Hilfenhaus", 
    "Basil Thampi", "Bipul Sharma", "C Ganapathy", "C Green", "C Madan", 
    "C Munro", "C Nanda", "C Sakariya", "C de Grandhomme", "CA Ingram", 
    "CA Lynn", "CA Pujara", "CH Gayle", "CH Morris", "CJ Anderson", 
    "CJ Dala", "CJ Ferguson", "CJ Green", "CJ Jordan", "CJ McKay", 
    "CK Kapugedera", "CK Langeveldt", "CL White", "CM Gautam", 
    "CR Brathwaite", "CR Woakes", "CRD Fernando", "CV Varun", 
    "D Brevis", "D Kalyankrishna", "D Padikkal", "D Pretorius", 
    "D Salunkhe", "D Wiese", "D du Preez", "DA Miller", "DA Warner", 
    "DAJ Bracewell", "DB Das", "DB Ravi Teja", "DE Bollinger", 
    "DG Nalkande", "DH Yagnik", "DJ Bravo", "DJ Harris", "DJ Hooda", 
    "DJ Hussey", "DJ Jacobs", "DJ Malan", "DJ Mitchell", "DJ Muthuswami", 
    "DJ Thornely", "DJ Willey", "DJG Sammy", "DJM Short", "DL Chahar", 
    "DL Vettori", "DM Bravo", "DNT Zoysa", "DP Conway", "DP Nannes", 
    "DP Vijaykumar", "DPMD Jayawardene", "DR Martyn", "DR Sams", 
    "DR Shorey", "DR Smith", "DS Kulkarni", "DS Lehmann", 
    "DT Christian", "DT Patil", "DW Steyn", "Dhruv Jurel", 
    "Duan Jansen", "E Lewis", "EJG Morgan", "ER Dwivedi", 
    "F Behardien", "F du Plessis", "FA Allen", "FH Edwards", 
    "FY Fazal", "Fazalhaq Farooqi", "G Gambhir", "GB Hogg", 
    "GC Smith", "GC Viljoen", "GD McGrath", "GD Phillips", 
    "GH Vihari", "GHS Garton", "GJ Bailey", "GJ Maxwell", 
    "GR Napier", "GS Sandhu", "Gagandeep Singh", "Gurkeerat Singh", 
    "Gurnoor Brar", "H Das", "H Klaasen", "H Sharma", 
    "HC Brook", "HE van der Dussen", "HF Gurney", "HH Gibbs", 
    "HH Pandya", "HM Amla", "HR Shokeen", "HV Patel", 
    "Harbhajan Singh", "Harmeet Singh", "Harmeet Singh (2)", 
    "Harpreet Brar", "Harpreet Singh", "Harshit Rana", 
    "I Malhotra", "I Sharma", "I Udana", "IC Pandey", 
    "IC Porel", "IK Pathan", "IR Jaggi", "IS Sodhi", 
    "Imran Tahir", "Iqbal Abdulla", "Ishan Kishan", 
    "J Arunkumar", "J Botha", "J Little", "J Suchith", 
    "J Syed Mohammad", "J Theron", "J Yadav", "JA Morkel", 
    "JA Richardson", "JC Archer", "JC Buttler", "JD Ryder", 
    "JD Unadkat", "JDP Oram", "JDS Neesham", "JE Root", 
    "JE Taylor", "JEC Franklin", "JH Kallis", "JJ Bumrah", 
    "JJ Roy", "JJ van der Wath", "JL Denly", "JL Pattinson", 
    "JM Bairstow", "JM Kemp", "JM Sharma", "JO Holder", 
    "JP Behrendorff", "JP Duminy", "JP Faulkner", 
    "JPR Scantlebury-Searles", "JR Hazlewood", "JR Hopes", 
    "JR Philippe", "JW Hastings", "Jalaj S Saxena", "Jaskaran Singh", 
    "Joginder Sharma", "K Goel", "K Gowtham", "K Kartikeya", 
    "K Khejroliya", "K Rabada", "K Santokie", "K Upadhyay", 
    "K Yadav", "KA Jamieson", "KA Pollard", "KAJ Roach", 
    "KB Arun Karthik", "KC Cariappa", "KC Sangakkara", 
    "KD Karthik", "KH Pandya", "KJ Abbott", "KK Ahmed", 
    "KK Cooper", "KK Nair", "KL Nagarkoti", "KL Rahul", 
    "KM Asif", "KM Jadhav", "KMA Paul", "KMDN Kulasekara", 
    "KP Appanna", "KP Pietersen", "KR Mayers", "KR Sen", 
    "KS Bharat", "KS Sharma", "KS Williamson", "KV Sharma", 
    "KW Richardson", "Kamran Akmal", "Kamran Khan", 
    "Karanveer Singh", "Kartik Tyagi", "Kuldeep Yadav", 
    "L Ablish", "L Balaji", "L Ngidi", "L Ronchi", 
    "LA Carseldine", "LA Pomersbach", "LE Plunkett", 
    "LH Ferguson", "LI Meriwala", "LJ Wright", "LMP Simmons", 
    "LPC Silva", "LR Shukla", "LRPL Taylor", "LS Livingstone", 
    "Lalit Yadav", "Liton Das", "M Ashwin", "M Jansen", 
    "M Kaif", "M Kartik", "M Klinger", "M Manhas", 
    "M Markande", "M Morkel", "M Muralitharan", "M Ntini", 
    "M Pathirana", "M Prasidh Krishna", "M Rawat", "M Shahrukh Khan", 
    "M Theekshana", "M Vijay", "M Vohra", "M de Lange", 
    "MA Agarwal", "MA Khote", "MA Starc", "MA Wood", 
    "MB Parmar", "MC Henriques", "MC Juneja", "MD Mishra", 
    "MD Shanaka", "MDKJ Perera", "MEK Hussey", "MF Maharoof", 
    "MG Bracewell", "MG Johnson", "MG Neser", "MJ Clarke", 
    "MJ Guptill", "MJ Henry", "MJ Lumb", "MJ McClenaghan", 
    "MJ Santner", "MK Lomror", "MK Pandey", "MK Tiwary", 
    "ML Hayden", "MM Ali", "MM Patel", "MM Sharma", 
    "MN Samuels", "MN van Wyk", "MP Stoinis", "MR Marsh", 
    "MS Bisla", "MS Dhoni", "MS Gony", "MS Wade", 
    "MV Boucher", "MW Short", "Mandeep Singh", "Mashrafe Mortaza", 
    "Mayank Dagar", "Misbah-ul-Haq", "Mohammad Ashraful", 
    "Mohammad Asif", "Mohammad Hafeez", "Mohammad Nabi", 
    "Mohammed Shami", "Mohammed Siraj", "Mohit Rathee", 
    "Mohsin Khan", "Monu Kumar", "Mujeeb Ur Rahman", 
    "Mukesh Choudhary", "Mukesh Kumar", "Mustafizur Rahman", 
    "N Jagadeesan", "N Pooran", "N Rana", "N Saini", 
    "N Wadhera", "NA Saini", "NB Singh", "ND Doshi", 
    "NJ Maddinson", "NJ Rimmington", "NL McCullum", 
    "NLTC Perera", "NM Coulter-Nile", "NS Naik", "NT Ellis", 
    "NV Ojha", "Naveen-ul-Haq", "Niraj Patel", "Nithish Kumar Reddy", 
    "Noor Ahmad", "O Thomas", "OA Shah", "OC McCoy", 
    "OF Smith", "P Amarnath", "P Awana", "P Chopra", 
    "P Dogra", "P Dubey", "P Kumar", "P Negi", 
    "P Parameswaran", "P Prasanth", "P Ray Barman", "P Sahu", 
    "P Simran Singh", "P Suyal", "PA Patel", "PA Reddy", 
    "PBB Rajapaksa", "PC Valthaty", "PD Collingwood", 
    "PD Salt", "PH Solanki", "PJ Cummins", "PJ Sangwan", 
    "PK Garg", "PM Sarvesh Kumar", "PN Mankad", "PP Chawla", 
    "PP Ojha", "PP Shaw", "PR Shah", "PSP Handscomb", 
    "PV Tambe", "PVD Chameera", "PWH de Silva", "Pankaj Singh", 
    "Parvez Rasool", "Q de Kock", "R Ashwin", "R Bhatia", 
    "R Bishnoi", "R Dhawan", "R Dravid", "R Goyal", 
    "R McLaren", "R Ninan", "R Parag", "R Powell", 
    "R Rampaul", "R Sai Kishore", "R Sanjay Yadav", "R Sathish", 
    "R Sharma", "R Shepherd", "R Shukla", "R Tewatia", 
    "R Vinay Kumar", "RA Bawa", "RA Jadeja", "RA Shaikh", 
    "RA Tripathi", "RD Chahar", "RD Gaikwad", "RE Levi", 
    "RE van der Merwe", "RG More", "RG Sharma", "RJ Harris", 
    "RJ Peterson", "RJ Quiney", "RJW Topley", "RK Bhui", 
    "RK Singh", "RM Patidar", "RN ten Doeschate", "RP Meredith", 
    "RP Singh", "RR Bhatkal", "RR Bose", "RR Pant", 
    "RR Powar", "RR Raje", "RR Rossouw", "RR Sarwan", 
    "RS Bopara", "RS Gavaskar", "RS Hangargekar", "RS Sodhi", 
    "RT Ponting", "RV Gomez", "RV Patel", "RV Uthappa", 
    "RW Price", "Rahmanullah Gurbaz", "Ramandeep Singh", 
    "Rashid Khan", "Rasikh Salam", "Ravi Bishnoi", "S Anirudha", 
    "S Aravind", "S Badree", "S Badrinath", "S Chanderpaul", 
    "S Dhawan", "S Dube", "S Gopal", "S Kaul", 
    "S Kaushik", "S Ladda", "S Lamichhane", "S Midhun", 
    "S Nadeem", "S Narwal", "S Rana", "S Randiv", 
    "S Sandeep Warrier", "S Sohal", "S Sreesanth", 
    "S Sriram", "S Tyagi", "S Vidyut", "SA Abbott", 
    "SA Asnodkar", "SA Yadav", "SB Bangar", "SB Jakati", 
    "SB Joshi", "SB Styris", "SB Wagh", "SC Ganguly", 
    "SC Kuggeleijn", "SD Chitnis", "SD Lad", "SE Bond", 
    "SE Marsh", "SE Rutherford", "SJ Srivastava", "SK Raina", 
    "SK Trivedi", "SK Warne", "SL Malinga", "SM Boland", 
    "SM Curran", "SM Harwood", "SM Katich", "SM Pollock", 
    "SMSM Senanayake", "SN Khan", "SN Thakur", "SO Hetmyer", 
    "SP Fleming", "SP Goswami", "SP Jackson", "SP Narine", 
    "SPD Smith", "SR Tendulkar", "SR Watson", "SS Agarwal", 
    "SS Cottrell", "SS Iyer", "SS Mundhe", "SS Prabhudessai", 
    "SS Sarkar", "SS Shaikh", "SS Tiwary", "SSB Magala", 
    "ST Jayasuriya", "STR Binny", "SV Samson", "SW Billings", 
    "SW Tait", "Sachin Baby", "Salman Butt", "Sandeep Sharma", 
    "Sanvir Singh", "Shahbaz Ahmed", "Shahid Afridi", 
    "Shakib Al Hasan", "Shashank Singh", "Shivam Mavi", 
    "Shivam Sharma", "Shoaib Ahmed", "Shoaib Akhtar", 
    "Shoaib Malik", "Shubman Gill", "Sikandar Raza", 
    "Simarjeet Singh", "Sohail Tanvir", "Sunny Gupta", 
    "Sunny Singh", "Suyash Sharma", "Swapnil Singh", 
    "T Banton", "T Henderson", "T Kohli", "T Natarajan", 
    "T Shamsi", "T Stubbs", "T Taibu", "T Thushara", 
    "TA Boult", "TD Paine", "TG Southee", "TH David", 
    "TK Curran", "TL Seifert", "TL Suman", "TM Dilshan", 
    "TM Head", "TM Srivastava", "TP Sudhindra", "TR Birt", 
    "TS Mills", "TU Deshpande", "Tejas Baroka", "Tilak Varma", 
    "U Kaul", "UA Birla", "UBT Chand", "UT Khawaja", 
    "UT Yadav", "Umar Gul", "Umran Malik", "V Kohli", 
    "V Pratap Singh", "V Sehwag", "V Shankar", "VG Arora", 
    "VH Zol", "VR Aaron", "VR Iyer", "VRV Singh", 
    "VS Malik", "VS Yeligati", "VVS Laxman", "VY Mahesh", 
    "Vijaykumar Vyshak", "Virat Singh", "Vishnu Vinod", 
    "Vivrant Sharma", "W Jaffer", "WA Mota", "WD Parnell", 
    "WP Saha", "WPUJC Vaas", "Washington Sundar", 
    "X Thalaivan Sargunam", "Y Gnaneswara Rao", "Y Nagar", 
    "Y Prithvi Raj", "Y Venugopal Rao", "YA Abdulla", 
    "YBK Jaiswal", "YK Pathan", "YS Chahal", "YV Dhull", 
    "YV Takawale", "Yash Dayal", "Yash Thakur", 
    "Yashpal Singh", "Younis Khan", "Yudhvir Singh", 
    "Yuvraj Singh", "Z Khan"
  ];

  const teams = [
    "Chennai Super Kings",
    "Deccan Chargers",
    "Delhi Capitals",
    "Delhi Daredevils",
    "Gujarat Lions",
    "Gujarat Titans",
    "Kings XI Punjab",
    "Kochi Tuskers Kerala",
    "Kolkata Knight Riders",
    "Lucknow Super Giants",
    "Mumbai Indians",
    "Pune Warriors",
    "Punjab Kings",
    "Rajasthan Royals",
    "Rising Pune Supergiant",
    "Rising Pune Supergiants",
    "Royal Challengers Bangalore",
    "Sunrisers Hyderabad"
  ];

  const venues = [
    "Arun Jaitley Stadium",
    "Arun Jaitley Stadium, Delhi",
    "Barabati Stadium",
    "Barsapara Cricket Stadium, Guwahati",
    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
    "Brabourne Stadium",
    "Brabourne Stadium, Mumbai",
    "Buffalo Park",
    "De Beers Diamond Oval",
    "Dr DY Patil Sports Academy",
    "Dr DY Patil Sports Academy, Mumbai",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
    "Dubai International Cricket Stadium",
    "Eden Gardens",
    "Eden Gardens, Kolkata",
    "Feroz Shah Kotla",
    "Green Park",
    "Himachal Pradesh Cricket Association Stadium",
    "Himachal Pradesh Cricket Association Stadium, Dharamsala",
    "Holkar Cricket Stadium",
    "JSCA International Stadium Complex",
    "Kingsmead",
    "M Chinnaswamy Stadium",
    "M Chinnaswamy Stadium, Bengaluru",
    "M.Chinnaswamy Stadium",
    "MA Chidambaram Stadium",
    "MA Chidambaram Stadium, Chepauk",
    "MA Chidambaram Stadium, Chepauk, Chennai",
    "Maharashtra Cricket Association Stadium",
    "Maharashtra Cricket Association Stadium, Pune",
    "Narendra Modi Stadium, Ahmedabad",
    "Nehru Stadium",
    "New Wanderers Stadium",
    "Newlands",
    "OUTsurance Oval",
    "Punjab Cricket Association IS Bindra Stadium",
    "Punjab Cricket Association IS Bindra Stadium, Mohali",
    "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh",
    "Punjab Cricket Association Stadium, Mohali",
    "Rajiv Gandhi International Stadium",
    "Rajiv Gandhi International Stadium, Uppal",
    "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
    "Sardar Patel Stadium, Motera",
    "Saurashtra Cricket Association Stadium",
    "Sawai Mansingh Stadium",
    "Sawai Mansingh Stadium, Jaipur",
    "Shaheed Veer Narayan Singh International Stadium",
    "Sharjah Cricket Stadium",
    "Sheikh Zayed Stadium",
    "St George's Park",
    "Subrata Roy Sahara Stadium",
    "SuperSport Park",
    "Vidarbha Cricket Association Stadium, Jamtha",
    "Wankhede Stadium",
    "Wankhede Stadium, Mumbai",
    "Zayed Cricket Stadium, Abu Dhabi"
  ];
  
  
  
  // Function to populate the dropdowns with the updated player names
//   function populateSelectors() {
//     const playerSelectors = ['player1', 'player2', 'player3'];
//     playerSelectors.forEach(selectorId => {
//       const dropdown = document.getElementById(selectorId);
//       players.forEach(player => {
//         const option = document.createElement('option');
//         option.value = player;
//         option.textContent = player;
//         dropdown.appendChild(option);
//       });
//     });
//   }

  // Function to populate the dropdown with player names
function populatePlayerDropdown() {
    const dropdown = document.getElementById('player1');
  
    players.forEach(player => {
      const option = document.createElement('option');
      option.value = player;
      option.textContent = player;
      dropdown.appendChild(option);
    });
  }

  // Function to populate the dropdown with venue names
function populateVenuesDropdown() {
    const dropdown = document.getElementById('player2');
  
    venues.forEach(player => {
      const option = document.createElement('option');
      option.value = player;
      option.textContent = player;
      dropdown.appendChild(option);
    });
  }


  // Function to populate the dropdown with opponents names
function populateOpponentsDropdown() {
    const dropdown = document.getElementById('player3');
  
    teams.forEach(player => {
      const option = document.createElement('option');
      option.value = player;
      option.textContent = player;
      dropdown.appendChild(option);
    });
  }
  
  // Call this function on page load to populate the selectors
  window.onload = function() {
    populateOpponentsDropdown();
    populatePlayerDropdown();
    populateVenuesDropdown();
  }
  
  // Function to handle the submit button click
  function submitPlayers() {
    const player = document.getElementById('player1').value;
    const venue = document.getElementById('player2').value;
    const team = document.getElementById('player3').value;
    const errorMessage = document.getElementById('error-message');
    
    // Validate if all selectors have selected values
    if (!player || !venue || !team) {
      errorMessage.textContent = 'Please select values for all three dropdowns.';
      return;
    }
  
    // Clear any previous error message
    errorMessage.textContent = '';
  
    // Call a function with the selected values
    processSelectedPlayers(player, venue, team);
  }
  
  // Function to process the selected players
  function processSelectedPlayers(player, venue, team) {
    function getTeamAcronym(teamName) {
        return teamName
          .split(" ")
          .map(word => word[0].toUpperCase()) // Get the first letter and capitalize it
          .join(""); // Join the letters to form the acronym
      }
    
      // Get the formatted team acronym
      const teamAcronym = getTeamAcronym(team);
      const teamLogoURL = `https://scores.iplt20.com/ipl/teamlogos/${teamAcronym}.png?v=1`;
      document.querySelector("#teamLogo").src = teamLogoURL;
    // Prepare the request body
    document.getElementById('player-name').textContent = player;
    document.getElementById('player-name1').textContent = player;
    const requestBody = {
      "player_name": player,
      "venue": venue,
      "opponent": team
    };
  
    // Make the POST request using fetch API
    fetch("http://127.0.0.1:8000/player_stats", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(requestBody)
    })
    .then(response => response.json()) // Parse the JSON from the response
    .then(data => {
      // Store the response in variables
      const bowlingAvg = data.bowling_avg;
      const economy = data.economy;
      const run = data.run;
      const strikeRate = data.strike_rate;
      const wicketsPerMatch = data.wickets_per_match;

      document.getElementById('runs').textContent = run;
      document.getElementById('strikeRate').textContent = strikeRate;
      document.getElementById('bowAvg').textContent = bowlingAvg;
      document.getElementById('economy').textContent = economy;
      document.getElementById('wickets').textContent = wicketsPerMatch;
      
  
      // Log the results or use them as needed
      console.log("Bowling Avg:", bowlingAvg);
      console.log("Economy:", economy);
      console.log("Run:", run);
      console.log("Strike Rate:", strikeRate);
      console.log("Wickets per Match:", wicketsPerMatch);
    })
    .catch(error => {
      console.error("Error:", error);
    });
  }
  
  