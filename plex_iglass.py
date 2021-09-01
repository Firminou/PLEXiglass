from pypresence import Presence
from plexapi.myplex import MyPlexAccount
import time
import json

with open('image.json') as ima:
    data = json.load(ima)

with open('config.json') as con:
    config = json.load(con)

data_title, data_id = [], []

for image in data['series']:
    data_title.append(image['title'])
    data_id.append(image['image_id'])

for image in data['movies']:
    data_title.append(image['title'])
    data_id.append(image['image_id'])
# Here I put all of the image.json in lists so it's easier

plex_username = config['plex_username']
plex_password = config['plex_password']
plex_server = config['plex_server']

client_id = config['client_id']  # Discord Application ID
RPC = Presence(client_id)
RPC.connect()


def search_in_image(to_search):
    index = -1
    for title in data_title:
        index += 1
        if title == to_search:
            return data_id[index]
    return 'plexblack'
# This function search in the image.json if my/your application support
# the image for the current show/movie


while True:
    account = MyPlexAccount(plex_username, plex_password)
    myPlex = account.resource(plex_server).connect()

    print(myPlex.sessions())
    session = myPlex.sessions()[0]

    if session.TYPE == 'episode':
        image = 'plexblack'

        if session.grandparentTitle in data_title:
            image = search_in_image(session.grandparentTitle)

        RPC.update(
            details=f"Watching {session.grandparentTitle}",
            state=f"S{session.parentIndex} E{session.index}",
            large_image=image
            )

    elif session.TYPE == 'movie':
        image = 'plexblack'

        if session.title in data_title:
            image = search_in_image(session.title)

        RPC.update(
            details=f"Watching {session.title}",
            large_image=image
            )

    time.sleep(120)  # It will update every two minutes
