package kr.ac.knu.cse.myapplication8;


import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.material.snackbar.Snackbar;
import com.google.gson.Gson;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    public static final int REQUEST_CODE_MENU = 101;

    EditText editText;
    TextView textview;
    static RequestQueue requestQueue;

    WeatherAdapter adapter;
    RecyclerView recyclerView;
    RadioGroup radioGroup1;


    ProgressBar progressBar;
    ProgressDialog dialog;

    boolean check1 = true;
    boolean check2 = true;
    String checkRegion;

    String date;

    String url = "";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        editText = findViewById(R.id.editText);
        textview = findViewById(R.id.textView);

        radioGroup1 = findViewById(R.id.RadioGroup1);



        progressBar = findViewById(R.id.progressBar);
        progressBar.setIndeterminate(false);
        progressBar.setProgress(80);
        progressBar.setVisibility(View.INVISIBLE);

        dialog = new ProgressDialog(MainActivity.this);



        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                check1 = true;
                dialog.setProgressStyle(ProgressDialog.STYLE_SPINNER);
                dialog.setMessage("잠시만 기다려 주세요 :D");
                dialog.show();


                InputMethodManager imm = (InputMethodManager)getSystemService(Activity.INPUT_METHOD_SERVICE);
                try{
                    imm.hideSoftInputFromWindow(getCurrentFocus().getWindowToken(),0);

                }catch (Exception e){
                    check1 = false;
                    Toast.makeText(getApplicationContext(),"오늘 또는 어제 날짜를 YYYYMMDD형식으로 입력하고(EX->20221217). 원하시는 지역을 선택해주세요. 또한 오늘 기준으로 검색하시는 경우 오전 2시 이전이라면 어제 날짜로 검색해주세요",Toast.LENGTH_LONG).show();
                }

                if(check1 == true) {
                    date = editText.getText().toString();
                }
                url = "";
                adapter.clearAll();
                url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=UH0KuuikKjLuZnNYrgNFeRWBZ7klTILJBaUp2zjui2cv9O9AMjuAI%2FwnTPbNgLCaFYG4ze1HFtHZgzP4RoiNQQ%3D%3D&numOfRows=1000&dataType=JSON&pageNo=1&base_date=" + date + "&base_time=0200";

                switch (radioGroup1.getCheckedRadioButtonId()) {
                    case R.id.radioButton: {
                        url = url + "&nx=55&ny=127";
                        checkRegion = "서울/경기";
                        break;
                    }

                    case R.id.radioButton2: {
                        url = url + "&nx=60&ny=127";
                        checkRegion = "춘천/강원";
                        break;
                    }

                    case R.id.radioButton3: {
                        url = url + "&nx=89&ny=90";
                        checkRegion = "대구/경북";
                        break;
                    }

                    case R.id.radioButton4: {
                        url = url + "&nx=60&ny=74";
                        checkRegion = "광주/전남";
                        break;
                    }

                    case R.id.radioButton5: {
                        url = url + "&nx=98&ny=76";
                        checkRegion = "부산/경남";
                        break;
                    }

                    case R.id.radioButton6: {
                        url = url + "&nx=69&ny=106";
                        checkRegion = "청주/충북";
                        break;
                    }

                    case R.id.radioButton7: {
                        url = url + "&nx=67&ny=100";
                        checkRegion = "대전/충남";
                        break;
                    }

                    case R.id.radioButton8: {
                        url = url + "&nx=63&ny=89";
                        checkRegion = "전주/전북";
                        break;
                    }

                    case R.id.radioButton9: {
                        url = url + "&nx=53&ny=38";
                        checkRegion = "제주";
                        break;
                    }


                }

                makeRequest();

            }
        });
        requestQueue = Volley.newRequestQueue(getApplicationContext());

        //리싸이클러뷰 가동을 위한 코드
        recyclerView = findViewById(R.id.recyclerView);
        LinearLayoutManager layoutManager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        recyclerView.setLayoutManager(layoutManager);
        adapter = new WeatherAdapter();
        recyclerView.setAdapter(adapter);

        Button button2 = findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(),MenuActivity.class);
                if(!url.equals("") && check1 == true && check2 == true){
                    intent.putExtra("date",date);
                    intent.putExtra("region",checkRegion);
                }
                startActivityForResult(intent,REQUEST_CODE_MENU);
            }
        });




    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if(requestCode == REQUEST_CODE_MENU){
            Toast.makeText(this, "메인화면으로 돌아옴", Toast.LENGTH_LONG).show();
        }if(resultCode == RESULT_OK) {
            String name = data.getStringExtra("name");
            Toast.makeText(this, "" +  name, Toast.LENGTH_LONG).show();
        }
    }

    private void makeRequest(){
        StringRequest request = new StringRequest(Request.Method.GET, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                //println("응답 : " + response);
                try{
                    check2 = true;
                    processResponse(response);
                }catch (Exception e){
                    check2 = false;
                    dialog.dismiss();
                    Toast.makeText(getApplicationContext(),"오늘 또는 어제 날짜를 YYYYMMDD형식으로 입력하고(EX->20221217). 원하시는 지역을 선택해주세요.  또한 오늘 기준으로 검색하시는 경우 오전 2시 이전이라면 어제 날짜로 검색해주세요",Toast.LENGTH_LONG).show();

                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                println("에러 : " + error);
            }
        });
        request.setShouldCache(false);
        requestQueue.add(request);
        println("요청 보냄");
    }

    public void println(String data) {
        Log.d("MainActivity", data);
    }

    private void processResponse(String responseJson){// Json값이 파라미터로 들어옴
        Gson gson = new Gson();
        Weather weather = gson.fromJson(responseJson,Weather.class);
        println(weather.response.body.items.item.size()+"");
        Item item;
        for(int i = 0; i< weather.response.body.items.item.size(); i++){

            if(weather.response.body.items.item.get(i).category.equals("TMP")) {
                item = weather.response.body.items.item.get(i);
                item.region = checkRegion;
                adapter.addItem(item);
            }
            if(weather.response.body.items.item.get(i).category.equals("PCP")){
                item = weather.response.body.items.item.get(i);
                item.region = checkRegion;
                adapter.addItem(item);
            }
        }
        adapter.notifyDataSetChanged();
        dialog.dismiss();

    }
}


class Weather{
    ResPonse response;
}


class ResPonse{
    Header header;
    Body body;
}

class Header{
    int resultCode;
    String resultMsg;
}

class Body{
    String dataType;
    Items items;
}

class Items{
    ArrayList<Item> item = new ArrayList<Item>();
}

class Item{
    int baseData;
    int baseTime;
    String category;
    int fcstDate;
    int fcstTime;
    String fcstValue;
    int nx;
    int ny;
    String region;

    String regId;
    int rnSt3Am;
    int rnSt3Pm;
    int rnSt4Am;
    int rnSt4Pm;
    int rnSt5Am;
    int rnSt5Pm;
    int rnSt6Am;
    int rnSt6Pm;
    int rnSt7Am;
    int rnSt7Pm;
    int rnSt8;
    int rnSt9;
    int rnSt10;
    String wf3Am;
    String wf3Pm;
    String wf4Am;
    String wf4Pm;
    String wf5Am;
    String wf5Pm;
    String wf6Am;
    String wf6Pm;
    String wf7Am;
    String wf7Pm;
    String wf8;
    String wf9;
    String wf10;

}