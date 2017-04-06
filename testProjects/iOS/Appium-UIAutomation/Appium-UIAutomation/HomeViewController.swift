//
//  HomeViewController.swift
//  Appium-UIAutomation
//
//  Created by Anjum Shrimali on 4/5/17.
//  Copyright © 2017 IshiSystems. All rights reserved.
//

import Foundation
import UIKit

class HomeViewController: UIViewController {
    
    
    @IBOutlet weak var txtWelcome: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        txtWelcome.text = "Welcome \(Utility.shared.displayName!)!"
    }
    
}
