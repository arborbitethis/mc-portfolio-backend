import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.mux_token_id = os.getenv("MUX_TOKEN_ID")
        self.mux_token_secret = os.getenv("MUX_TOKEN_SECRET")
        self.database_url = os.getenv("DATABASE_URL")
