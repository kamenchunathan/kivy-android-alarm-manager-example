package org.test.myapp;

import android.content.Context;
import android.content.Intent;
import android.content.BroadcastReceiver;
import android.media.MediaPlayer;
import android.provider.Settings;
import android.os.Bundle;
import android.util.Log;

public class TaskReceiver extends BroadcastReceiver {

    // The onReceive method will start the service defined in the buildozer.spec file
    @Override
    public void onReceive(Context context, Intent intent){
        // set argument to pass to python code
        Bundle extras = intent.getExtras();
        String argument = extras.getString("pythonServiceArgument");
        Log.i("python", argument);
        /*
            The ServiceHandleTask class corresponds to the class defined in the the buildozer.spec file as:
                services = handletask:tasks.py
        */
        ServiceHandletask.start(context, argument);
    }

}