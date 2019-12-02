#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
from google.oauth2 import service_account
from googleapiclient.discovery import build


def get_creds(config):
    return service_account.Credentials.from_service_account_file(
        config["cred_file"],
        scopes=["https://www.googleapis.com/auth/presentations"],
    )


def get_service(config):
    return build("slides", "v1", credentials=get_creds(config)).presentations()


def randomize():
    with open("config.json", "r") as f:
        config = json.load(f)
    service = get_service(config)
    presentation = service.get(presentationId=config["deck_id"]).execute()
    slides = presentation.get("slides")
    ids = [slide.get("objectId") for slide in slides[1:]]
    random.shuffle(ids)
    updates = [
        {"updateSlidesPosition": {"slideObjectIds": [i], "insertionIndex": 1}}
        for i in ids
    ]
    service.batchUpdate(
        presentationId=config["deck_id"], body={"requests": updates}
    ).execute()


if __name__ == "__main__":
    randomize()
