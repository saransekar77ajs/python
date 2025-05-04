import pandas as pd
import requests
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

# Retrieve API key
api_key = os.getenv("TMDB_API_KEY")
if not api_key:
    raise ValueError("API key not found! Please set TMDB_API_KEY in .env file.")

# Base URL for the API request
base_url = "https://api.themoviedb.org/3/movie/top_rated"
total_pages = 500  # Adjust as needed

# Initialize a session for optimized HTTP requests
session = requests.Session()
session.headers.update({"accept": "application/json"})

# Initialize an empty list to store results
all_movies = []

# Loop through each page and fetch data
for page in range(1, total_pages + 1):
    params = {"api_key": api_key, "language": "en-US", "page": page}
    response = session.get(base_url, params=params)

    # Ensure the request was successful
    if response.status_code == 200:
        data = response.json()
        all_movies.extend(data["results"])
    else:
        print(f"Error fetching page {page}: {response.status_code}")

# Convert the collected data into a DataFrame
df = pd.DataFrame(all_movies)[
    [
        "id",
        "title",
        "release_date",
        "overview",
        "popularity",
        "vote_average",
        "vote_count",
    ]
]

# Display the first few rows
print(df.head())


# Save to a CSV file
df.to_csv(
    "C:\\Users\\saran\\OneDrive\\Desktop\\Python FullStack\\Assignments\\data\\top_rated_movies_final.csv",
    index=False,
)
print(f"Data saved to: {output_path}")
