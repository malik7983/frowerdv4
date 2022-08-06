#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 12345))
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    SESSION = os.environ.get("SESSION", "Media_search")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
