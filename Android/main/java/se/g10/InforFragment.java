package se.g10;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import se.g10.R;

public class InforFragment extends Fragment {

    private ImageButton profilePhoto;
    private TextView history, logOut, setting;

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);

        //关联activity
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //fragment创建
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_infor, null);

        profilePhoto = view.findViewById(R.id.profilePhoto);
        profilePhoto.setImageResource(R.drawable.zhangsan);
        profilePhoto.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //头像点击事件
            }
        });

        history = view.findViewById(R.id.history);
        history.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //查看预约历史点击事件
            }
        });

        logOut = view.findViewById(R.id.logOut);
        logOut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //退出登录点击事件
            }
        });

        setting = view.findViewById(R.id.setting);
        setting.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //设置点击事件
            }
        });

        return view;
        //fragment视图创建
    }

    @Override
    public void onActivityCreated(@Nullable Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        //activity创建
    }

    @Override
    public void onStart() {
        super.onStart();
    }

    @Override
    public void onStop() {
        super.onStop();
    }

    @Override
    public void onResume() {
        super.onResume();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        //销毁
    }

    @Override
    public void onPause() {
        super.onPause();
        //暂停
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        //视图销毁
    }

    @Override
    public void onDetach() {
        super.onDetach();
        //解除绑定
    }
}
