#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  simple_settings.py
#
#  Copyright 2020 Sergi Casbas <sergi@casbas.cat>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
''' Simple command line arguments and settings manager '''
import json

class SimpleSettings():
	''' Simple settings / command line parameters manager '''
	def __init__(self, argv):
		''' Class initialization '''
		#Array to return.
		settings = {}

		# Convert arguments into a settings list.
		for argument in argv[1:]:
			splited = argument.split("=")
			if len(splited) == 1:
				settings[splited[0][2:]] = True
			elif len(splited) == 2:
				settings[splited[0][2:]] = splited[1]

		# Read extra settings file.
		if 'settings' in settings:
			with open(settings['settings'], 'r',encoding='utf8') as json_file:
				for key,value in json.loads(json_file.read()).items():
					if key not in settings: # cmd have higher priority.
						settings[key] = value

		# If no verbose level is defined, set it to critical.
		# This is based on the criteria of python loggin facilites
		# https://docs.python.org/3/library/logging.html
		if 'verbose' not in settings:
			settings['verbose'] = "CRITICAL"

		# Store in a class variable.
		self.__settings = settings

	def get(self, key, default=None):
		''' Get a setting, a default value can be supplied if setting don't exists '''
		if key not in self.__settings:
			return default if default is not None else None
		return self.__settings[key]

	def getAll(self):
		''' Get the whole settings dictionary '''
		return self.__settings

	def exists(self, key):
		''' Check if a key exists in the settings '''
		return key in self.__settings
