package se.g10.doctors;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import java.util.ArrayList;
import java.util.List;

import se.g10.DataManager;
import se.g10.R;

public class DoctorsFragment extends Fragment {
    private ListView mListView;
    public DoctorAdapter myAdapter;

    public void refreshList(){
        myAdapter = new DoctorAdapter(DataManager.doctors, getContext());
        myAdapter.notifyDataSetChanged();
        mListView.setAdapter(myAdapter);
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.general_list, container, false);

        Button addButton=view.findViewById(R.id.add);
        addButton.setText("add a new doctor");
        addButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                LayoutInflater factory = LayoutInflater.from(getActivity());
                final View textEntryView = factory.inflate(R.layout.doctor_dialog, null);
                Context context = getContext();
                AlertDialog.Builder builder = new AlertDialog.Builder(context);
                builder.setTitle("请输入医生信息");
                final EditText editNname = textEntryView.findViewById(R.id.editTextName);
                final EditText editTelephone = textEntryView.findViewById(R.id.editTextPhone);
                final EditText editAge = textEntryView.findViewById(R.id.editTextAge);
                final EditText editIntroduction = textEntryView.findViewById(R.id.editTextIntro);

                builder.setView(textEntryView);
                builder.setPositiveButton("确认", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        String name = editNname.getText().toString();
                        String telephone = editTelephone.getText().toString();
                        int age = Integer.valueOf(editAge.getText().toString());
                        String introduction = editIntroduction.getText().toString();
                        Toast.makeText(getActivity(),name + telephone + age + introduction, Toast.LENGTH_SHORT ).show();
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

        Button refreshButton=view.findViewById(R.id.refresh);
        refreshButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                DataManager dm=new DataManager();
                if(dm.running==1)
                    return;//prevent dead lock
                dm.running=1;
                dm.start();
                refreshList();
            }
        });

        mListView = view.findViewById(R.id.listview);
        refreshList();

        return view;
    }
}
