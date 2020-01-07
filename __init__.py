# -*- coding: utf-8 -*-
"""This module contains the MindMeld home assistant blueprint application"""
from traveli.root import app

import traveli.greeting
import traveli.hotels_in_city
import traveli.unknown
import traveli.weather  # noqa: ignore=F401

__all__ = ['app']
