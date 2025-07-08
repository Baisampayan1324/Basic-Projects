package com.example.to_dolist.Adapter;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.CompoundButton;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.to_dolist.AddNewTask;
import com.example.to_dolist.MainActivity;
import com.example.to_dolist.Model.ToDoModel;
import com.example.to_dolist.R;
import com.example.to_dolist.Utils.DataBaseHelper;

import java.util.List;

public class ToDoAdapter extends RecyclerView.Adapter<ToDoAdapter.MyViewHolder> {
    private List<ToDoModel> mList; // List of tasks
    private MainActivity activity; // MainActivity reference
    private DataBaseHelper myDB; // Database helper

    // Constructor
    public ToDoAdapter(DataBaseHelper myDB, MainActivity activity) {
        this.activity = activity;
        this.myDB = myDB;
    }

    // Inflate the task layout and create a ViewHolder
    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.task_layout, parent, false);
        return new MyViewHolder(v);
    }

    // Bind the data to the ViewHolder
    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        final ToDoModel item = mList.get(position); // Get the task at the current position
        holder.checkBox.setText(item.getTask()); // Set the task text
        holder.checkBox.setChecked(toBoolean(item.getStatus())); // Set the checkbox status

        // Handle checkbox state changes
        holder.checkBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean isChecked) {
                if (isChecked) {
                    myDB.updateStatus(item.getId(), 1); // Mark task as completed
                } else {
                    myDB.updateStatus(item.getId(), 0); // Mark task as not completed
                }
            }
        });
    }

    // Convert integer status to boolean
    public boolean toBoolean(int num) {
        return num != 0;
    }

    // Get the context
    public Context getContext() {
        return activity;
    }

    // Return the size of the task list
    @Override
    public int getItemCount() {
        return mList != null ? mList.size() : 0;
    }

    // Set the task list and refresh the adapter
    public void setTask(List<ToDoModel> mList) {
        this.mList = mList;
        notifyDataSetChanged();
    }

    // Delete a task
    public void deleteTask(int position) {
        ToDoModel item = mList.get(position); // Get the task to delete
        myDB.deleteTask(item.getId()); // Delete from the database
        mList.remove(position); // Remove from the list
        notifyItemRemoved(position); // Notify adapter
    }

    // Edit a task
    public void editTask(int position) {
        ToDoModel item = mList.get(position); // Get the task to edit
        Bundle bundle = new Bundle();
        bundle.putInt("Id", item.getId()); // Pass the task ID
        bundle.putString("task", item.getTask()); // Pass the task text

        AddNewTask task = new AddNewTask(); // Create the AddNewTask dialog
        task.setArguments(bundle); // Set arguments
        task.show(activity.getSupportFragmentManager(), task.getTag()); // Show the dialog
    }

    // ViewHolder class
    public static class MyViewHolder extends RecyclerView.ViewHolder {
        CheckBox checkBox;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            checkBox = itemView.findViewById(R.id.checkbox); // Initialize the checkbox
        }
    }
}
