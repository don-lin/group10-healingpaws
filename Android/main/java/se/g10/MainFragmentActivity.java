package se.g10;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.util.List;

import se.g10.appoinments.AppoinmentFragment;
import se.g10.doctors.DoctorsFragment;
import se.g10.pets.Pet;
import se.g10.pets.StatusFragment;

public class MainFragmentActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fragment);
        Button f1=findViewById(R.id.f1);
        f1.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                changeFragment(new HomeFragment());
            }
        });
        Button f2=findViewById(R.id.f2);
        f2.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                changeFragment(new StatusFragment());
            }
        });

        Button doctors=findViewById(R.id.doctors);
        doctors.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                changeFragment(new DoctorsFragment());
            }
        });
        Button f3=findViewById(R.id.f3);
        f3.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                changeFragment(new AppoinmentFragment());
            }
        });

        Button f4=findViewById(R.id.f4);
        f4.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                changeFragment(new InforFragment());
            }
        });
        DataManager.refreshData();
        changeFragment(new InputFragment());

    }

    public void changeFragment(Fragment fragment) {

        FragmentTransaction fragmentTransaction = getSupportFragmentManager().beginTransaction();
        fragmentTransaction.setCustomAnimations(R.anim.slide_right_in,R.anim.slide_left_out);
        fragmentTransaction.replace(R.id.myFragment, fragment);
        fragmentTransaction.commit();
    }
}
