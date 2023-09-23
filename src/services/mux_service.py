import requests
import json
from ..config import Config

config = Config()

class MuxService:
    def __init__(self, token_id, token_secret):
        self.base_url = "https://api.mux.com/video/v1"
        self.token_id = config.mux_token_id
        self.token_secret = config.mux_token_secret
        self.headers = {"Content-Type": "application/json"}
        self.auth = (self.token_id, self.token_secret)
        self.assets = None

    def get_assets(self):
        url = f"{self.base_url}/assets"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        asset_data = self.extract_asset_data(response.json())
        return asset_data

    # example response
    #{'tracks': [{'type': 'video', 'max_width': 1280, 'max_height': 720, 
        #'max_frame_rate': 30, 'id': '6B7SLE7C2qriSvnjCwv8XDpaIff502651qCQIQN7g19c', 'duration': 18.2}, 
        #{'type': 'audio', 'max_channels': 2, 'max_channel_layout': 'stereo', 
        #'id': 'jSrsJf5OGi7B49KAIWAAYdgKsf6HulQxVB5zdsDXoC8', 'duration': 18.204444}], 'status': 'ready', 
        #'playback_ids': [{'policy': 'public', 'id': 'vTr6GNQkx19lOHeO00AW5C9hi7XidXNJaNRZccp353iI'}], 
        #'passthrough': '8561d564-7ca8-4976-bd55-d8ac254dabf8', 'mp4_support': 'none', 'max_stored_resolution': 'HD', 
        #'max_stored_frame_rate': 30, 'master_access': 'none', 'id': 'riDrY3ypcHS02SRbG6BbOmWMoeWCt7e8rlQ1012u025rpA',
        # 'duration': 18.233333, 'created_at': '1614915194', 'aspect_ratio': '16:9'}
    def extract_asset_data(self, json_data):
        asset_data = []
        data = json_data["data"]

        for item in data:
            if item["status"] == "ready":
                asset = {}
                asset["created_at"] = item["created_at"]
                asset["duration"] = item["duration"]
                asset["aspect_ratio"] = item["aspect_ratio"]

                # Extract playback ID
                if "playback_ids" in item:
                    playback_id_obj = next((pb for pb in item["playback_ids"] if pb["policy"] == "public"), None)
                    asset["playback_id"] = playback_id_obj["id"] if playback_id_obj else None
                else:
                    asset["playback_id"] = None

                # Extract video track info
                video_track = next((track for track in item["tracks"] if track["type"] == "video"), None)
                if video_track:
                    asset["max_width"] = video_track["max_width"]
                    asset["max_height"] = video_track["max_height"]
                    asset["max_frame_rate"] = video_track["max_frame_rate"]

                asset_data.append(asset)

        return asset_data
