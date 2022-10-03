import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ssd1306',
    version='1.0.0',
    description='Python SSD1306 OLED driver with I2C interface.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/submer-crypto/ssd1306',
    license='MIT',
    packages=setuptools.find_packages(),
    extras_require={
        'rpi': ['adafruit-circuitpython-framebuf>=1.4.14,<1.5.0']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
