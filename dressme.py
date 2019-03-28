from google_images_search import GoogleImagesSearch
import os

cse_id = os.environ.get("cse_id", None)
api_key = os.environ.get("api_key", None)

gis = GoogleImagesSearch('api_key', 'cse_id')

_search_params = {
    'q': '...',
    'num': 1-50,
    'safe': 'high',
    'fileType': 'jpg|gif|png',
    'imgType': 'photo',
    'imgSize': 'medium',
    'searchType': 'image',
    'imgDominantColor': ''
}

gis.search(_search_params=_search_params)
