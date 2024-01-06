from flask import Flask, request
import webbrowser
import config
import secrets

global oauth_access_token
global oauth_state

def authorize():
    state = secrets.token_hex(32)
    webbrowser.open("https://www.tumblr.com/oauth2/authorize?client_id={consumer_key}&response_type=code&scope=basic+write&state={state}".format(
        consumer_key=config.Config().TUMBLR_CONSUMER_KEY,
        state=state
        ))

    app = Flask(__name__)

    @app.route("/tumblr_authenticated")
    def tumblr_authenticated():
        print(request.args)

        global oauth_access_token
        oauth_access_token = request.args.get("code")
        global oauth_state
        oauth_state = request.args.get("state")
        return "Authenticated"
    
    app.run(port=8080)
    
    if state != oauth_state:
        raise Exception("State does not match")

    return oauth_access_token