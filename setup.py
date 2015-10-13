from distutils.core import setup


setup(
    name='base64fonts',
    version='1.0',
    author='Harsh Vakharia',
    py_modules=['convert'],
    install_requires=['colorama'],
    license='MIT',
    keywords='fonts less sass converter',
    entry_points={
        'console_scripts': ['base64fonts = convert:main']
    })
