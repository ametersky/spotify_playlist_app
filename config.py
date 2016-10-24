APP_SESSION_KEY = 'the horse is a neat color'

CLIENT_ID = '9b1ef622d575468cb033ce88d7d8584f'
CLIENT_SECRET = 'f04d2e1d7d99448687b2bc16276238f4'

# Spotify URLS
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
SPOTIFY_ME_URL = 'https://api.spotify.com/v1/me'
API_VERSION = 'v1'
SPOTIFY_API_URL = '{}/{}'.format(SPOTIFY_API_BASE_URL, API_VERSION)


# Server-side Parameters
PORT = int(os.environ.get("PORT", 5000))
CLIENT_SIDE_URL = 'https://spotify-flask-app.herokuapp.com'
REDIRECT_URI = '{}:{}/callback/q'.format(CLIENT_SIDE_URL, PORT)
SCOPE = 'playlist-modify-public playlist-modify-private'

AUTH_QUERY_PARAMETERS = {
    'response_type': 'code',
    'redirect_uri': REDIRECT_URI,
    'scope': SCOPE,
    'client_id': CLIENT_ID
}
