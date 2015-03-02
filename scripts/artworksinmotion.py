'''
Artworks in Motion module

Artworks in Motion (http://www.artworksinmotion.com/) is a project by
Return to the Source (http://r2src.com/) with the aim to become an
exhibition of internet-age visual artworks.

This Python module exports the functions needed to manage the Youtube
playlist that currently powers the Artworks in Motion project.

'''

import os
import yaml
from gdata.youtube import YouTubePlaylistVideoEntry
from gdata.youtube.service import YouTubeService
from jinja2 import Environment, FileSystemLoader

# Google account details:
EMAIL        = ''
PASSWORD     = ''

# Google developer details:
KEY          = ''
SOURCE       = ''
PLAYLIST_URI = ''

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)

# load the video database
with open(os.path.join(PARENT_DIR, 'db')) as db:
    VIDEOS = yaml.load(db)

# set jinja environment
ENV = Environment(loader=FileSystemLoader(os.path.join(PARENT_DIR, 'templates')))

def populate():
    '''
    Populates the site directory (../site) with html pages.

    First, it creates subdirectories for each video named after their
    slug and uses ../templates/video.html to generate each index.html

    Second, it uses ../templates/index.html to create the main page
    which contains a list of all the videos.

    WARNING: All previously existing files will be overwritten!
    '''

    template = ENV.get_template('video.html')
    for video in VIDEOS:
        html = template.render(video=video)
        video_dir = os.path.join(PARENT_DIR, 'site', video['slug'])
        if not os.path.exists(video_dir):
            os.makedirs(video_dir)
        with open(os.path.join(video_dir, 'index.html'), 'w') as f:
            f.write(html.encode('utf-8'))

    template = ENV.get_template("index.html")
    html = template.render(videos=VIDEOS)
    with open(os.path.join(PARENT_DIR, 'site', 'index.html'), "w") as f:
        f.write(html.encode('utf-8'))

def addvideo(video_id):
    '''
    Adds a video to the Artworks in Motion playlist, or raises an
    exception when it fails
    '''
    service = YouTubeService()
    service.ssl = True
    service.email = EMAIL
    service.password = PASSWORD
    service.developer_key = KEY
    service.source = SOURCE
    service.ProgrammaticLogin()

    entry = service.AddPlaylistVideoEntryToPlaylist(PLAYLIST_URI, video_id)

    if not isinstance(entry, YouTubePlaylistVideoEntry):
        raise Exception('Video not added to playlist for unknown reason')

def write_db():
    '''
    Writes the current contents of the VIDEOS array to the db file.

    '''
    with open(os.path.join(PARENT_DIR, 'db'), 'w') as file:
        yaml.dump(VIDEOS, file, default_flow_style=False)
