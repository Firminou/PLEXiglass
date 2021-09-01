# PLEXiglass
A script to update your discord rich presence to what show/movie you are watching

# Requirements:
- Python (I used 3.9.7 but it should be fine with most versions)
- pypresence (After installing python run "py -m pip install pypresence" into the terminal if you are on windows, 
and I don't know what to run on linux but if you are using it you should already know)
- plexapi ("py -m pip install plexapi")

# Configuration:
Open config_blank.json and then change the text only the text don't touche the " or the ,

When you are done with it rename it to config.json

# Custom pictures (optional):
It's actually pretty easy to do !
- Go on: https://discord.com/developers/applications
- Create a new app
- On your new app you should see an Application ID put it into the config.json where it belongs
- After on the rich presence part upload a new image and call it "plexblack" it will be the default image
- Then upload as many images as you want
- Then on the image.json remove what I done but keep the formatting you can remove as many as you want but don't forget the , and the "
- title is the actual name on the show plex shows
- image_id is the name of the image on the discord rich presence

# When you are done just run plex_iglass.py and it will update every two minutes
