from setuptools import setup
import os

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='django-user-clipboard',
    version='0.2.0',
    url='https://github.com/IndustriaTech/django-user-clipboard',
    description='Clipboard API',
    author='Vladimir Rusinov',
    author_email='vladimirrussinov@gmail.com',
    long_description=README,
    install_requires=[
        'Pillow',
        'django-imagekit',
    ],
    packages=[
        'user_clipboard',
        'user_clipboard.management',
        'user_clipboard.management.commands',
        'user_clipboard.migrations',
        'user_clipboard.south_migrations',
        'user_clipboard.utils',
    ],
    package_data={
        '': ['LICENSE', 'README.md']
    },
    include_package_data=True,
    keywords=['Clipboard', 'Clipboard API', 'File Clipboard', 'Image Clipboard'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP/JSON',
    ],
)
