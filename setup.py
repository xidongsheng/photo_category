from setuptools import setup, find_packages

setup(
      name="PictureCategory",
      version="0.0.1",
      description="category photos by date",
      author="Dongsheng Xi",
      url="",
      license="LGPL",
      packages= find_packages(),
      install_requires=['Pillow'],
      # scripts=["picture_category/*.py"],
      entry_points = {
        'console_scripts': [
            'pic_category = picture_category.main:main']
      }
    )