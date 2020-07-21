#!/usr/bin/env python

"""
    utils.py
    ----------
    This module contains special utilities to declare database
	models.
"""

__author__ = "Arian Gallardo"

from app import db 

class AddUpdateDelete():
	"Interface for database models that allow them to implement SQL transactions smoothly."
	def add(self, resource):
		""" Adds a resource to the database (insertion).

			:type resource: object
			:param resource: Object to be added to the database.
		"""
		db.session.add(resource)
	
	def update(self):
		"Updates a resource to the database."
		pass
	
	def delete(self, resource):
		""" Deletes a resource from the database.

			:type resource: object
			:param resource: Object to be deleted from the database.
		"""
		db.session.delete(resource)
		return db.session.commit()
