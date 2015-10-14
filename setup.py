from distutils.core import setup


setup(
    name='base64fonts',
    version='0.1',
    author='Harsh Vakharia',
    py_modules=['base64fonts'],
    install_requires=['colorama'],
    license='MIT',
    keywords='fonts less sass converter',
    entry_points={
        'console_scripts': ['base64fonts = base64fonts:main']
    })
