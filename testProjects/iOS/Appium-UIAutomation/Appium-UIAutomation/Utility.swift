//
//  Utility.swift
//  Appium-UIAutomation
//
//  Created by Anjum Shrimali on 4/5/17.
//  Copyright © 2017 IshiSystems. All rights reserved.
//

import Foundation

class Utility {
    var displayName:String?, username:String?, password:String?
    
    private init() { }
    
    static let shared = Utility()
    
    func register(displayName:String, username:String, password:String) -> Void {
        self.displayName = displayName
        self.username = username
        self.password = password
    }
    
    func login(username:String, password:String) -> Bool {
        if let usr = self.username, let pwd = self.password, usr == username && pwd == password {
            return true
        }
        
        return false
    }
    
    
}
