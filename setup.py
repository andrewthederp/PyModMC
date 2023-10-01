import setuptools

setuptools.setup(
    name='PyModMC',
    version='1.2.2-alpha',
    author='Fluxyn',
    description='A Minecraft modding library made for Python.',
    url='https://github.com/Fluxyn/PyModMC',
    packages=['PyModMC'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    include_package_data=True,
    package_data={
        '': [
            'locale_codes.txt'
        ]
    },
)
