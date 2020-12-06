# kivy-android-alarm-scheduler-example
Illustrates using the android alarm manager to schedule tasks using kivy

Its relatively straightforward except that you have to add a the following code to the AndroidManifest.xml file
```
<receiver
            android:name="org.myapp.Notify"
            android:enabled="true"
            android:exported="true" />
```
