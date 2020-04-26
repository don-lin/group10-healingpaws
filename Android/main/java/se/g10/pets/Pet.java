package se.g10.pets;

public class Pet {
    private int id;
    private String name;
    private String birthday;
    private String health;

    public Pet(int id, String name, String birthday, String health) {
        this.id = id;
        this.name = name;
        this.birthday = birthday;
        this.health = health;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getBirthday() {
        return birthday;
    }

    public String getHealth() {
        return health;
    }

    public void setHealth(String health) {
        this.health = health;
    }
}
