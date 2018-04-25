import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

sp = util.authorize_api(username, scope, 'server')

results = sp.current_user_saved_tracks()
for item in results['items']:
    track = item['track']
    print track['name'] + ' - ' + track['artists'][0]['name']