import unittest

from volley import Form
from volley.fields import Field
from volley.validators import Required


class UserValidationForm(Form):
	first_name = Field('user.first_name')
	last_name = Field('User.last_name')
	email = Field('User.email')
	phone = Field('User.address.phone')


class TestVolley(unittest.TestCase):
	def test_form_validation_succeeds(self):
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

		form = UserValidationForm(mock)

		is_validation_passed = form.validate()

		self.assertTrue(is_validation_passed)

		self.assertEqual(expected, mock)

	def test_form_validation_fails(self):
		pass
