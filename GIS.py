from google_images_search import GoogleImagesSearch
import os

cse_id = os.environ.get("cse_id", None)
api_key = os.environ.get("api_key", None)

gis = GoogleImagesSearch("api_key", "cse_id")

_search_params = {
    'q': '...',
    'num': 1-50,
    'safe': 'high|medium|off',
    'fileType': 'jpg|gif|png',
    'imgType': 'clipart|face|lineart|news|photo',
    'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
    'searchType': 'image',
    'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow'
}

gis.search({'q': 'puppies', 'num': 3})
