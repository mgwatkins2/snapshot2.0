from setuptools import setup

setup(
	name='snapshot2.0',
	version='0.1',
	author="Matthew Watkins",
	author_email="mgwatkins2@gmail.com",
	description="Snapshot2.0 is a tool to manage AWS EC2 snapshots",
	license="GPLv3+",
	packages=['shotty'],
	url="https://github.com/mgwatkins2/snapshot2.0",
	install_requires=[
		'click',
		'boto3'
	],
	entry_points='''
		[console_scripts]
		shotty=shotty.shotty:cli
	''',
)