#!/usr/bin/env python
# Writes the now playing track to a text file
# License: MIT
# Copyright (c) 2018 c0de <c0defox.es>

import sys
import time
import json

import spotipy
import spotipy.util as util

if len(sys.argv) > 2:
    username = sys.argv[1]
    outfile = sys.argv[2]
else:
    print "Usage: %s username outfile" % sys.argv[0]
    sys.exit()

# Authorization Scope, can possibly be a dict?
scope = 'user-top-read'
sp = util.authorize_api(username, scope, 'server')
tt = json.dumps(sp.current_user_top_tracks())

with open(outfile+'.json', 'w') as output:
    output.write(tt)
    output.close()