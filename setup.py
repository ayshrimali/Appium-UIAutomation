from distutils.core import setup

setup(
    name='Appium-UIAutomation',
    version='0.0.1',
    packages=['automation', 'automation.mobile'],
    url='https://github.com/ayshrimali/Appium-UIAutomation',
    license='Apache 2.0',
    author='Anjum Shrimali',
    author_email='ayshrimali@gmail.com',
    description='A handy tool based on Appium-Python to write common UIAutomation test cases (for both iOS and Android) easily.',
    keywords=[
        'appium',
        'appium 1.0',
        'selenium',
        'selenium 3',
        'python client',
        'mobile automation'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=['selenium>=2.47.0', 'Appium-Python-Client=0.24']
)
