# Spotify Music Player Application

## Overview
This is an interactive desktop application for controlling and displaying Spotify song information.
The application uses Tkinter for the graphical user interface (GUI) and Spotipy for interacting with the Spotify API.
It provides features to control playback, display song information, and adjust volume. Additionally, it includes
a slider that allows users to seek to any part of the currently playing song.



## Features
- **Playback Controls**: Play, Pause, Rewind, Forward.
- **Volume Adjustment**: Increase or decrease the volume.
- **Song Information Display**: Shows the currently playing song's title and artist.
- **Seek Slider**: Allows users to skip to any point in the song.
- **UI Fade Effect**: The interface fades out when not interacted with and reappears when hovered over or activated by a shortcut.

## Requirements
- Python 3.7 or higher
- Spotipy library
- Tkinter library (usually included with Python installation)

## Installation
1. **Clone the repository**:
		git clone https://github.com/yourusername/spotify-music-player.git
	Navigate to the Project Directory:
		cd spotify-music-player


2. Create and Activate a Virtual Environment (Recommended):
		python -m venv venv
		source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. Install Required Dependencies
		pip install -r requirements.txt
Configure Spotipy:
	- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
	- Create a new application to get your `CLIENT_ID` and `CLIENT_SECRET`.
	- Add your redirect URI (e.g., `http://localhost:8888/callback`) to the application settings.


4. **Set up environment variables**:
Create a file named `.env` in the project directory and add the following lines:
	SPOTIPY_CLIENT_ID = your_client_id
	SPOTIPY_CLIENT_SECRET = your_client_secret
	SPOTIPY_REDIRECT_URI = http://localhost:8888/callback
	

**Interface**:
- The application window will appear in the top-left corner of the screen.
- Use the buttons to control playback (Play, Pause, Rewind, Forward).
- Adjust the volume using the volume control.
- The currently playing song's title and artist will be displayed.
- Use the slider to seek to any point in the song.

**UI Interaction**:
- The interface will fade out after a period of inactivity.
- Hover over or activate the application window to make it reappear.
- The UI remains visible while the mouse is hovering over it.

## Code Structure
- `spotify_player.py`: The main script containing the application logic and UI code.
- `spotipy_utils.py`: Helper functions for interacting with the Spotify API.
- `styles.css`: CSS file for styling the Tkinter application (if applicable).

## Troubleshooting
- **Application not starting**: Ensure all required libraries are installed and environment variables are correctly set.
- **Spotify authentication issues**: Verify your Spotify API credentials and redirect URI.

## Contribution
Feel free to contribute to this project by submitting pull requests or opening issues. 

## License
This project is licensed under the MIT License.

## Contact
For any questions or support, please contact seyedhamidjavaheri@gmail.com.


