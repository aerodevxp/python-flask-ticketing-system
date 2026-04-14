import app
import os

if __name__ == "__main__":
   our_app = app.create_app()
   our_app.run(host="127.0.0.1")