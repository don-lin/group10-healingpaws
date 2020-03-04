package se.g10.pets;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ListView;

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

            }
        });

        mListView = view.findViewById(R.id.listview);


        PetAdapter myAdapter = new PetAdapter(DataManager.pets, getActivity());
        myAdapter.notifyDataSetChanged();
        mListView.setAdapter(myAdapter);

        return view;
    }
}
