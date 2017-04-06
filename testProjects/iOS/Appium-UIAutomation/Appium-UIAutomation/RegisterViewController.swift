//
//  RegisterViewController.swift
//  Appium-UIAutomation
//
//  Created by Anjum Shrimali on 4/5/17.
//  Copyright © 2017 IshiSystems. All rights reserved.
//

import Foundation
import UIKit

class RegisterViewController: UIViewController {
    
    @IBOutlet weak var txtDisplayName: UITextField!
    @IBOutlet weak var txtUsername: UITextField!
    @IBOutlet weak var txtPassword: UITextField!
    @IBOutlet weak var btnRegister: UIButton!
    @IBOutlet weak var btnLogin: UIButton!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
    }
    
    func validate() -> String? {
        let trimDisplayName: String? = self.txtDisplayName.text?.trimmingCharacters(in: CharacterSet(charactersIn: " "))
        guard (trimDisplayName?.lengthOfBytes(using: .utf8))! > 0 else {
            return "Please enter display name"
        }
        
        let trimUsername: String? = self.txtUsername.text?.trimmingCharacters(in: CharacterSet(charactersIn: " "))
        guard (trimUsername?.lengthOfBytes(using: .utf8))! > 0 else {
            return "Please enter username"
        }
        
        let trimPass: String? = self.txtPassword.text?.trimmingCharacters(in: CharacterSet(charactersIn: " "))
        guard (trimPass?.lengthOfBytes(using: .utf8))! > 0 else {
            return "Please enter password"
        }
        
        return nil
    }
    
    
    @IBAction func btnRegisterPressed(_ sender: UIButton) {
        txtDisplayName.resignFirstResponder()
        txtUsername.resignFirstResponder()
        txtPassword.resignFirstResponder()
        let errorMessage = self.validate()
        if errorMessage == nil {
            Utility.shared.register(displayName: txtDisplayName.text!, username: txtUsername.text!, password: txtPassword.text!)
            AlertUtility.showAlert(title: "", message: "Registered successfully", presentOn: self, handler: {(action:UIAlertAction) -> Void in
                self.navigationController!.popViewController(animated: true)
            })
        } else {
            AlertUtility.showAlert(title: "", message: errorMessage, presentOn: self)
        }
    }
    
    @IBAction func btnLoginPressed(_ sender: UIButton) {
        self.navigationController!.popViewController(animated: true)
    }
    
}
