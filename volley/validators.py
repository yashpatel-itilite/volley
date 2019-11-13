""" Validators

	Attributes ::
		- Validator
		- Required
"""

from .exceptions import ValidationError


class Validator(object):
	def validate(self, *args, **kwargs):
		raise NotImplementedError('Validator class should implement validate method')

	def error_message(self, human_readable_attribute_name):
		return '{} is required'.format(human_readable_attribute_name)


class Required(Validator):
	def validate(self, attr_name, value, data):

		if not value:
			raise ValidationError()
