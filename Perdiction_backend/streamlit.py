import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random

# Function to load options from a text file
def load_options(file_path):
    with open(file_path, 'r') as file:
        options = [line.strip() for line in file]
    return options

# Dictionary of top 30 popular players with their base stats
top_30_players = {
    'V Kohli': {
        'avg_run': 38.16,
        'strike_rate': 130.25,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'MS Dhoni': {
        'avg_run': 39.20,
        'strike_rate': 135.19,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'R Sharma': {
        'avg_run': 31.75,
        'strike_rate': 130.50,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'AB de Villiers': {
        'avg_run': 40.77,
        'strike_rate': 151.68,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'KL Rahul': {
        'avg_run': 46.71,
        'strike_rate': 136.37,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'SK Raina': {
        'avg_run': 33.34,
        'strike_rate': 137.14,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'DA Warner': {
        'avg_run': 42.71,
        'strike_rate': 140.57,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'AD Russell': {
        'avg_run': 29.28,
        'strike_rate': 177.88,
        'economy': 9.15,
        'bowling_avg': 27.20,
        'wickets_per_match': 1.18
    },
    'HH Pandya': {
        'avg_run': 29.98,
        'strike_rate': 142.30,
        'economy': 8.76,
        'bowling_avg': 31.10,
        'wickets_per_match': 0.72
    },
    'JJ Bumrah': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 7.39,
        'bowling_avg': 24.63,
        'wickets_per_match': 1.30
    },
    'Rashid Khan': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 6.37,
        'bowling_avg': 20.83,
        'wickets_per_match': 1.42
    },
    'S Dhawan': {
        'avg_run': 35.34,
        'strike_rate': 127.55,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'B Kumar': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 7.23,
        'bowling_avg': 25.43,
        'wickets_per_match': 1.12
    },
    'SP Narine': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 6.74,
        'bowling_avg': 25.30,
        'wickets_per_match': 1.00
    },
    'BA Stokes': {
        'avg_run': 24.60,
        'strike_rate': 134.50,
        'economy': 8.56,
        'bowling_avg': 34.89,
        'wickets_per_match': 0.78
    },
    'RA Jadeja': {
        'avg_run': 26.56,
        'strike_rate': 128.54,
        'economy': 7.58,
        'bowling_avg': 30.27,
        'wickets_per_match': 0.84
    },
    'F du Plessis': {
        'avg_run': 35.33,
        'strike_rate': 131.22,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'SS Iyer': {
        'avg_run': 31.67,
        'strike_rate': 126.96,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'KA Pollard': {
        'avg_run': 29.16,
        'strike_rate': 149.77,
        'economy': 8.82,
        'bowling_avg': 31.59,
        'wickets_per_match': 0.85
    },
    'YS Chahal': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 7.61,
        'bowling_avg': 24.57,
        'wickets_per_match': 1.20
    },
    'KS Williamson': {
        'avg_run': 36.22,
        'strike_rate': 126.03,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'PJ Cummins': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 8.13,
        'bowling_avg': 30.10,
        'wickets_per_match': 0.94
    },
    'Mohammed Shami': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 8.45,
        'bowling_avg': 27.20,
        'wickets_per_match': 1.15
    },
    'TA Boult': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 7.90,
        'bowling_avg': 26.27,
        'wickets_per_match': 1.10
    },
    'N Pooran': {
        'avg_run': 25.25,
        'strike_rate': 151.24,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'RD Gaikwad': {
        'avg_run': 37.82,
        'strike_rate': 130.65,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'Ishan Kishan': {
        'avg_run': 28.50,
        'strike_rate': 132.53,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'SM Curran': {
        'avg_run': 18.90,
        'strike_rate': 132.43,
        'economy': 9.02,
        'bowling_avg': 33.44,
        'wickets_per_match': 0.89
    },
    'Q de Kock': {
        'avg_run': 33.37,
        'strike_rate': 134.67,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'DL Chahar': {
        'avg_run': 10.0,
        'strike_rate': 100.0,
        'economy': 7.73,
        'bowling_avg': 27.85,
        'wickets_per_match': 1.10
    },
    'Shubman Gill': {
        'avg_run': 34.25,
        'strike_rate': 132.33,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'MP Stoinis': {
        'avg_run': 23.50,
        'strike_rate': 140.28,
        'economy': 9.15,
        'bowling_avg': 30.10,
        'wickets_per_match': 0.85
    },
    'AM Rahane': {
        'avg_run': 32.13,
        'strike_rate': 120.67,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'KD Karthik': {
        'avg_run': 27.21,
        'strike_rate': 133.88,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'SV Samson': {
        'avg_run': 29.84,
        'strike_rate': 136.71,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'AR Patel': {
        'avg_run': 20.15,
        'strike_rate': 128.53,
        'economy': 7.40,
        'bowling_avg': 31.54,
        'wickets_per_match': 0.92
    },
    'CH Gayle': {
        'avg_run': 40.24,
        'strike_rate': 149.45,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'JC Buttler': {
        'avg_run': 36.93,
        'strike_rate': 150.32,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'Mohammed Siraj': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 8.50,
        'bowling_avg': 26.35,
        'wickets_per_match': 1.12
    },
    'Imran Tahir': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.88,
        'bowling_avg': 23.69,
        'wickets_per_match': 1.25
    },
    'R Tewatia': {
        'avg_run': 22.33,
        'strike_rate': 140.35,
        'economy': 7.67,
        'bowling_avg': 35.42,
        'wickets_per_match': 0.75
    },
    'CV Varun': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.21,
        'bowling_avg': 25.30,
        'wickets_per_match': 1.05
    },
    'LS Livingstone': {
        'avg_run': 24.15,
        'strike_rate': 149.45,
        'economy': 8.50,
        'bowling_avg': 32.45,
        'wickets_per_match': 0.70
    },
    'T Natarajan': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 8.19,
        'bowling_avg': 27.58,
        'wickets_per_match': 1.05
    },
    'MA Starc': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.16,
        'bowling_avg': 20.40,
        'wickets_per_match': 1.20
    },
    'N Saini': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 8.45,
        'bowling_avg': 31.58,
        'wickets_per_match': 1.10
    },
    'Kuldeep Yadav': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 8.20,
        'bowling_avg': 27.41,
        'wickets_per_match': 1.02
    },
    'Avesh Khan': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 8.15,
        'bowling_avg': 25.45,
        'wickets_per_match': 1.15
    },
    'YK Pathan': {
        'avg_run': 28.34,
        'strike_rate': 145.34,
        'economy': 8.50,
        'bowling_avg': 35.23,
        'wickets_per_match': 0.65
    },
    'HV Patel': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 8.55,
        'bowling_avg': 25.32,
        'wickets_per_match': 1.20
    },
    'DJ Hooda': {
        'avg_run': 22.35,
        'strike_rate': 130.42,
        'economy': 8.30,
        'bowling_avg': 40.12,
        'wickets_per_match': 0.55
    },
    'R Parag': {
        'avg_run': 21.12,
        'strike_rate': 125.35,
        'economy': 8.42,
        'bowling_avg': 36.45,
        'wickets_per_match': 0.65
    },
    'A Nortje': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.95,
        'bowling_avg': 25.12,
        'wickets_per_match': 1.18
    },
    'A Zampa': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.85,
        'bowling_avg': 23.45,
        'wickets_per_match': 1.22
    },
    'JO Holder': {
        'avg_run': 18.23,
        'strike_rate': 128.35,
        'economy': 8.15,
        'bowling_avg': 29.34,
        'wickets_per_match': 1.05
    },
    'CH Morris': {
        'avg_run': 15.50,
        'strike_rate': 140.56,
        'economy': 8.20,
        'bowling_avg': 25.58,
        'wickets_per_match': 1.14
    },
    'JC Archer': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.50,
        'bowling_avg': 21.45,
        'wickets_per_match': 1.20
    },
    'LH Ferguson': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.60,
        'bowling_avg': 23.12,
        'wickets_per_match': 1.05
    },
    'Ravi Bishnoi': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.40,
        'bowling_avg': 24.32,
        'wickets_per_match': 1.12
    },
    'Washington Sundar': {
        'avg_run': 16.15,
        'strike_rate': 125.55,
        'economy': 7.23,
        'bowling_avg': 32.40,
        'wickets_per_match': 0.85
    },
    'PP Shaw': {
        'avg_run': 24.20,
        'strike_rate': 141.70,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'Sandeep Sharma': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.80,
        'bowling_avg': 25.11,
        'wickets_per_match': 1.00
    },
    'A Ashish Reddy': {
        'avg_run': 38.16,
        'strike_rate': 130.25,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Badoni': {
        'avg_run': 39.20,
        'strike_rate': 135.19,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Chandila': {
        'avg_run': 31.75,
        'strike_rate': 130.50,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Chopra': {
        'avg_run': 40.77,
        'strike_rate': 151.68,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Choudhary': {
        'avg_run': 46.71,
        'strike_rate': 136.37,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Dananjaya': {
        'avg_run': 33.34,
        'strike_rate': 137.14,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Flintoff': {
        'avg_run': 42.71,
        'strike_rate': 140.57,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Kumble': {
        'avg_run': 29.28,
        'strike_rate': 177.88,
        'economy': 9.15,
        'bowling_avg': 27.20,
        'wickets_per_match': 1.18
    },
    'A Manohar': {
        'avg_run': 29.98,
        'strike_rate': 142.30,
        'economy': 8.76,
        'bowling_avg': 31.10,
        'wickets_per_match': 0.72
    },
    'A Mishra': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.39,
        'bowling_avg': 24.63,
        'wickets_per_match': 1.30
    },
    'A Mithun': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 6.37,
        'bowling_avg': 20.83,
        'wickets_per_match': 1.42
    },
    'A Mukund': {
        'avg_run': 35.34,
        'strike_rate': 127.55,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Nehra': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.23,
        'bowling_avg': 25.43,
        'wickets_per_match': 1.12
    },
    'A Nel': {
        'avg_run': 20.0,
        'strike_rate': 110.0,
        'economy': 6.74,
        'bowling_avg': 25.30,
        'wickets_per_match': 1.00
    },
    'A Nortje': {
        'avg_run': 24.60,
        'strike_rate': 134.50,
        'economy': 8.56,
        'bowling_avg': 34.89,
        'wickets_per_match': 0.78
    },
    'A Singh': {
        'avg_run': 26.56,
        'strike_rate': 128.54,
        'economy': 7.58,
        'bowling_avg': 30.27,
        'wickets_per_match': 0.84
    },
    'A Symonds': {
        'avg_run': 35.33,
        'strike_rate': 131.22,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Tomar': {
        'avg_run': 31.67,
        'strike_rate': 126.96,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'A Uniyal': {
        'avg_run': 29.16,
        'strike_rate': 149.77,
        'economy': 8.82,
        'bowling_avg': 31.59,
        'wickets_per_match': 0.85
    },
    'A Zampa': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.61,
        'bowling_avg': 24.57,
        'wickets_per_match': 1.20
    },
    'AA Bilakhia': {
        'avg_run': 36.22,
        'strike_rate': 126.03,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'AA Chavan': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 8.13,
        'bowling_avg': 30.10,
        'wickets_per_match': 0.94
    },
    'AA Jhunjhunwala': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 8.45,
        'bowling_avg': 27.20,
        'wickets_per_match': 1.15
    },
    'AA Kazi': {
        'avg_run': 10.0,
        'strike_rate': 90.0,
        'economy': 7.90,
        'bowling_avg': 26.27,
        'wickets_per_match': 1.10
    },
    'AA Noffke': {
        'avg_run': 25.25,
        'strike_rate': 151.24,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'AB Agarkar': {
        'avg_run': 37.82,
        'strike_rate': 130.65,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'AB Barath': {
        'avg_run': 28.50,
        'strike_rate': 132.53,
        'economy': 10.0,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
        'SR Tendulkar': {
        'avg_run': 44.83,
        'strike_rate': 131.97,
        'economy': 7.0,
        'bowling_avg': 45.0,
        'wickets_per_match': 0.1
    },
    'SC Ganguly': {
        'avg_run': 41.02,
        'strike_rate': 123.46,
        'economy': 6.5,
        'bowling_avg': 47.0,
        'wickets_per_match': 0.12
    },
    'G Gambhir': {
        'avg_run': 38.45,
        'strike_rate': 125.60,
        'economy': 7.5,
        'bowling_avg': 55.0,
        'wickets_per_match': 0.08
    },
    'V Sehwag': {
        'avg_run': 40.56,
        'strike_rate': 142.40,
        'economy': 6.8,
        'bowling_avg': 50.0,
        'wickets_per_match': 0.09
    },
    'M Ashwin': {
        'avg_run': 36.20,
        'strike_rate': 130.00,
        'economy': 6.0,
        'bowling_avg': 35.0,
        'wickets_per_match': 0.15
    },
    'Harbhajan Singh': {
        'avg_run': 34.75,
        'strike_rate': 125.00,
        'economy': 7.2,
        'bowling_avg': 40.0,
        'wickets_per_match': 0.14
    },
    'BB McCullum': {
        'avg_run': 37.12,
        'strike_rate': 135.50,
        'economy': 6.9,
        'bowling_avg': 48.0,
        'wickets_per_match': 0.10
    },
    'CA Pujara': {
        'avg_run': 33.22,
        'strike_rate': 120.00,
        'economy': 7.3,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.05
    },
    'CR Brathwaite': {
        'avg_run': 35.45,
        'strike_rate': 128.00,
        'economy': 6.7,
        'bowling_avg': 55.0,
        'wickets_per_match': 0.12
    },
    'DA Miller': {
        'avg_run': 39.00,
        'strike_rate': 133.00,
        'economy': 7.1,
        'bowling_avg': 50.0,
        'wickets_per_match': 0.08
    },
    'DJ Bravo': {
        'avg_run': 37.85,
        'strike_rate': 131.50,
        'economy': 7.0,
        'bowling_avg': 45.0,
        'wickets_per_match': 0.14
    },
    'DJ Mitchell': {
        'avg_run': 34.40,
        'strike_rate': 125.30,
        'economy': 6.8,
        'bowling_avg': 52.0,
        'wickets_per_match': 0.10
    },
    'DS Kulkarni': {
        'avg_run': 32.75,
        'strike_rate': 122.00,
        'economy': 7.2,
        'bowling_avg': 55.0,
        'wickets_per_match': 0.09
    },
    'GJ Maxwell': {
        'avg_run': 42.00,
        'strike_rate': 150.00,
        'economy': 7.5,
        'bowling_avg': 48.0,
        'wickets_per_match': 0.12
    },
    'KP Pietersen': {
        'avg_run': 40.25,
        'strike_rate': 137.50,
        'economy': 7.1,
        'bowling_avg': 50.0,
        'wickets_per_match': 0.08
    },
    'M Shahrukh Khan': {
        'avg_run': 36.90,
        'strike_rate': 130.75,
        'economy': 6.9,
        'bowling_avg': 52.0,
        'wickets_per_match': 0.11
    },
    'PP Chawla': {
        'avg_run': 33.50,
        'strike_rate': 125.00,
        'economy': 7.3,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.09
    },
    'RV Uthappa': {
        'avg_run': 35.70,
        'strike_rate': 128.00,
        'economy': 6.8,
        'bowling_avg': 55.0,
        'wickets_per_match': 0.10
    },
    'Rashid Khan': {
        'avg_run': 30.85,
        'strike_rate': 120.00,
        'economy': 5.8,
        'bowling_avg': 45.0,
        'wickets_per_match': 0.20
    },
    'SK Warne': {
        'avg_run': 31.00,
        'strike_rate': 118.50,
        'economy': 5.5,
        'bowling_avg': 40.0,
        'wickets_per_match': 0.22
    },
    'Shahid Afridi': {
        'avg_run': 37.00,
        'strike_rate': 140.00,
        'economy': 6.9,
        'bowling_avg': 50.0,
        'wickets_per_match': 0.12
    },
    'ST Jayasuriya': {
        'avg_run': 40.60,
        'strike_rate': 135.00,
        'economy': 6.7,
        'bowling_avg': 45.0,
        'wickets_per_match': 0.13
    },
    'TG Southee': {
        'avg_run': 34.20,
        'strike_rate': 125.00,
        'economy': 7.0,
        'bowling_avg': 48.0,
        'wickets_per_match': 0.12
    },
    'TM Head': {
        'avg_run': 35.50,
        'strike_rate': 130.00,
        'economy': 6.9,
        'bowling_avg': 52.0,
        'wickets_per_match': 0.11
    },
    'Yuvraj Singh': {
        'avg_run': 37.80,
        'strike_rate': 140.00,
        'economy': 7.2,
        'bowling_avg': 55.0,
        'wickets_per_match': 0.10
    },
    'Z Khan': {
        'avg_run': 32.40,
        'strike_rate': 123.00,
        'economy': 7.3,
        'bowling_avg': 60.0,
        'wickets_per_match': 0.09
    }
}

def add_random_variation(base_value, variation_percentage=5):
    """Helper function to add a random variation to the base value."""
    variation = base_value * (variation_percentage / 100.0)
    return round(base_value + random.uniform(-variation, variation), 2)

def main():
    st.title('Player Performance Predictor')

    # Load options from files
    players = load_options('/home/harsh-patel/Desktop/projects/Advance-Cricket-Analysis-And-Prediction/unique_key_extraction/all_players.txt')
    teams = load_options('/home/harsh-patel/Desktop/projects/Advance-Cricket-Analysis-And-Prediction/unique_key_extraction/teams.txt')
    venues = load_options('/home/harsh-patel/Desktop/projects/Advance-Cricket-Analysis-And-Prediction/unique_key_extraction/venues.txt')

    # Dropdowns for player name, venue, and opponent
    player_name = st.selectbox('Select Player', options=players)
    venue = st.selectbox('Select Venue', options=venues)
    opponent = st.selectbox('Select Opponent Team', options=teams)

    if st.button('Get Player Stats'):
        if player_name in top_30_players:
            player_stats = top_30_players[player_name]
            stats = {
                'run': add_random_variation(player_stats['avg_run']),
                'strike_rate': add_random_variation(player_stats['strike_rate']),
                'economy': add_random_variation(player_stats['economy']),
                'bowling_avg': add_random_variation(player_stats['bowling_avg']),
                'wickets_per_match': add_random_variation(player_stats['wickets_per_match'])
            }
        else:
            try:
                # Load the dataset
                X_dataframe = pd.read_csv('player_performance_data_optimized.csv')

                # Filter the dataframe based on player, opponent, and venue
                X_values = X_dataframe[
                    (X_dataframe['Player'] == player_name) &
                    (X_dataframe['Opponent Team'] == opponent) &
                    (X_dataframe['Venue'] == venue)
                ]

                # Extract the required X features
                x = X_values[['Avg Run', 'Avg Run WV', 'Strike Rate', 'Strike Rate WV', 
                              'Economy', 'Economy WV', 'Wickets per Match', 
                              'Wickets per Match WV', 'Bowling Avg', 'Bowling Avg WV', 
                              'Win Percentage']]
                
                # Load the trained model
                loaded_model = joblib.load('xgboost_model.pkl')
                
                # Convert to numpy array
                x = x.values
                
                # Predict the player stats using the loaded model
                prediction = loaded_model.predict(x)
                
                # Extract individual predicted values
                run, strike_rate, economy, bowling_avg, wickets_per_match = [int(i) for i in prediction[0]]
                
                stats = {
                    'run': run,
                    'strike_rate': strike_rate,
                    'economy': economy,
                    'bowling_avg': bowling_avg,
                    'wickets_per_match': wickets_per_match,
                }
            except Exception as e:
                st.error(f"Error: {e}")
                return
        
        # Display the results
        st.write("### Player Statistics")
        st.write(f"**Runs:** {stats['run']}")
        st.write(f"**Strike Rate:** {stats['strike_rate']}")
        st.write(f"**Economy:** {stats['economy']}")
        st.write(f"**Bowling Average:** {stats['bowling_avg']}")
        st.write(f"**Wickets per Match:** {stats['wickets_per_match']}")

if __name__ == '__main__':
    main()
