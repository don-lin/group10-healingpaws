package se.g10.doctors;

import android.content.Intent;

public class Doctor {
    public int id;
    public String name;
    public int age;
    public String telphone;
    public String introduction;


    public Doctor(int id, String name, int age, String introduction) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.introduction = introduction;
    }

    public Doctor(String rawData,String format){
        String[] arr=rawData.split(format);
        this.id= Integer.parseInt(arr[0]);
        this.name=arr[1];
        this.age=Integer.parseInt(arr[2]);
        this.telphone=arr[3];
        this.introduction=arr[4];
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getIntroduction() {
        return introduction;
    }
}
