#!/usr/bin/python3

import sys
import requests

def get_movie_characters(movie_id):
    # Define the base URL of the Star Wars API (SWAPI)
    base_url = "https://swapi.dev/api/films/"
    
    # Build the URL for the given movie ID (note: IDs are 1-indexed, not 0-indexed)
    movie_url = f"{base_url}{movie_id}/"
    
    try:
        # Make the API request to fetch movie details
        response = requests.get(movie_url)
        response.raise_for_status()  # Raise an exception for bad HTTP responses (4xx, 5xx)
        
        # Parse the JSON response
        movie_data = response.json()
        
        # Extract the character URLs
        character_urls = movie_data.get("characters", [])
        
        # Print each character name
        for character_url in character_urls:
            character_response = requests.get(character_url)
            character_response.raise_for_status()  # Check for HTTP errors
            
            character_data = character_response.json()
            print(character_data["name"])
    
    except requests.exceptions.RequestException as e:
        # Handle any errors (network issues, invalid responses, etc.)
        print(f"Error: {e}")
        sys.exit(1)

def main():
    # Check if a movie ID is passed as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <movie_id>")
        sys.exit(1)
    
    try:
        # Get the movie ID from the command-line argument
        movie_id = int(sys.argv[1])
        
        # Validate movie ID (1-6)
        if movie_id < 1 or movie_id > 6:
            print("Invalid movie ID. Please provide a valid movie ID between 1 and 6.")
            sys.exit(1)
        
        # Call the function to get and print characters for the movie
        get_movie_characters(movie_id)
    
    except ValueError:
        print("Please provide a valid integer for the movie ID.")
        sys.exit(1)

if __name__ == "__main__":
    main()

