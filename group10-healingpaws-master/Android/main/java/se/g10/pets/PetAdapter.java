package se.g10.pets;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.List;

import se.g10.R;

public class PetAdapter extends BaseAdapter {
    private List<Pet> pets;
    private LayoutInflater inflater;

    public PetAdapter(List<Pet> mPets, Context context){
        this.pets = mPets;
        this.inflater = LayoutInflater.from(context);
    }

    @Override
    public int getCount() {
        return pets.size();
    }

    @Override
    public Object getItem(int i) {
        return pets.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int i, View contentView, ViewGroup viewGroup) {
        View view = inflater.inflate(R.layout.general_item, null);
        Pet mPet = (Pet) getItem(i);

        TextView name = view.findViewById(R.id.line1);
        TextView birthday = view.findViewById(R.id.line2);
        TextView health = view.findViewById(R.id.line3);

        name.setText("Pet Name" + mPet.getName());
        birthday.setText("Birthday:" + mPet.getBirthday());
        health.setText("Health:" + mPet.getHealth());

        return view;
    }
}
