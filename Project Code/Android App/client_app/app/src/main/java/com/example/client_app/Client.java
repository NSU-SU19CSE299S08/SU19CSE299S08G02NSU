package com.example.client_app;

import android.os.AsyncTask;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

public class Client extends AsyncTask<Void,Void,Void> {

    String type = "";
    String ip_address = "192.168.0.103";

    Client(String t){
        type = t;
    }

    protected Void doInBackground(Void... arg0){
        try {
            Socket client = new Socket(ip_address,7890);
            OutputStream toServer = client.getOutputStream();
            DataOutputStream output = new DataOutputStream(toServer);
            output.writeBytes(type);
        } catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }

}

