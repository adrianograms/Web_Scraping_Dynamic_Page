from src.web_scraping import get_video_infomations
from flask import Flask, request, jsonify

app = Flask(__name__)
base_url = 'https://www.youtube.com/'

@app.route('/')
def channel_scraping():
    """Scrape a youtube channel page for all videos (informations about the videos)

    Returns:
        string: Return all the video informations in a json format
    """
    try:
        name_channel = request.args.get('name_channel')
        name_channel = '@' + name_channel

        jumps = request.args.get('jumps')
        if jumps is None:
            jumps = 0
        jumps = int(jumps)
        
        wait_time = request.args.get('wait_time')
        if wait_time is None:
            wait_time = 4
        wait_time = int(wait_time)

        popular = request.args.get('popular')
        if popular is None:
            popular = False
        elif 'TRUE' == popular.upper():
            popular = True
        else:
            popular = False
        
        url = base_url + name_channel + '/videos'
        video_infos = get_video_infomations(url, jumps, wait_time, popular)
        return jsonify(video_infos)
    except ValueError:
        return "Wrong type", 400
    except TypeError:
        return "Wrong paramaters", 400

app.config['JSON_AS_ASCII'] = False

if __name__ == "__main__":
    app.run(debug=True)