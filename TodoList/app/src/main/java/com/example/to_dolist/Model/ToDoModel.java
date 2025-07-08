package com.example.to_dolist.Model;

public class ToDoModel {
    private String task;  // The task description
    private int id;       // The unique identifier for each task
    private int status;   // The status of the task (e.g., 0 for incomplete, 1 for complete)

    // Getter for the task description
    public String getTask() {
        return task;
    }

    // Setter for the task description
    public void setTask(String task) {
        this.task = task;
    }

    // Getter for the task ID
    public int getId() {
        return id;
    }

    // Setter for the task ID
    public void setId(int id) {
        this.id = id;
    }

    // Getter for the task status
    public int getStatus() {
        return status;
    }

    // Setter for the task status
    public void setStatus(int status) {
        this.status = status;
    }
}
