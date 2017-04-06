//
//  ViewController.swift
//  Appium-UIAutomation
//
//  Created by Anjum Shrimali on 4/5/17.
//  Copyright © 2017 IshiSystems. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    
    @IBOutlet weak var txtUsername: UITextField!
    @IBOutlet weak var txtPassword: UITextField!
    @IBOutlet weak var btnLogin: UIButton!
    @IBOutlet weak var btnRegister: UIButton!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        txtUsername.text = ""
        txtPassword.text = ""
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func validate() -> String? {
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
    
    @IBAction func btnLoginPressed(_ sender: UIButton) {
        txtUsername.resignFirstResponder()
        txtPassword.resignFirstResponder()
        let errorMessage = self.validate()
        if errorMessage == nil {
            if Utility.shared.login(username: txtUsername.text!, password: txtPassword.text!) {
                let storyBoard = UIStoryboard(name: "Main", bundle: nil)
                let homeController = storyBoard.instantiateViewController(withIdentifier: "homecontroller")
                self.navigationController?.pushViewController(homeController, animated: true)
            } else {
                AlertUtility.showAlert(title: "", message:"Invalid username or password", presentOn: self)
            }
        } else {
            AlertUtility.showAlert(title: "", message: errorMessage, presentOn: self)
        }
    }
    
    @IBAction func btnRegisterPressed(_ sender: UIButton) {
        let storyBoard = UIStoryboard(name: "Main", bundle: nil)
        let homeController = storyBoard.instantiateViewController(withIdentifier: "registercontroller")
        self.navigationController?.pushViewController(homeController, animated: true)
    }
    
}

