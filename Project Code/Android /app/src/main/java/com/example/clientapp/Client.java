package com.example.clientapp;

import android.os.AsyncTask;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

public class Client extends AsyncTask<Void, Void, Void> {


    String type = "";
    String ipAddress = "103.25.120.190";

    Client(String t) {
        type = t;
    }

    protected Void doInBackground(Void... arg0) {
        if (type == "low tide") {
            try {
                Socket cli = new Socket(ipAddress, 9999);
                OutputStream toServer = cli.getOutputStream();
                DataOutputStream out = new DataOutputStream(toServer);
                out.writeBytes("low tide");
                }
            catch (IOException e)
                {
                    e.printStackTrace();
                }
        }
        else if (type == "normal tide") {
            try {
                Socket cli = new Socket(ipAddress, 9999);
                OutputStream toServer = cli.getOutputStream();
                DataOutputStream out = new DataOutputStream(toServer);
                out.writeBytes("low tide");
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        }
        else if (type == "face recognizer") {
            try {
                Socket cli = new Socket(ipAddress, 9999);
                OutputStream toServer = cli.getOutputStream();
                DataOutputStream out = new DataOutputStream(toServer);
                out.writeBytes("low tide");
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        }
        return null;
    }

}
