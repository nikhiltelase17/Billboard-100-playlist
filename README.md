# Billboard 100 Playlist Automation with Python

## Overview

This Python script automates the creation of a personalized Spotify playlist based on the Billboard 100 chart for a specific date. The script uses the Spotipy library to interact with the Spotify API and a custom song list scraper to extract Billboard 100 data.

## Features

1. **User Input:** The script prompts the user for a specific date (in the format YYYY-MM-DD) to travel back in time to their favorite musical era.

2. **Billboard 100 Scraping:** It scrapes the Billboard 100 chart for the specified date, extracting the top 100 songs.

3. **Spotify Song Search:** The script searches for corresponding songs on Spotify based on title and year.

4. **Playlist Creation:** It creates a new Spotify playlist named after the specified date and "Billboard" for easy reference.

5. **Playlist Population:** All the found songs are added to the created playlist, providing a seamless listening experience.

## How to Use

### Prerequisites

- Python 3.x installed on your machine.
- Spotipy library installed (`pip install spotipy`).
- Spotify Developer account to obtain API credentials.

### Setup

1. Clone the repository: 
   ```bash
   git clonehttps://github.com/nikhiltelase17/Billboard-100-playlist/main.py.git
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain Spotify API credentials:
   - Create a Spotify Developer account and create a new app.
   - Note down the `Client ID` and `Client Secret`.

4. Create a `.env` file in the project root and add your Spotify API credentials:
   ```env
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   ```

### Usage

Run the script:
```bash
python main.py
```

Follow the on-screen instructions to enter the desired date.

## Disclaimer

This code requires additional libraries and proper authentication. Always adhere to Spotify's API terms and conditions.

## Contributing

Feel free to contribute to the project by opening issues or pull requests. Your feedback and ideas are highly appreciated!

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the Spotipy library and the contributors behind it.
- Inspired by the love for music and the desire to relive past Billboard 100 charts.

Enjoy your personalized Billboard 100 playlist! 🎵
