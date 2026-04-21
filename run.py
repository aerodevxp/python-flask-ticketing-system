import app
import os

if __name__ == "__main__":
   our_app = app.create_app()
   our_app.run(threaded=True, ssl_context=('selfcerts/cert.pem', 'selfcerts/key.pem'), host="0.0.0.0") 