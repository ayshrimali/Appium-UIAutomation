import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# refer at http://appium.io/slate/en/master/?ruby#the-default-capabilities-flag for more details


def get_desired_capabilities(app_path=str, platform=int):

    if app_path == '<<Path to application bundle>>':
        print('Please set <<Path to application bundle>> in your test case')
        exit(1)

    if platform == 1:
        desired_caps = {
            'deviceName': 'iPhone 5s',
            'platformName': 'iOS',
            'platformVersion': '10.2',
            'app': PATH('./' + app_path),
            'automationName': 'XCUITest',
            'noReset': 'true',
            'fullReset': 'false'
        }
    elif platform == 2:
        desired_caps = {
            'deviceName': 'emulator-5554',
            'platformName': 'Android',
            'platformVersion': '7.0',
            'app': PATH('./' + app_path),
            'automationName': 'uiautomator2',
            'noReset': 'true',
            'fullReset': 'false'
        }


    return desired_caps
