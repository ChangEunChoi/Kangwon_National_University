package kr.ac.knu.cse.myapplication8;


import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.Gson;

public class MenuActivity extends AppCompatActivity {

    TextView textView2;

    String urlStr;
    static RequestQueue requestQueue;

    String date;
    String region;
    String regionCode;

    viewerFragment viewerFragment;

    String msgforFragment;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        FragmentManager manager = getSupportFragmentManager();
        viewerFragment = (viewerFragment)manager.findFragmentById(R.id.viewerFragment);

        textView2 = findViewById(R.id.textView2);
        Button button = findViewById(R.id.button2);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent();
                intent.putExtra("name","메인화면으로 돌아갑니다.                                                                                                                                                 ");
                setResult(RESULT_OK,intent);
                finish();
            }
        });

        Button button3 = findViewById(R.id.button3);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent1 = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.weather.go.kr/w/index.do"));
                startActivity(myIntent1);
            }
        });

        Button button4 = findViewById(R.id.button4);
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent2 = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.weatheri.co.kr/"));
                startActivity(myIntent2);
            }
        });

        Button button5 = findViewById(R.id.button5);
        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent3 =  new Intent(Intent.ACTION_VIEW, Uri.parse("tel:131"));

                startActivity(myIntent3);
            }
        });

        Button button6 = findViewById(R.id.button6);
        button6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                makeRequest();
            }
        });
        requestQueue = Volley.newRequestQueue(getApplicationContext());


        Intent intentFromMain = getIntent();
        processIntent(intentFromMain);
    }

    private void processIntent(Intent intent){
        if(intent != null) {
            Bundle bundle = intent.getExtras();
            textView2.setText("'"+intent.getStringExtra("date") + "' 기준 '"+intent.getStringExtra("region")+"' 지역의 중기예보 입니다.");
            date = intent.getStringExtra("date");
            region = intent.getStringExtra("region");
            if(date != null && region != null) {
                switch (region){
                    case "서울/경기": {
                        regionCode = "11B00000";
                        break;
                    }

                    case "춘천/강원": {
                        regionCode = "11D10000";
                        break;
                    }
                    case "대구/경북":{
                        regionCode = "11H10000";
                        break;
                    }

                    case "광주/전남":{
                        regionCode = "11F20000";
                        break;
                    }

                    case "부산/경남":{
                        regionCode = "11H20000";
                        break;
                    }

                    case "청주/충북":{
                        regionCode = "11C10000";
                        break;
                    }

                    case "대전/충남":{
                        regionCode = "11C20000";
                        break;
                    }
                    case "전주/전북":{
                        regionCode = "11F10000";
                        break;
                    }
                    case "제주":{
                        regionCode = "11G00000";
                        break;
                    }

                }
                urlStr ="http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst?serviceKey=UH0KuuikKjLuZnNYrgNFeRWBZ7klTILJBaUp2zjui2cv9O9AMjuAI%2FwnTPbNgLCaFYG4ze1HFtHZgzP4RoiNQQ%3D%3D&numOfRows=1000&dataType=JSON&pageNo=1&regId="+regionCode+"&tmFc="+date+"0600";

            }else{
                urlStr ="";
            }
        }

    }


    private void makeRequest() {
        StringRequest request = new StringRequest(Request.Method.GET, urlStr, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                //println("응답 : " + response);
                try{
                    processResponse(response);//json객체 넣어줌
                }catch (Exception e) {
                    Toast.makeText(getApplicationContext(),"오류가 발생했습니다.입력값들이 올바른지 확인해주세요. (중기예보는 최근 24시간 내 조회만 가능합니다.)",Toast.LENGTH_LONG).show();
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

    private  void processResponse(String responseJson) {
        Gson gson = new Gson();
        /*MovieList movieList = gson.fromJson(response, MovieList.class);
        for (int i = 0; i < movieList.boxOfficeResult.dailyBoxOfficeList.size(); i++) {
            println(movieList.boxOfficeResult.dailyBoxOfficeList.get(i).movieNm);
        }*/
        Weather weather = gson.fromJson(responseJson,Weather.class);
        println(weather.response.body.items.item.size()+"");
        Item item;
        msgforFragment = "";
        println("3일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf3Am);
        msgforFragment += "3일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf3Am;
        println("3일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt3Am);
        msgforFragment += "\n3일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt3Am;
        println("3일 후 오후 날씨예보 : " + weather.response.body.items.item.get(0).wf3Pm);
        msgforFragment += "\n3일 후 오후 날씨예보 : " + weather.response.body.items.item.get(0).wf3Pm;
        println("3일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt3Pm);
        msgforFragment += "\n3일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt3Pm;
        println("4일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf4Am);
        msgforFragment += "\n4일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf4Am;
        println("4일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt4Am);
        msgforFragment += "\n4일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt4Am;
        println("4일 후 오후 날씨예보 : " + weather.response.body.items.item.get(0).wf4Pm);
        msgforFragment += "\n4일 후 오후 날씨예보 : " + weather.response.body.items.item.get(0).wf4Pm;
        println("4일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt4Pm);
        msgforFragment += "\n4일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt4Pm;
        println("5일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf5Am);
        msgforFragment += "\n5일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf5Am;
        println("5일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt5Am);
        msgforFragment += "\n5일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt5Am;
        println("5일 후 오후 날씨예보 : " + weather.response.body.items.item.get(0).wf5Pm);
        msgforFragment +="\n5일 후 오후 날씨예보 : " + weather.response.body.items.item.get(0).wf5Pm;
        println("5일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt5Pm);
        msgforFragment +="\n5일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt5Pm;
        println("6일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf6Am);
        msgforFragment +="\n6일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf6Am;
        println("6일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt6Am);
        msgforFragment +="\n6일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt6Am;
        println("6일 후 오후 날씨예보 : " + weather.response.body.items.item.get(0).wf6Pm);
        msgforFragment +="\n6일 후 오후 날씨예보 : " + weather.response.body.items.item.get(0).wf6Pm;
        println("6일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt6Pm);
        msgforFragment +="\n6일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt6Pm;
        println("7일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf7Am);
        msgforFragment +="\n7일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf7Am;
        println("7일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt7Am);
        msgforFragment +="\n7일 후 오전 강수 확률 : " + weather.response.body.items.item.get(0).rnSt7Am;
        println("7일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf7Pm);
        msgforFragment +="\n7일 후 오전 날씨예보 : " + weather.response.body.items.item.get(0).wf7Pm;
        println("7일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt7Pm);
        msgforFragment +="\n7일 후 오후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt7Pm;
        println("8일 후 날씨예보 : " + weather.response.body.items.item.get(0).wf8);
        msgforFragment +="\n8일 후 날씨예보 : " + weather.response.body.items.item.get(0).wf8;
        println("8일 후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt8);
        msgforFragment +="\n8일 후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt8;
        println("9일 후 날씨예보 : " + weather.response.body.items.item.get(0).wf9);
        msgforFragment +="\n9일 후 날씨예보 : " + weather.response.body.items.item.get(0).wf9;
        println("9일 후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt9);
        msgforFragment +="\n9일 후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt9;
        println("10일 후 날씨예보 : " + weather.response.body.items.item.get(0).wf10);
        msgforFragment +="\n10일 후 날씨예보 : " + weather.response.body.items.item.get(0).wf10;
        println("10일 후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt10);
        msgforFragment +="\n10일 후 강수 확률 : " + weather.response.body.items.item.get(0).rnSt10;
        SendText(msgforFragment);

    }

    private void println(final String str) {
        //textView2.append(str+"\n");

    }

    public void SendText(String s) {
        viewerFragment.printText(s);
    }
}