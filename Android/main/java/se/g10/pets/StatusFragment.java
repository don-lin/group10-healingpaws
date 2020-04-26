package se.g10.pets;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import se.g10.DataManager;
import se.g10.R;

public class StatusFragment extends Fragment {
    private ListView mListView;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.general_list, container, false);
        Button addButton=view.findViewById(R.id.add);
        addButton.setText("add a new pet");
        addButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                LayoutInflater factory = LayoutInflater.from(getActivity());
                final View textEntryView = factory.inflate(R.layout.pet_dialog, null);
                Context context = getContext();
                AlertDialog.Builder builder = new AlertDialog.Builder(context);
                builder.setTitle("请输入宠物信息");
                final EditText editName = textEntryView.findViewById(R.id.editTextName);
                final EditText editDob = textEntryView.findViewById(R.id.editTextdob);


                builder.setView(textEntryView);
                builder.setPositiveButton("确认", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        String name = editName.getText().toString();
                        String dob = editDob.getText().toString();
                        Toast.makeText(getActivity(),name + dob, Toast.LENGTH_SHORT ).show();
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


        PetAdapter myAdapter = new PetAdapter(DataManager.pets, getActivity());
        myAdapter.notifyDataSetChanged();
        mListView.setAdapter(myAdapter);

        return view;
    }
}
