# Volley
> Python data validation library

Lot of libraries are there to validate the data like WTForms, jsonshcema etc ...
you also might have used one of them, previously I have used WTForms a lot in
my personal projects, It has very cool features and the fun thing is everything
is written in fully object oriented way.

It is very useful when your data is in linear form, linear is a sence there's
no nested level inside the dictionary. Still upto one level nested structure it
is good. Incase of very complecated nesting structure it'll become very difficult
to write validations.

>> Let's take a look at it
```
from volley import Form
from volley.fields import Field
from volley.validators import Required

data = {
	'user': {
		'first_name': 'Jhon',
		'last_name': 'Doe',
		'email': 'mailme@jhondoe.com',
		'addresses': [{
			'phone': '+9100000000',
		}]
	}
}


class UserValidationForm(Form):
	first_name = Field('user.first_name', validators=[Required()])
	last_name = Field('user.last_name', validators=[Required()])
	email = Field('user.email', validators=[Required()])
	phone = Field('user.addresses.phone[0]', validators=[Required()])

form = UserValidationForm(data)

if not form.validate():
	print(form.errors)
```

Inspired by WTForms
