from setuptools import setup, find_packages

setup(
    name='django-shop-bulkform',
    version=__import__('shop_bulkform').__version__,
    license="BSD",

    install_requires = [],

    description='A bulk order form for a django-shop site.',
    long_description=open('README').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-shop-bulkform',
    download_url='http://github.com/powellc/django-shop-bulkform/downloads',

    include_package_data=True,

    packages=['shop_bulkform'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
