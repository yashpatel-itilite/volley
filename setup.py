from setuptools import setup, find_packages

setup(
	name='volley',
	version='0.1.1',
	description='Python Data Validation Library',
	url='https://www.github.com/yashpatel-itilite/volley',
	license='MIT',
	packages=find_packages(exclude=('tests', 'tests/*', 'example', 'example/*')),
	install_requires=[
		'jmespath',
	],
	zip_safe=False,
	test_suite='nose.collector',
    tests_require=['nose']
)
