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

from enum import Enum
from collections import namedtuple


class UIComponents:

    # named tuple to hold two xPath values for each platform
    Component = namedtuple('Component', ['iOS', 'Android'])

    LABEL = Component(iOS='//XCUIElementTypeStaticText[{}]', Android='//android.widget.TextView[{}]')
    BUTTON = Component(iOS='//XCUIElementTypeButton[{}]', Android='//android.widget.Button[{}]')
    TEXTFIELD = Component(iOS='//XCUIElementTypeTextField[{}]', Android='//android.widget.EditText[{}]')
    LIST = Component(iOS='//XCUIElementTypeTable/*[{}]', Android='//android.widget.ListView/*[{}]')
    SWITCH = Component(iOS='//XCUIElementTypeSwitch[{}]', Android='TBD')
    SLIDER = Component(iOS='//XCUIElementTypeSlider[{}]', Android='TBD')



    # iOS
    # name: (null)
    # type: XCUIElementTypeCell
    # value: (null)
    # label: (null)
    # hint: (null)
    # enabled: true
    # visible: true
    # valid: false
    # location: {0, 64}
    # size: {320, 44}
    # xpath: // XCUIElementTypeApplication[1] / XCUIElementTypeWindow[1] / XCUIElementTypeOther[1] / XCUIElementTypeOther[
    #     1] / XCUIElementTypeOther[1] / XCUIElementTypeTable[1] / XCUIElementTypeCell[1]


    # name: Buttons
    # type: XCUIElementTypeStaticText
    # value: Buttons
    # label: Buttons
    # hint: (null)
    # enabled: true
    # visible: true
    # valid: false
    # location: {15, 68}
    # size: {63, 22}
    # xpath: // XCUIElementTypeApplication[1] / XCUIElementTypeWindow[1] / XCUIElementTypeOther[1] / XCUIElementTypeOther[
    #     1] / XCUIElementTypeOther[1] / XCUIElementTypeTable[1] / XCUIElementTypeCell[1] / XCUIElementTypeStaticText[1]


    # Android
    # content - desc: Animation
    # type: android.widget.TextView
    # text: Animation
    # index: 1
    # enabled: true
    # location: {0, 387}
    # size: {1080, 144}
    # checkable: false
    # checked: false
    # focusable: false
    # clickable: true
    # long - clickable: false
    # package: com.example.android.apis
    # password: false
    # resource - id: android:id / text1
    # scrollable: false
    # selected: false
    # xpath: // android.view.ViewGroup[1] / android.widget.FrameLayout[2] / android.widget.ListView[1] / \
    #           android.widget.TextView[2]

# iOS component types
# TableViewCell = XCUIElementTypeCell
# TableView = XCUIElementTypeTable
# Label = XCUIElementTypeStaticText
# Button = XCUIElementTypeButton
# Switch = XCUIElementTypeSwitch
# Slider = XCUIElementTypeSlider
# TextField = XCUIElementTypeTextField
# Secure TextField = XCUIElementTypeSecureTextField (Password field)
# TextView = XCUIElementTypeTextView
# Picker = XCUIElementTypePickerWheel
# SegmentControl = XCUIElementTypeSegmentedControl, XCUIElementTypeButton with value 1 for selected button
# ImageView = XCUIElementTypeImage
# Toolbar = XCUIElementTypeToolbar
# ActionSheet = XCUIElementTypeSheet
# Alert = XCUIElementTypeAlert
# CollectionView = XCUIElementTypeCollectionView
# CollectionViewCell = XCUIElementTypeCell

# Android component types
# TableViewCell = Any, direct children of android.widget.ListView, they are clickable
# TableView/List = android.widget.ListView
# Label = android.widget.TextView
# Button = android.widget.Button / android.widget.ImageButton
# Switch = XCUIElementTypeSwitch
# Slider = XCUIElementTypeSlider
# TextField/EditText = android.widget.EditText
# Secure TextField = XCUIElementTypeSecureTextField (Password field)
# TextView = android.widget.TextView
# Picker/Spinner = android.widget.Spinner -> android.widget.ListView -> android.widget.CheckedTextView for context menu
# ActionBar Tab = android.app.ActionBar.Tab, android.app.ActionBar.Tab with selected true for selected tab
# ImageView = android.widget.ImageView
# Toolbar = XCUIElementTypeToolbar
# Alert = XCUIElementTypeAlert