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
        doctors.add(new Doctor(1, "张三", 50,"名医"));
        doctors.add(new Doctor(2, "李四", 70, "名医"));

        appoinments = new ArrayList<>();
        appoinments.add(new Appoinment(1, "狗1", "张三","2020年5月1日"));
        appoinments.add(new Appoinment(2, "狗2", "李四","2020年3月1日"));
    }

    public void run(){
        try {
            URL url = new URL("http://192.168.199.224:2020/android/doctors");
            //2. HttpURLConnection
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            //3. POST
            conn.setRequestMethod("POST");
            //4. Content-Type,这里是固定写法，发送内容的类型
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            //5. output，这里要记得开启输出流，将自己要添加的参数用这个输出流写进去，传给服务端，这是socket的基本结构
            conn.setDoOutput(true);
            OutputStream os = conn.getOutputStream();
            String param = "haha";
            //一定要记得将自己的参数转换为字节，编码格式是utf-8
            os.write(param.getBytes("utf-8"));
            os.flush();
            //6. is
            InputStream is = conn.getInputStream();
            //7. 解析is，获取responseText
            BufferedReader reader = new BufferedReader(new InputStreamReader(is));
            StringBuilder sb = new StringBuilder();
            String line = null;
            while ((line = reader.readLine()) != null) {
                sb.append(line);
            }
            //获取响应文本
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
