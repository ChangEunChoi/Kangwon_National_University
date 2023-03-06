package kr.ac.knu.cse.myapplication8;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;


public class viewerFragment extends Fragment {


    TextView textView;

    public viewerFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View rootView = inflater.inflate(R.layout.fragment_viewer, container, false);
        textView = rootView.findViewById(R.id.textView);
        return rootView;
    }

    public void printText(String s) {
        textView.setText("@@@프래그먼트를 활용해 출력하는중@@@\n" + s);
    }
}