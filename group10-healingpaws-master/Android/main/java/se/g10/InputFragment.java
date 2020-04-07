package se.g10;

import android.annotation.SuppressLint;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;

import androidx.fragment.app.Fragment;

import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class InputFragment extends Fragment {
    ImageView i ;

    @SuppressLint("HandlerLeak")
    private Handler wxHandler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            switch (msg.what) {
                case 0:
                    Bitmap wxShareBitmap = (Bitmap) msg.obj;
                    i.setImageBitmap(wxShareBitmap);
                    break;
            }
        }
    };

    private void getBitmap(final String imgUrl) {

        new Thread(new Runnable() {
            @Override
            public void run() {
                HttpURLConnection connection = null;
                try {
                    URL bitmapUrl = new URL(imgUrl);
                    connection = (HttpURLConnection) bitmapUrl.openConnection();
                    connection.setRequestMethod("GET");
                    connection.setConnectTimeout(5000);
                    connection.setReadTimeout(5000);

                    if (connection.getResponseCode() == 200) {
                        InputStream inputStream = connection.getInputStream();
                        Bitmap shareBitmap = BitmapFactory.decodeStream(inputStream);
                        Message message = wxHandler.obtainMessage();
                        message.what = 0;
                        message.obj = shareBitmap;
                        wxHandler.sendMessage(message);
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                } finally {
                    if (connection != null) {
                        connection.disconnect();
                    }
                }
            }
        }).start();
    }

    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view=inflater.inflate(R.layout.input,container,false);
        i=view.findViewById(R.id.imageView);
        getBitmap("http://0cdl.com:5000/static/images/body_bg.jpg");
        return view;
    }
}
