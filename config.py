import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "20870885"))
    API_HASH = os.environ.get("API_HASH", "a7e1280d30225e7aa036d57a0c9bb929")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5297888360")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://afmovies013:2ogoa47o7uge8SHt@cluster0.rpk5lsu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
