import os
from flask import Flask, redirect, request, url_for
from requests_oauthlib import OAuth2Session

app = Flask(__name__)

# Fitbit OAuth 2.0 credentials from the details you provided
CLIENT_ID = '23PRZ4'
CLIENT_SECRET = 'cfd1f3cdbf8fa149071a2995de0723b6'
REDIRECT_URI = 'https://stepss.online/signin-fitbit'

# Fitbit OAuth 2.0 endpoints
AUTHORIZATION_URL = 'https://www.fitbit.com/oauth2/authorize'
TOKEN_URL = 'https://api.fitbit.com/oauth2/token'

# Define the required scopes for the OAuth flow
SCOPES = ['activity']

# Create an OAuth2 session
oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPES)

@app.route('/')
def index():
    """Homepage route."""
    return 'Welcome to Fitbit OAuth 2.0 integration!'

@app.route('/login')
def login():
    """Redirect user to Fitbit's authorization URL."""
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_URL)
    return redirect(authorization_url)

@app.route('/signin-fitbit')
def signin_fitbit():
    """Handle the redirect from Fitbit after user grants access."""
    # Fetch the access and refresh tokens using the authorization code sent by Fitbit
    token = oauth.fetch_token(TOKEN_URL, authorization_response=request.url,
                              client_secret=CLIENT_SECRET)
    
    # Extract the access and refresh tokens
    access_token = token['access_token']
    refresh_token = token['refresh_token']

    # For security, you can store the tokens in a session or database
    # For now, we're displaying them on the screen (this is for testing purposes only)
    return f"Access token: {access_token}<br>Refresh token: {refresh_token}"

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)
