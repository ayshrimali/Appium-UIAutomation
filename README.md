# Appium-UIAutomation
A handy tool based on Appium & Python to write common UIAutomation test cases easily (for both iOS and Android).

## Installation
####Install Python and setuptools
This tool requires Python 3.6 and setuptools. If you don't have that yet, download and install it from [here](https://www.python.org/downloads/).

Once you have Python, you will need to install setuptools. Install it using command,

```shell
pip install setuptools
```

####Install GUI less Appium 1.6
You should also have Appium 1.6 installed in your machine, If you don't have that too, you can get some help to install in your machine from these steps,
1. Download and install node js from [here](https://nodejs.org/en/download/). Make sure to use official installer to install node, which will take care of all required components. Else you may need to identify and install each missing component like npm.
2. Download and install GUI less Appium 1.6 (beta) using this command,
```shell
npm install appium 1.6.1
```

####Install Appium-UIAutomation lib
There are three ways to install and use the Appium Python client.

1. Install from [PyPi](https://pypi.python.org/pypi), as
['Appium-UIAutomation'](https://pypi.python.org/pypi/Appium-UIAutomation).

    ```shell
    pip install Appium_UIAutomation
    ```

2. Install from source, via [PyPi](https://pypi.python.org/pypi). From ['Appium-UIAutomation'](https://pypi.python.org/pypi/Appium-UIAutomation),
download and unarchive the source tarball (Appium-UIAutomation-X.X.tar.gz).

    ```shell
    tar -xvf Appium-UIAutomation-X.X.tar.gz
    cd Appium-UIAutomation-X.X
    python setup.py install
    ```

3. Install from source via [GitHub](https://github.com/ayshrimali/Appium-UIAutomation).

    ```shell
    git clone https://github.com/ayshrimali/Appium-UIAutomation.git
    cd Appium-UIAutomation
    python setup.py install
    ```

## Usage
Appium-UIAutomation is python based client library based on Appium-Python-Client and Selenimum 3.0. It is still in evaluation phase and has an objective to write easy and common test cases which can be executed on both iOS and Android platforms.

To start, create a folder and keep your apps bundles into it, say 'testApps',

go to your 'testApps' folder,

```shell
cd testApps
```

generate test suite file with your desired file name,

```shell
generate_testcase
Enter test case suite name:<<>Enter your suite file name here>
```

This will generate two files in your current folder,
1. desired_capabilities.py - where you can specify details of your simulator or physical device. You can also configure testing methodology. For more details, refer [here](http://appium.io/slate/en/master/?ruby#the-default-capabilities-flag).
2. TestSuite.py - where you can write your own test cases.

Execute your test suite, which will ask for platform to run and app bundle to test.

```shell
python TestSuite.py
1 - iOS
2 - Android
Choose platform:1
Enter path to app bundle:testApps/AppBundle.zip
```
 
Make sure your Appium server is up and running while you execute your test suite. You can see results in text file generated with name 'Test_suite_name_report.txt'
 
Happy automating. ;) 
