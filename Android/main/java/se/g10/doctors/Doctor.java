package se.g10.doctors;

public class Doctor {
    public int id;
    public String name;
    public int age;
    public String introduction;

    public Doctor(int id, String name, int age, String introduction) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.introduction = introduction;
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
