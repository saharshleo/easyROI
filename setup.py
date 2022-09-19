import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='EasyROI',
    packages=setuptools.find_packages(),
    version='1.0.3',
    description='ROI Helper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Saharsh',
    url='https://github.com/saharshleo/easyROI',
    license='MIT',
    install_requires=['opencv-python==4.5.1.48', 'numpy==1.22.0'],
    python_requires='>=3.6',
    setup_requires=[],
    tests_require=[],
    test_suite='tests',
)