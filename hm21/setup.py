import setuptools

setuptools.setup(name='otushm',
                 version='0.1',
                 url='https://github.com/kyklaed/otus-qa-course',
                 license='Free',
                 author='Vadim',
                 author_email='kyklaed@gmail.com',
                 description='home work for otus qa course',
                 packages=setuptools.find_packages(exclude=['otus-qa-course']),
                 install_requires=['pytest>=4.6.3'],
                 zip_safe=False)