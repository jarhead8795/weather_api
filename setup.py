import setuptools

setuptools.setup(name='weather_api',
                 version='0.0.1',
                 author = 'Patrick Morton',
                 author_email = 'jarhead8795@gmail.com',
                 description = 'Location and weather forecast package',
                 long_description='Location and weather forecast package',
                 long_description_content_type = 'text/x-rst,'
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                ],
                python_requires='>=3.0'                         
)