# -*- coding: utf-8 -*-
"""This module contains the hotel dialogue states for the MindMeld
traveli application
"""

import os
import requests
import json
from .root import app
import traveli.get_city as gc
#API CONSTRAINT
CITY_NOT_FOUND_CODE = 0
DEFAULT_LOCATION = 'gandhinagar'
BASE_API_STRING = 'https://adbapi.000webhostapp.com/APIS/readone.php'


@app.handle(intent='hotels_in_city')
def find_hotels_city(request, responder):
    """
    When the user asks for weather, return the weather in that location or use gandhinagar if no
      location is given.
    """
    try:
        # Get the location the user wants
        selected_city = gc._get_city(request)
        # Get weather information via the API
        url_string = _construct_weather_api_url(selected_city)

        hotel_info = requests.get(url_string).json()
        #hotel_info = json.loads(hotel_info)
    except ConnectionError:
        reply = "Sorry, I was unable to connect to the API, please check your connection."
        responder.reply(reply)
        return

    if (int(hotel_info['Responce']) == CITY_NOT_FOUND_CODE):
        responder.slots['city'] = selected_city
        responder.reply("sorry, we are not currently surving in {city}")
        return
    lst = []
    city = hotel_info['data'][0]['City']
    responder.slots['city'] = city
    for i in range(len(hotel_info['data'])):
	    lst.append(hotel_info['data'][i]['Name'])

    hotels1 = ' ,'.join([str(elem) for elem in lst])
    responder.slots['hotels'] = hotels1 
    responder.reply("{hotels} these are the hotels located in {city}")


# Helpers

def _construct_weather_api_url(selected_location):
    url_string = "{base_string}?city={location}".format(
        base_string=BASE_API_STRING, location=selected_location.replace(" ", "+"))

    return url_string
