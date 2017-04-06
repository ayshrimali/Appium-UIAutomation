package com.ishisystems.appium_uiautomation;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.ishisystems.appium_uiautomation.commons.Utility;

public class LoginActivity extends AppCompatActivity {

    private EditText edtUsername, edtPassword;
    private Button btnLogin, btnRegister;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        bindViews();

        setActionListeners();

        setTitle("Login");
    }

    @Override
    protected void onResume() {
        super.onResume();
        edtUsername.setText("");
        edtPassword.setText("");
    }

    private void bindViews() {
        edtUsername = (EditText) findViewById(R.id.edtUsername);
        edtPassword = (EditText) findViewById(R.id.edtPassword);
        btnLogin = (Button) findViewById(R.id.btnLogin);
        btnRegister = (Button) findViewById(R.id.btnRegister);
    }

    private void setActionListeners() {
        btnRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent objIntent = new Intent(LoginActivity.this, RegisterActivity.class);
                startActivity(objIntent);
            }
        });

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (validate()) {
                    if (Utility.login(edtUsername.getText().toString(),
                            edtPassword.getText().toString())) {
                        Intent objIntent = new Intent(LoginActivity.this, HomeActivity.class);
                        startActivity(objIntent);
                        finish();
                    } else {
                        Utility.showInfoDialog("Invalid username or password", null, LoginActivity.this);
                    }
                }
            }
        });
    }

    private boolean validate() {
        edtUsername.setText(edtUsername.getText().toString().trim());
        edtPassword.setText(edtPassword.getText().toString().trim());

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
