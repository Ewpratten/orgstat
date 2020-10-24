from setuptools import setup

setup(name='orgstat',
      version='1.0.0',
      description='A tool for ranking contributors to a GitHub organization',
      url='https://github.com/Ewpratten/orgstat',
      author='Evan Pratten',
      author_email='ewpratten@gmail.com',
      license='GPLv3',
      packages=['orgstat'],
      zip_safe=False,
      include_package_data=True,
      instapp_requires=[
          "requests",
          "tqdm"
      ],
      entry_points={
          'console_scripts': [
              'orgstat = orgstat.__main__:main'
          ]
      }
      )
