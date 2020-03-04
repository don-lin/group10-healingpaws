package se.g10.appoinments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ListView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import java.util.ArrayList;
import java.util.List;

import se.g10.DataManager;
import se.g10.R;

public class AppoinmentFragment extends Fragment {
    private List<Appoinment> appoinments;
    private ListView mListView;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.general_list, container, false);

        Button addButton=view.findViewById(R.id.add);
        addButton.setText("add a new appointment");
        addButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {

            }
        });

        mListView = view.findViewById(R.id.listview);

        AppoinmentAdapter myAdapter = new AppoinmentAdapter(DataManager.appoinments, getContext());
        myAdapter.notifyDataSetChanged();
        mListView.setAdapter(myAdapter);

        return view;
    }
}
