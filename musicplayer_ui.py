import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_player import client_id, client_secret, redirect_uri

#----------------------------------------------------------------------------------------------------------------------#
# This block of code is used for updating the song info on the display
def update_song_info():
    current_track = sp.current_playback()
    if current_track is not None and current_track['item'] is not None:
        song_title = current_track['item']['name']
        artists = ", ".join([artist['name'] for artist in current_track['item']['artists']])
        title_label.config(text = song_title)
        artist_label.config(text = artists)
    else:
        title_label.config(text = "No song playing")
        artist_label.config(text = "")

    # Repeat every second (1000ms)
    root.after(1000, update_song_info)

#----------------------------------------------------------------------------------------------------------------------#

# This block is in charge of toggling the play/pause functions
def toggle_play_pause():
    current_track = sp.current_playback()
    if current_track is not None and current_track['is_playing']:
        sp.pause_playback()
        play_pause_button.config(text = "Play")
    else:
        sp.start_playback()
        play_pause_button.config(text = "Pause")

    # Updates the text to update whether it's playing or paused
def update_play_pause_button():
    current_track = sp.current_playback()
    if current_track is not None and current_track['is_playing']:
        play_pause_button.config(text = "Pause")
    else:
        play_pause_button.config(text = "Play")

    # Repeat every second
    root.after(1000, update_play_pause_button)

#----------------------------------------------------------------------------------------------------------------------#

# Defining the Rewind and Forward Options
def handle_rewind():
    current_track = sp.current_playback()['progress_ms'] / 1000 # This line gets the current position in the song
    if current_track <= 3: # Goes back to the previous song
        sp.previous_track()
    else:
        sp.seek_track(0) # Restarts the song back to 0:00

def rewind_10_seconds():
    current_position = sp.current_playback()['progress_ms'] / 1000 # This line gets the current position in the song
    track_duration = sp.current_playback()['item']['duration_ms'] / 1000 # Gets the track's duration, in seconds
    new_position = max(current_position - 10, 0) # Makes sure the new position is within the track duration
    sp.seek_track(new_position * 1000) # Seek to new position

def forward_10_seconds():
    current_position = sp.current_playback()['progress_ms'] / 1000 # This line gets the current position in the song
    track_duration = sp.current_playback()['item']['duration_ms'] / 1000 # Gets the track's duration, in seconds
    new_position = min(current_position + 10, track_duration) # Makes sure the new position is within the track duration
    sp.seek_track(new_position * 1000) # Seek to new position

def on_rewind_button_press(event):
    global rewind_pressed
    rewind_pressed = True
    check_rewind()

def on_rewind_button_release(event):
    global rewind_pressed
    rewind_pressed = False

def on_forward_button_press(event):
    global forward_pressed
    forward_pressed = True
    check_forward()

def on_forward_button_release(event):
    global forward_pressed
    forward_pressed = False

def check_rewind():
    if rewind_pressed:
        rewind_10_seconds()
        root.after(500, check_rewind)  # Call this function every 500 milliseconds

def check_forward():
    if forward_pressed:
        forward_10_seconds()
        root.after(500, check_forward)  # Call this function every 500 milliseconds

#----------------------------------------------------------------------------------------------------------------------#

# Spotify Authentication
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = client_id,
                                               client_secret = client_secret,
                                               redirect_uri = redirect_uri,
                                               scope = 'user-read-playback-state'))

#----------------------------------------------------------------------------------------------------------------------#

# Create the main window
root = tk.Tk()
root.geometry('300x100+2240+10')
root.title("Spotify Music Player")



# Create labels to display the song title and artist
title_label = tk.Label(root, text = "Loading...", font = ("Helvetica", 12))
title_label.grid(row = 0, column = 1, columnspan = 3, pady = 10)
artist_label = tk.Label(root, text = "", font = ("Helvetica", 10))
artist_label.grid(row = 1, column = 1, columnspan = 3)

#----------------------------------------------------------------------------------------------------------------------#

# Create buttons
rewind_button = tk.Button(root, text = "Rewind", command = handle_rewind, font = ("Helvetica", 10))
rewind_button.grid(row = 2, column = 0, padx = 10)
#----------------------------------------------------------------------------------------------------------------------#
play_pause_button = tk.Button(root, text = "Play", command = toggle_play_pause, font = ("Helvetica", 10))
play_pause_button.grid(row = 2, column = 1)
#----------------------------------------------------------------------------------------------------------------------#
forward_button = tk.Button(root, text = "Forward", command = lambda: sp.next_track(), font = ("Helvetica", 10))
forward_button.grid(row = 2, column = 2, padx = 10)
#----------------------------------------------------------------------------------------------------------------------#
rewind_button.bind("<ButtonPress-1>", on_rewind_button_press)
rewind_button.bind("<ButtonRelease-1>", on_rewind_button_release)
forward_button.bind("<ButtonPress-1>", on_forward_button_press)
forward_button.bind("<ButtonRelease-1>", on_forward_button_release)





# Start updating the song info
update_song_info()
update_play_pause_button()
rewind_pressed = False
forward_pressed = False

# Run the application
root.mainloop()

