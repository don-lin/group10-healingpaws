package se.g10;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainFragmentActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fragment);
        Button f1=findViewById(R.id.f1);
        f1.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                changeFragment(new SettingFragment());
            }
        });
        Button f2=findViewById(R.id.f2);
        f2.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                changeFragment(new InputFragment());
            }
        });

        Button f3=findViewById(R.id.f3);
        f3.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                changeFragment(new SettingFragment());
            }
        });
        changeFragment(new InputFragment());

    }

    public void changeFragment(Fragment fragment) {

        FragmentTransaction fragmentTransaction = getSupportFragmentManager().beginTransaction();
        fragmentTransaction.setCustomAnimations(R.anim.slide_right_in,R.anim.slide_left_out);
        fragmentTransaction.replace(R.id.myFragment, fragment);
        fragmentTransaction.commit();
    }
}
