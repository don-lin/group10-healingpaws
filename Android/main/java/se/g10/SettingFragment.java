package se.g10;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.SeekBar;
import android.widget.TextView;

import androidx.fragment.app.Fragment;

public class SettingFragment extends Fragment {
    class RefreshColorListener implements SeekBar.OnSeekBarChangeListener{

        @Override
        public void onProgressChanged(SeekBar seekBar, int i, boolean b) {

            int alphaValue=alphaSeekBar.getProgress()*255/alphaSeekBar.getMax();
            int redValue=redSeekBar.getProgress()*255/redSeekBar.getMax();
            int greenValue=greenSeekBar.getProgress()*255/greenSeekBar.getMax();
            int blueValue=blueSeekBar.getProgress()*255/blueSeekBar.getMax();
            Log.d("red_value",""+redValue);
            Log.d("red_max",""+redSeekBar.getMax());

            int finalcolor=(alphaValue<<(8*3))+(redValue<<(8*2))+(greenValue<<(8*1))+(blueValue<<(8*0));

            Log.d("final_color",""+finalcolor);
            colorSample.setBackgroundColor(finalcolor);
        }

        @Override
        public void onStartTrackingTouch(SeekBar seekBar) {

        }

        @Override
        public void onStopTrackingTouch(SeekBar seekBar) {

        }
    }

    static TextView colorSample;
    static SeekBar alphaSeekBar;
    static SeekBar redSeekBar;
    static SeekBar greenSeekBar;
    static SeekBar blueSeekBar;

    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view=inflater.inflate(R.layout.setting,container,false);

        colorSample=view.findViewById(R.id.colorSample);
        alphaSeekBar=view.findViewById(R.id.alphaValue);
        redSeekBar=view.findViewById(R.id.redValue);
        greenSeekBar=view.findViewById(R.id.greenValue);
        blueSeekBar=view.findViewById(R.id.blueValue);

        alphaSeekBar.setOnSeekBarChangeListener(new RefreshColorListener());
        redSeekBar.setOnSeekBarChangeListener(new RefreshColorListener());
        greenSeekBar.setOnSeekBarChangeListener(new RefreshColorListener());
        blueSeekBar.setOnSeekBarChangeListener(new RefreshColorListener());
        
        return view;
    }
}
