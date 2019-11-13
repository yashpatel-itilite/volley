""" Form """

from .fields import Field
from .exceptions import ValidationError


class Form(object):
	def __init__(self, data):
		self._data = data
		self._new_data = dict()
		self._errors = dict()

	def validate(self):
		for attr_name in dir(self):
			human_readable_attr_name = ' '.join(attr_name.split('_'))
			human_readable_attr_name = human_readable_attr_name[0].upper() + ''.join(human_readable_attr_name[1:])

			attr = getattr(self, attr_name)

			if not isinstance(attr, Field):
				continue

			value = attr.process_value(self._data)
			self._new_data[attr_name] = value

			for validator in attr.validators:
				try:
					validator.validate(attr_name, value, self._data)
				except ValidationError:
					self._add_error(attr_name, validator.error_message(human_readable_attr_name))

		return not self._errors

	@property
	def errors(self):
		return self._errors

	@property
	def data(self):
		return self._new_data

	def _add_error(self, attr_name, error_message):
		if attr_name not in self._errors:
			self._errors[attr_name] = []

		self._errors[attr_name].append(error_message)
