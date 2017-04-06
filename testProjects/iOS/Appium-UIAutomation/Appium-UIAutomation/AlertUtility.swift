//
//  AlertUtility.swift
//  SkoolClub
//
//  Created by Kushagra Pandya on 3/22/17.
//  Copyright © 2017 conficle. All rights reserved.
//

import UIKit

class AlertUtility: NSObject {
    
    static func showAlert(title: String?, message: String?, presentOn:UIViewController, handler:((UIAlertAction) -> Void)? = nil) {
        let alertCon = UIAlertController(title: title,
                                         message: message
            , preferredStyle: .alert)
        alertCon.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.default ,
                                         handler:handler))
        presentOn.present(alertCon, animated: true, completion: nil)
    }
}
