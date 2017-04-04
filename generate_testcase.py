#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

print("1 - Andriod")
print("2 - iOS")
platform = input("Choose platform:")
testCaseSuiteName = input("Enter test case suite name:")
filein = open('automation/template_testcase.txt')

if int(platform) == 1: # its android
    platform = 'Platform.ANDROID'
elif int(platform) == 2: # its iOS
    platform = 'Platform.IOS'
else:
    print('You have selected an invalid platform')
    exit(1)


if filein is not None:
    # write testcase.py
    src = filein.read().format(testCaseSuiteName, platform)
    dstFile = open(testCaseSuiteName + ".py", "w")
    dstFile.write(src)
    dstFile.close()
    filein.close()

    # write desired_caps.py
    filein = open("automation/template_desired_capabilities.txt")
    src = filein.read()
    dstFile = open("desired_capabilities.py", "w")
    dstFile.write(src)
    dstFile.close()
