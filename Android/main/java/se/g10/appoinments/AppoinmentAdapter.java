package se.g10.appoinments;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.List;

import se.g10.R;

public class AppoinmentAdapter extends BaseAdapter {
    private List<Appoinment> appoinments;
    private LayoutInflater inflater;

    public AppoinmentAdapter(List<Appoinment> mAppoinments, Context context){
        this.appoinments = mAppoinments;
        this.inflater = LayoutInflater.from(context);
    }

    @Override
    public int getCount() {
        return appoinments.size();
    }

    @Override
    public Object getItem(int i) {
        return appoinments.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int i, View contentView, ViewGroup viewGroup) {
        View view = inflater.inflate(R.layout.general_item, null);
        Appoinment mAppoinment = (Appoinment) getItem(i);

        TextView petName = view.findViewById(R.id.line1);
        TextView doctorName = view.findViewById(R.id.line2);
        TextView date = view.findViewById(R.id.line3);

        petName.setText("Pet Name: " + mAppoinment.getPetName());
        doctorName.setText("Doctor Name: " + mAppoinment.getDoctorName());
        date.setText("Date: " + mAppoinment.getDate());

        return view;
    }
}
