package se.g10;

import java.util.ArrayList;
import java.util.List;

import se.g10.appoinments.Appoinment;
import se.g10.doctors.Doctor;
import se.g10.pets.Pet;

public class DataManager {
    public static List<Pet> pets;
    public static List<Doctor> doctors;
    public static List<Appoinment> appoinments;

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
}
