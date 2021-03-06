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
from spotipy.exceptions import SpotifyException

start_time = time.time()

if len(sys.argv) > 2:
    username = sys.argv[1]
    outfile = sys.argv[2]
else:
    print "Usage: %s username outfile" % sys.argv[0]
    sys.exit()

def get_now_playing(sp):
    try:
        # Get the currently playing track and artist
        np = sp.currently_playing()
        # Take a look at the other goodies that gets returned here for future stuff
        return "%s by: %s" % (np['item']['name'], np['item']['artists'][0]['name'])
    except TypeError:
        return "Nothing is playing"

# Authorization Scope, can possibly be a dict?
scope = 'user-read-currently-playing'
sp = util.authorize_api(username, scope, 'server')

# Main loop
while True:
    try:
        np = get_now_playing(sp)
    except SpotifyException as e:
        if e.http_status == '401' and e.code == '-1':  # Unauthorized and Expired access token
            print "[%.2fs] Access Token for %s Expired, reaquiring..." % \
                    (time.time()-start_time, username)
            # Reauth and get the next now playing
            sp = util.authorize_api(username, scope, 'server')
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
