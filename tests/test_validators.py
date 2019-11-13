import unittest

from volley.fields import StringField, FloatField


class TestValidators(unittest.TestCase):
	def test_string_field(self):
		field = StringField('foo')

		value = field.process_value({ 'foo': 'bar' })
		self.assertEqual('bar', value)

	def test_string_fields_default_value(self):
		field = StringField('foo')

		value = field.process_value({ 'bar': 'foo' })
		self.assertEqual('', value)

	def test_float_field(self):
		field = FloatField('foo')

		value = field.process_value({ 'foo': 10.20 })
		self.assertEqual(10.20, value)

	def test_float_field_with_float_as_string(self):
		field = FloatField('bar')

		value = field.process_value({ 'bar': '10' })
		self.assertEqual(10, value)
