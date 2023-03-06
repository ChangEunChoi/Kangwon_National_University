package kr.ac.knu.cse.myapplication8;



import android.graphics.Movie;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class WeatherAdapter extends RecyclerView.Adapter<WeatherAdapter.ViewHolder>{
    ArrayList<Item> items = new ArrayList<Item>();

    //디버깅용 메서드
    public void checkArrayList(){
        for (int i =0; i< items.size();i++) {
            Log.d("check",""+ i);
        }
    }

    public void clearAll(){
        items.clear();
        notifyDataSetChanged();
    }
    @NonNull
    @Override
    //필요한 개수만큼만 뷰홀더 객체 생성하고 안쓰임
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View itemView = inflater.inflate(R.layout.weather_item,parent,false);

        return new ViewHolder(itemView);
    }


    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Item item = items.get(position);
        holder.setItem(item);//시스템이 알아서 적절한 차례의 뷰홀더 객체 제공
    }

    @Override
    public int getItemCount() {
        return items.size();
    }

    public void addItem(Item item){
        items.add(item);
    }

    public void setItems(ArrayList<Item> items){
        this.items = items;
    }

    public Item getItem(int position){
        return items.get(position);
    }



    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView textView,textView2,textViewDate;

        public ViewHolder(View itemView) {//onCreateViewHolder에서 필요한 수만큼만 사용되고 안쓰임
            super(itemView);

            textView = itemView.findViewById(R.id.textView);
            textView2 = itemView.findViewById(R.id.textView2);
            textViewDate = itemView.findViewById(R.id.textViewDate);
        }

        public void setItem(Item item){
            textView.setText(item.fcstValue);
            textView2.setText(item.fcstTime +"시");
            textViewDate.setText(item.fcstDate+"\n"+item.region);
        }
    }
}