import setuptools

setuptools.setup(name='weather_api_assignment',
                 version='0.0.1',
                 author = 'Patrick Morton',
                 author_email = 'jarhead8795@gmail.com',
                 description = 'Location and weather forecast package',
                 long_description='Location and weather forecast package',
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                ],
                python_requires='>=3.0'                         
)