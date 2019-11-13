""" Fields

	Attributes ::
		- Field
		- StringField
"""

import jmespath


class Field(object):
	def __init__(self, position, validators: list=[], default=None):
		self._position = position
		self._validators = validators
		self._default = default

	@property
	def validators(self):
		return self._validators

	@property
	def default(self):
		return self._default

	@property
	def position(self):
		return self._position

	def process_value(self, data):
		return jmespath.search(self.position, data) or self.default


class StringField(Field):
	def process_value(self):
		return
