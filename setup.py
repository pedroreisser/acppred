from setuptools import setup, find_packages

setup(
    name='acppred',
    version='0.0.1',
    packages=find_packages(),
    author='Pedro',
    entry_points={
        'console_scripts':[
            'acppred-train = acppred.train:main',
            'acppred-predict = acppred.predict:main'
        ]
    }
)

