package org.myapp;

import android.content.Context;
import android.content.Intent;
import android.content.BroadcastReceiver;
import android.media.MediaPlayer;
import android.provider.Settings;


public class TaskReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent){
        MediaPlayer mediaPlayer = MediaPlayer.create(
            context,
            Settings.System.DEFAULT_RINGTONE_URI
        );
        mediaPlayer.start();
    }

}