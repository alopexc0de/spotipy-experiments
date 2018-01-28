#!/usr/bin/env python
# Writes the now playing track to a text file
# License: MIT
# Copyright (c) 2018 c0de <c0defox.es>

import spotipy
import spotipy.util as util
import time
import sys
import os

start_time = time.time()

if len(sys.argv) > 2:
    username = sys.argv[1]
    outfile = sys.argv[2]
else:
    print "Usage: %s username outfile" % sys.argv[0]
    sys.exit()

def get_now_playing(sp):
    # This should be sp.currently_playing(), but somehow does not work...
    # So I its return: https://github.com/plamere/spotipy/blob/master/spotipy/client.py#L899
    # Get the currently playing track and artist
    np = sp._get("me/player/currently-playing", market=None)
    return "%s by: %s" % (np['item']['name'], np['item']['artists'][0]['name'])

# Authorization Scope, can possibly be a dict?
scope = 'user-read-currently-playing'

# User Auth-Token - Achieved by running a webserver on localhost (might not be needed) as we just paste the URL here
token = util.prompt_for_user_token(username, scope)

if token:
    # Authorize with the API
    sp = spotipy.Spotify(auth=token)

    while True:
        np = get_now_playing(sp)

        try:
            with open(outfile, 'w') as output:
                output.write(np)
                print "[%.2fs] %s" % (time.time()-start_time, np)
                output.close()
        except:
            print "[%.2fs] Unable to open %s" % (time.time()-start_time, outfile)
            sys.exit()
        
        # Wait 1 minute before checking again
        time.sleep(60.0 - ((time.time() - start_time) % 60.0))
else:
    print "Can't get a token for %s" % username
    sys.exit()
