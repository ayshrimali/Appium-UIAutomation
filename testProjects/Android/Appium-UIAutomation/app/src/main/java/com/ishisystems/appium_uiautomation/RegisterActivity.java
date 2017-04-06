package com.ishisystems.appium_uiautomation;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.ishisystems.appium_uiautomation.commons.Utility;

/**
 * Created by anjum.shrimali on 4/5/17.
 */

public class RegisterActivity extends AppCompatActivity {

    private EditText edtUsername, edtPassword, edtDisplayName;
    private Button btnLogin, btnRegister;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        bindViews();

        setActionListeners();

        setTitle("Register");
    }

    private void bindViews() {
        edtDisplayName = (EditText) findViewById(R.id.edtDisplayName);
        edtUsername = (EditText) findViewById(R.id.edtUsername);
        edtPassword = (EditText) findViewById(R.id.edtPassword);
        btnLogin = (Button) findViewById(R.id.btnLogin);
        btnRegister = (Button) findViewById(R.id.btnRegister);
    }

    private void setActionListeners() {
        btnRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (validate()) {
                    Utility.register(edtDisplayName.getText().toString(),
                            edtUsername.getText().toString(),
                            edtPassword.getText().toString());
                    Utility.showInfoDialog("Registered successfully", new Runnable() {
                        @Override
                        public void run() {
                            finish();
                        }
                    }, RegisterActivity.this);
                }
            }
        });

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
    }

    private boolean validate() {
        edtDisplayName.setText(edtDisplayName.getText().toString().trim());
        edtUsername.setText(edtUsername.getText().toString().trim());
        edtPassword.setText(edtPassword.getText().toString().trim());

        String displayname = edtDisplayName.getText().toString();
        if (displayname != null && displayname.length() == 0) {
            Utility.showInfoDialog("Please enter display name", null, this);
            return false;
        }

        String username = edtUsername.getText().toString();
        if (username != null && username.length() == 0) {
            Utility.showInfoDialog("Please enter username", null, this);
            return false;
        }

        String password = edtPassword.getText().toString();
        if (password != null && password.length() == 0) {
            Utility.showInfoDialog("Please enter password", null, this);
            return false;
        }

        return true;
    }
}
