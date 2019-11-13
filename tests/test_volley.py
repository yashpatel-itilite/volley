import unittest

from volley import Form
from volley.fields import Field
from volley.validators import Required


class UserValidationForm(Form):
	first_name = Field('user.first_name', validators=[Required()])
	last_name = Field('user.last_name', validators=[Required()])
	email = Field('user.email', validators=[Required()])
	phone = Field('user.address.phone', validators=[Required()])


mock_false_data = {
	'user': {
		'last_name': 'Doe',
		'email': 'mailme@jhondoe.com',
	}
}

mock_false_data_errors = {
	'first_name': ['First name is required'],
	'phone': ['Phone is required'],
}

mock = {
	'user': {
		'first_name': 'Jhon',
		'last_name': 'Doe',
		'email': 'mailme@jhondoe.com',
		'address': {
			'phone': '+9100000000',
		}
	}
}

expected = {
	'first_name': 'Jhon',
	'last_name': 'Doe',
	'email': 'mailme@jhondoe.com',
	'phone': '+9100000000'
}



class TestVolley(unittest.TestCase):
	def test_form_validation_succeeds(self):
		form = UserValidationForm(mock)
		is_validation_passed = form.validate()
		self.assertTrue(is_validation_passed)

	def test_form_validation_provides_new_positioning(self):
		form = UserValidationForm(mock)
		form.validate()
		self.assertEqual(expected, form.data)

	def test_form_validation_fails(self):
		form = UserValidationForm(mock_false_data)
		self.assertFalse(form.validate())

	def test_errors_form_validation_fails(self):
		form = UserValidationForm(mock_false_data)
		form.validate()
		self.assertEqual(form.errors, mock_false_data_errors)
