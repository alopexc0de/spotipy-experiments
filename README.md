# Spotify API Experiments

This is a collection of experimentations with the Spotipy python library.
All of these scripts will request an auth token for a particular user (username arg) upon startup
From my experimentation so far, this will remmeber that the app was previously authorized for whatever "authorization scope" was approved by the user at the oauth screen

save_now_playing.py - This script will poll for the user's now playing track every 10s and update a text file
get_user_auth.py - "Hello World" from the docs, this shows how to authorize using env
show_all_playlist.py - Unlike the name suggests, I did not see all my playlists. This could be an auth scope issue however

## To get started:
* Create an app on Spotify's Developer console - https://beta.developer.spotify.com
* Clone this repository
* Ensure that you have "python-pip", and "python-virtualenv" installed
* Run `virtualenv venv` to create a new python environment
* Edit "set_env.sh" to configure your API ID, Secret, and redirect using the information from your previously created app
* Configure your environment by running `set_env.sh`
* Run `pip install -r requirements.txt` to install the required dependencies
* `git clone https://github.com/alopexc0de/spotipy.git` into venv/lib/python2.7/site-packages/spotipy
    * If using "server" from util.authorize_api(), include a port higher than 1024 inside `SPOTIPY_REDIRECT_URI`. For example: "http://localhost:8000/"
* Run any of the scripts to use them

## License: MIT
Copyright (c) 2014 Paul Lamere - https://github.com/plamere/spotipy
Copyright (c) 2018 c0de <c0defox.es, gama.io>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.