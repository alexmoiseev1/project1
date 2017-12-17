from collections import namedtuple

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
API_KEY = 'AIzaSyCoX9a5SUgRmT1FZuU3QxdigS9txzM3dxM'

DEFAULT_SEARCH = ''
MAX_RESULTS = 50

Options = namedtuple('Options', ['q', 'maxResults'])

FIELD_SET = {'channelId', 'title'}
