#!/usr/bin/env python
# Writes the now playing track to a text file
# License: MIT
# Copyright (c) 2018 c0de <c0defox.es>

# Edit "set_env.sh" to configure your API key
# $ virtualenv venv
# $ ./set_env.sh
# $ pip install -r requirements.txt

import sys
import time

import spotipy
import spotipy.util as util
from spotipy.client import SpotifyException

start_time = time.time()

if len(sys.argv) > 2:
    username = sys.argv[1]
    outfile = sys.argv[2]
else:
    print "Usage: %s username outfile" % sys.argv[0]
    sys.exit()

def get_now_playing(sp):
    # This should be sp.currently_playing(), but somehow does not work...
    # So I used its return: https://github.com/plamere/spotipy/blob/master/spotipy/client.py#L899

    try:
        # Get the currently playing track and artist
        np = sp._get("me/player/currently-playing", market=None)
        # Take a look at the other goodies that gets returned here for future stuff
        return "%s by: %s" % (np['item']['name'], np['item']['artists'][0]['name'])
    except TypeError:
        return "Nothing is playing"

def authorize_api(username, scope=None):
    if not scope:
        # Authorization Scope, can possibly be a dict?
        scope = 'user-read-currently-playing'

    print "[%.2fs] Authorizing %s with this auth scope: %s" % \
            (time.time()-start_time, username, scope)

    # The access token appears to expire around 2000ish seconds of use. 
    # Rerunning this and retrieving the callback url (with new token) will allow the script to continue
    
    # Use HttpSimpleServer based auth if available (using c0de's spotipy for example)
    if hasattr(util, 'obtain_token_localhost'):
        token = util.obtain_token_localhost(username, scope)
    else:
        token = util.prompt_for_user_token(username, scope)

    if token:
        # Authorize with the API
        return spotipy.Spotify(auth=token)
    else:
        print "[%.2fs] Unable to authorize %s - Did they approve the oauth login?" % \
                (time.time()-start_time, username)
        sys.exit()

sp = authorize_api(username)

# Main loop
while True:
    try:
        np = get_now_playing(sp)
    except SpotifyException as e:
        if e.http_status == '401' and e.code == '-1':  # Unauthorized and Expired access token
            print "[%.2fs] Access Token for %s Expired, reaquiring..." % \
                    (time.time()-start_time, username)
            # Reauth and get the next now playing
            sp = authorize_api(username)
            continue
        else:
            raise Exception(e)

    try:
        with open(outfile, 'w') as output:
            output.write(np)
            print "[%.2fs] %s" % (time.time()-start_time, np)
            output.close()
    except:
        print "[%.2fs] Unable to open %s" % (time.time()-start_time, outfile)
        sys.exit()
    
    # Wait approximately 10s before checking again
    time.sleep(10.0 - ((time.time() - start_time) % 10.0))
