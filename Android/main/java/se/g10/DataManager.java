package se.g10;

import android.util.Log;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import se.g10.appoinments.Appoinment;
import se.g10.doctors.Doctor;
import se.g10.doctors.DoctorsFragment;
import se.g10.pets.Pet;

public class DataManager extends Thread{
    public static List<Pet> pets;
    public static List<Doctor> doctors;
    public static List<Appoinment> appoinments;

    public static int running=0;

    public final static String splitKey="dlcc";
    public final static String formatKey="ccddll";

    public static void refreshData(){
        pets = new ArrayList<>();
        pets.add(new Pet(1, "狗", "2020-01-02","健康"));
        pets.add(new Pet(2, "猫", "2020-01-13", "健康"));

        doctors = new ArrayList<>();
        doctors.add(new Doctor(1, "张三", 50,"名医","6666"));
        doctors.add(new Doctor(2, "李四", 70, "名医", "8888"));
        appoinments = new ArrayList<>();
        appoinments.add(new Appoinment(1, "狗1", "张三","2020年5月1日"));
        appoinments.add(new Appoinment(2, "狗2", "李四","2020年3月1日"));
    }

    public void run(){
        try {
            URL url = new URL("http://0cdl.com:2020/android/doctors");

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            //3. POST
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            conn.setDoOutput(true);
            OutputStream os = conn.getOutputStream();
            String param = "haha";
            os.write(param.getBytes("utf-8"));
            os.flush();
            InputStream is = conn.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(is));
            StringBuilder sb = new StringBuilder();
            String line = null;
            while ((line = reader.readLine()) != null) {
                sb.append(line);
            }
            String responseText = sb.toString();
            Log.d("test",responseText);
            String[] r=responseText.split(splitKey);
            doctors=new ArrayList<>();
            for(int i=0;i<r.length;i++){
                Doctor d=new Doctor(r[i],formatKey);
                doctors.add(d);
            }
            conn.disconnect();
        }catch (Exception e){
            Log.d("test",e.toString());
        }
        running=0;
    }
}
