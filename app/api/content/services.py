from random import randrange
from typing import Final
from fastapi import HTTPException
import requests
from urllib.parse import urljoin, quote_plus
from .schemas import ContentRequest, ContentResponse


def get(request: ContentRequest):
    return request
