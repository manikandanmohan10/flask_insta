# import os
# import requests
# from urllib.parse import parse_qs


# """
# Define the GITHUB_ID and GITHUB_SECRET environment variables
# along with the endpoints.
# """
# CLIENT_ID = os.getenv("GITHUB_ID", '681723bfcd11512fcf84')
# CLIENT_SECRET = os.getenv("GITHUB_SECRET", 'ca03513033df46ae40c3176586cc65dcf2593201')
# AUTHORIZATION_ENDPOINT = f"https://github.com/login/oauth/authorize?response_type=code&client_id={os.getenv('GITHUB_ID', '681723bfcd11512fcf84')}"
# TOKEN_ENDPOINT = "https://github.com/login/oauth/access_token"
# USER_ENDPOINT = "https://api.github.com/user"


# """
# 1. Log in via the browser using the 'Authorization URL' outputted in the terminal.
#    (If you're already logged in to GitHub, either log out or test in an incognito/private browser window.)
# 2. Once logged in, the page will redirect. Grab the code from the redirect URL.
# 3. Paste the code in the terminal.
# """
# print(f"Authorization URL: {AUTHORIZATION_ENDPOINT}")
# print(os.getenv('GITHUB_ID'))
# code = input("Enter the code: ")


# """
# Using the authorization code, we can request an access token.
# """
# # Once we get the code, we sent the code to the access token
# # endpoint(along with id and secret). The response contains
# # the access_token and we parse is using parse_qs
# res = requests.post(
#     TOKEN_ENDPOINT,
#     data=dict(
#         client_id=os.getenv("GITHUB_ID", '681723bfcd11512fcf84'),
#         client_secret=os.getenv("GITHUB_SECRET", 'ca03513033df46ae40c3176586cc65dcf2593201'),
#         code=code,
#     ),
# )
# res = parse_qs(res.content.decode("utf-8"))
# token = res["access_token"][0]


# """
# Finally, we can use the access token to obtain information about the user.
# """
# user_data = requests.get(USER_ENDPOINT, headers=dict(Authorization=f"token {token}"))
# username = user_data.json()["login"]
# print(f"You are {username} on GitHub")


import os
from flask import Flask, jsonify, redirect, url_for
from flask.views import MethodView
from flask_dance.consumer import oauth_authorized
from flask_dance.contrib.github import make_github_blueprint, github


github_blueprint = make_github_blueprint(
    client_id=os.getenv("GITHUB_ID"),
    client_secret=os.getenv("GITHUB_SECRET"),
)
 
 
class GithubLogin(MethodView):
    def get(self):
        if not github.authorized:
            return redirect(url_for('github.login'))
        
                
        return jsonify('OK')
    

class GithubVerify(MethodView):
    # @oauth_authorized.connect_via(github_blueprint)
    def get(self):
        info = github.get("/users")
        if info.ok:
            username = info.json()['login']
            print(username)
        return jsonify('OK')