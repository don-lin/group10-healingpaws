package se.g10.appoinments;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemSelectedListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import java.util.ArrayList;
import java.util.List;

import se.g10.DataManager;
import se.g10.R;
import se.g10.doctors.Doctor;
import se.g10.pets.Pet;

public class AppoinmentFragment extends Fragment {
    private List<Appoinment> appoinments;
    private static List<Pet> pets;
    private static List<Doctor> doctors;
    private ListView mListView;
    private TextView spinnerTextView1;
    private TextView spinnerTextView2;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.general_list, container, false);
        LayoutInflater factory = LayoutInflater.from(getActivity());
        final View textEntryView = factory.inflate(R.layout.doctor_dialog, null);
        Button addButton=view.findViewById(R.id.add);
        addButton.setText("add a new appointment");
        addButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                DataManager dm=new DataManager();
                dm.start();
                LayoutInflater factory = LayoutInflater.from(getActivity());
                final View textEntryView = factory.inflate(R.layout.appointment_dialog, null);
                final Spinner petSpinner = textEntryView.findViewById(R.id.select_pet);
                final Spinner doctorSpinner = textEntryView.findViewById(R.id.select_doctor);
                //获取数据源
                pets = DataManager.pets;
                doctors = DataManager.doctors;
                //使用数组存放名字
                String[] petNames = new String[pets.size()];
                for(int i = 0; i < pets.size(); i++){
                    petNames[i] = pets.get(i).getName();
                }
                String[] doctorNames = new String[doctors.size()];
                for(int i = 0; i < doctors.size(); i++){
                    doctorNames[i] = doctors.get(i).getName();
                }
                
                //将可选内容与ArrayAdapter连接起来
                ArrayAdapter<String> adapter1 = new ArrayAdapter<String>(getContext(), R.layout.support_simple_spinner_dropdown_item, petNames);
                ArrayAdapter<String> adapter2 = new ArrayAdapter<String>(getContext(), R.layout.support_simple_spinner_dropdown_item, doctorNames);

                //设置下拉列表的风格
                adapter1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

                //将adapter 添加到spinner中
                petSpinner.setAdapter(adapter1);
                doctorSpinner.setAdapter(adapter2);

                //设置spinner监听
                petSpinner.setOnItemSelectedListener(new PetSelectedListener());
                doctorSpinner.setOnItemSelectedListener(new DoctorSelectedListener());

                petSpinner.setVisibility(View.VISIBLE);
                doctorSpinner.setVisibility(View.VISIBLE);

                Context context = getContext();
                AlertDialog.Builder builder = new AlertDialog.Builder(context);
                builder.setTitle("预约");
                builder.setView(textEntryView);

                builder.setPositiveButton("确认", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                    }
                });

                builder.setNegativeButton("取消", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {

                    }
                });
                builder.show();

            }
        });

        mListView = view.findViewById(R.id.listview);

        AppoinmentAdapter myAdapter = new AppoinmentAdapter(DataManager.appoinments, getContext());
        myAdapter.notifyDataSetChanged();
        mListView.setAdapter(myAdapter);

        return view;
    }

    //使用数组形式操作
    class PetSelectedListener implements OnItemSelectedListener{

        public void onItemSelected(AdapterView<?> arg0, View arg1, int arg2,
                                   long arg3) {
            //这里已经获取了选择的对象
            Pet pet = pets.get(arg2);
            Toast.makeText(getContext(),"你选择了 "+ pet.getName(),Toast.LENGTH_SHORT).show();
        }

        public void onNothingSelected(AdapterView<?> arg0) {
        }

    }

    class DoctorSelectedListener implements OnItemSelectedListener{

        public void onItemSelected(AdapterView<?> arg0, View arg1, int arg2,
                                   long arg3) {
            //这里已经获取了选择的对象
            Doctor doctor = doctors.get(arg2);
            Toast.makeText(getContext(),"你选择了 "+ doctor.getName(),Toast.LENGTH_SHORT).show();
        }

        public void onNothingSelected(AdapterView<?> arg0) {
        }

    }
}
