import app
import os

if __name__ == "__main__":
   our_app = app.create_app()
   our_app.run(ssl_context=('selfcerts/cert.pem', 'selfcerts/key.pem'), host="127.0.0.1")