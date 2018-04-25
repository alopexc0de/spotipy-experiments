#!/bin/bash

# Client ID and Secret can be found at:
# https://beta.developer.spotify.com/dashboard/applications/

# Activate Python Virtualenv
# Ensure that you have previously set this up with `virtualenv venv`
# Select only one of the below
source venv/bin/activate  # For Linux/macOS/*nix Users
# source venv/Scripts/activate  # For Windows Users

# API Auth Stuffs
export SPOTIPY_CLIENT_ID='YOUR_CLIENT_ID_HERE'
export SPOTIPY_CLIENT_SECRET='YOUR_CLIENT_SECRET_HERE'
# Response from Spotify API after authorization
# Not sure if this actually requires a local web server
export SPOTIPY_REDIRECT_URI='http://localhost/'
