#!/usr/bin/env python
# Writes the user's playlists to json files
# License: MIT
# Copyright (c) 2018 c0de <c0defox.es>

import sys
import time
import json

import spotipy
import spotipy.util as util
from spotipy.exceptions import SpotifyException

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "usage: python save_all_playlist.py [username]"
    sys.exit()

start_time = time.time()

# Permissions to request from the user and perform action with perms
scope = 'user-library-read playlist-read-private playlist-read-collaborative'
sp = util.authorize_api(username, scope, 'server')
playlists = sp.current_user_playlists()

limit = 100
exported = 0

# This will export all of your playlists, if you wish to not include certain ones,
# they should be added to playlist_blacklist
playlist_ids = {}

playlist_blacklist = [
    'Liked from Radio',
    'Starred'
]

# Get the user's playlists
for playlist in playlists['items']:
    id = playlist['id']
    name = playlist['name']
    total = playlist['tracks']['total']

    if name in playlist_blacklist:
        print "[%.2fs] Not exporting %s" % (time.time()-start_time, name)
        continue

    playlist_ids[id] = [total, name]

    print "[%.2fs] Exporting %s tracks from %s" % (time.time()-start_time, total, name)

# Export all tracks from the user's playlists
for playlist in playlist_ids:
    id = playlist
    total = playlist_ids[playlist][0]
    name = playlist_ids[playlist][1]
    filename = 'playlists/%s.json' % name
    limit_count = 0

    with open(filename, "w") as output:
        print "[%.2fs] Saving playlist %s to %s" % (time.time()-start_time, id, filename)

        if total > limit:
            print "[%.2fs] playlist has %s more songs than the limit" % (time.time()-start_time, total-limit)
            
            while total > 0:
                try:
                    tracks = json.dumps(sp.user_playlist_tracks(username, playlist,
                            limit=limit, offset=limit*limit_count))
                except SpotifyException as e:
                    if e.http_status == '404' and e.code == '-1':
                        # we don't have the ability to download that playlist, or it doesn't exist
                        print "playlist %s returned a 404 error" % (time.time()-start_time, name)
                        pass
                limit_count += 1
                total -= limit
                # This will go negative when there are less than 100 items in the total
                print "[%.2fs]-[%s] Downloading %s tracks with %s left" % (time.time()-start_time, limit_count, limit, total)
        else:
            try:
                tracks = json.dumps(sp.user_playlist_tracks(username, playlist))
            except SpotifyException as e:
                if e.http_status == '404' and e.code == '-1':
                    # we don't have permission to download that playlist, or it doesn't exist
                    print "[%.2fs] playlist %s returned a 404 error" % (time.time()-start_time, playlist)
                    pass
        if tracks:
            exported += 1

        output.write(tracks)
        output.close()
    
    # Wait approximately 5s before checking again
    print "[%.2fs] waiting 5s..." % (time.time()-start_time)
    time.sleep(5.0 - ((time.time() - start_time) % 5.0))
print "[%.2fs] %s/%s playlists have been exported to json format" % (time.time()-start_time, exported, len(playlist_ids))