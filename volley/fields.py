""" Fields

	Attributes ::
		- Field
		- StringField
"""

import jmespath


class Field(object):
	DEFAULT = None

	def __init__(self, position, validators: list=[], default=None):
		self._position = position
		self._validators = validators
		self._default = default or self.DEFAULT

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
	DEFAULT = ''

	def process_value(self, data):
		value = super(StringField, self).process_value(data)

		if not isinstance(value, str):
			raise TypeError()

		return value

	def error_message(self, human_readable_attribute_name):
		return '{} must be string'.format(human_readable_attribute_name)


class FloatField(Field):
	DEFAULT = 0

	def process_value(self, data):
		value = super(FloatField, self).process_value(data)

		if isinstance(value, str):
			if value.isnumeric():
				value = float(value)

		if not isinstance(value, float):
			raise TypeError()

		return value

	def error_message(self, human_readable_attribute_name):
		return '{} must be string'.format(human_readable_attribute_name)


class ListField(Field):
	DEFAULT = []
