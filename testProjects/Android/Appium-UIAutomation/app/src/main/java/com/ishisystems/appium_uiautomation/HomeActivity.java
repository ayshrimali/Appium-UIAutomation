package com.ishisystems.appium_uiautomation;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

import com.ishisystems.appium_uiautomation.commons.Utility;

/**
 * Created by anjum.shrimali on 4/5/17.
 */

public class HomeActivity extends AppCompatActivity {

    private TextView txtWelcome;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        setTitle("Home");
        ((TextView) findViewById(R.id.txtWelcome)).setText("Welcome " + Utility.getDisplayName() + "!");

    }
}
