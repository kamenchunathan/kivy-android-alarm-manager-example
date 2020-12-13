# kivy-android-alarm-scheduler-example

Illustrates using the android alarm manager to schedule tasks using kivy

The receiver has to be registered in the android manifest and this is done by adding the following in the Manifest template file located in .buildozer/android/platform/build-armeabi-v7a/dists/myapp__armeabi-v7a/templates/AndroidManifest.tmpl.xml
if buildozer is being used

```xml
<receiver
            android:name="org.test.myapp.TaskReceiver"
            android:enabled="true"
            android:exported="true" />
```
