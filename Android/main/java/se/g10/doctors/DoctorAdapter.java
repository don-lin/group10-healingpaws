package se.g10.doctors;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.List;

import se.g10.R;

public class DoctorAdapter extends BaseAdapter {
    private List<Doctor> doctors;
    private LayoutInflater inflater;

    public DoctorAdapter(List<Doctor> mDoctors, Context context){
        this.doctors = mDoctors;
        this.inflater = LayoutInflater.from(context);
    }

    @Override
    public int getCount() {
        return doctors.size();
    }

    @Override
    public Object getItem(int i) {
        return doctors.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int i, View contentView, ViewGroup viewGroup) {
        View view = inflater.inflate(R.layout.general_item, null);
        Doctor mDoctor = (Doctor) getItem(i);

        TextView name = view.findViewById(R.id.line1);
        TextView age = view.findViewById(R.id.line2);
        TextView intro = view.findViewById(R.id.line3);

        name.setText("Doctor Name" + mDoctor.getName());
        age.setText("Age:" + mDoctor.getAge());
        intro.setText("Introduction:" + mDoctor.getIntroduction());

        return view;
    }
}
