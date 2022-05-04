# Route_Recommendation_App

## Client Setup

1. Open `index.html` use any browser

### Known issue

- The web page refreshes itself in few seconds after first run, please wait for ~10sec or it refreshes (it blinks), whichever comes first
## Server Setup

1. Make sure to update
   1. `sudo apt update`
   2. `sudo apt upgrade`
2. Configure environment inside the repo
   1. `sudo apt install python3.10-venv`
   2. `python3 -m venv venv`
   3. ` . venv/bin/activate`: activate environment
3. Install dependencies
   1. `pip3 install Flask osmnx scikit-learn shapely` 
   1. `pip3 install -U flask-cors`
4. Configure Flask settings
   1. `export FLASK_APP=server`
5. Run
   1. `python3 server.py`
