package com.ishisystems.appium_uiautomation.commons;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;

/**
 * Created by anjum.shrimali on 4/5/17.
 */

public class Utility {
    public static void showInfoDialog(String msg, final Runnable callBack, Context mContext) {
        AlertDialog.Builder builder = new AlertDialog.Builder(mContext);
        builder.setMessage("Info");
        builder.setMessage(msg);
        builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {

            @Override
            public void onClick(DialogInterface dialog, int which) {
                dialog.dismiss();
                if (callBack != null)
                    callBack.run();
            }
        });
        builder.show();
    }

    private static String displayName = "N/A", username = "", password = "";

    public static void register(String displayName, String username, String password) {
        Utility.displayName = displayName;
        Utility.username = username;
        Utility.password = password;
    }

    public static boolean login(String username, String password) {
        if (username.equals(Utility.username) && password.equals(Utility.password))
            return true;
        else
            return false;
    }

    public static String getDisplayName() {
        return Utility.displayName;
    }
}
