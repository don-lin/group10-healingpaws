package se.g10.appoinments;

public class Appoinment {
    public int id;
    public String petName;
    public String doctorName;
    public String date;

    public Appoinment(int id, String petName, String doctorName, String date) {
        this.id = id;
        this.petName = petName;
        this.doctorName = doctorName;
        this.date = date;
    }

    public int getId() {
        return id;
    }

    public String getPetName(){
        return petName;
    }
    public  String getDoctorName(){
        return doctorName;
    }
    public String getDate(){
        return date;
    }

}
