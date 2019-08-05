package com.example.clientapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void lowTide(View v)
    {
        Client myClient = new Client("low tide ");
        myClient.execute();

    }
    public void normalTide(View v)
    {
        Client myClient2 = new Client("normal tide ");
        myClient2.execute();

    }
    public void faceRecognizer(View v)
    {
        Client myClient3 = new Client("face recognizer ");
        myClient3.execute();

    }
}
