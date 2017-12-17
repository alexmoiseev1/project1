from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

import src.config as config

import re

class YSearch:

    youtube = None

    def __init__(self):
        pass

    def __search(options):
        global youtube
        youtube = build(config.API_SERVICE_NAME, config.API_VERSION, developerKey=config.API_KEY)

        search_items = youtube.search().list(
            q=options.q,
            part="id,snippet",
            maxResults=options.maxResults,
            type="channel"
        ).execute()['items']

        return YSearch.__flush(search_items)

    def __flush(items):

        info_list = []

        for item in items:
            snippet = item['snippet']
            info_dict = {k: snippet[k] for k in snippet if k in config.FIELD_SET}
            info_list.append(info_dict)
        return info_list

    def run(q=config.DEFAULT_SEARCH, maxResults=config.MAX_RESULTS):

        args = config.Options(q=q, maxResults=maxResults)

        try:
            return YSearch.__search(args)
        except HttpError as e:
            print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))


    def to_dict(result):
        result_dict = {}

        for item in result:
            result_dict[item['channelId']] = item

        return result_dict


    def channel(channelId):
        global youtube
        channel_info = youtube.channels().list(
            part="snippet, statistics",
            id=channelId
        ).execute()['items'][0]
        return channel_info

    def desc_to_mail(desc):
        match = re.search(r'[\w\.-]+@[\w\.-]+', desc)
        if match != None:
            return match.group(0)
        return None
