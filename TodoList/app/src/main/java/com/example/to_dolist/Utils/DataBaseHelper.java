package com.example.to_dolist.Utils;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import com.example.to_dolist.Model.ToDoModel;

import java.util.ArrayList;
import java.util.List;

public class DataBaseHelper extends SQLiteOpenHelper {

    private static final String DATABASE_NAME = "TODO_DATABASE";
    private static final String TABLE_NAME = "TASKS";  // Changed TABLE_NAME to TASKS for clarity
    private static final String COL_1 = "ID";
    private static final String COL_2 = "TASK";
    private static final String COL_3 = "STATUS";
    private static final int DATABASE_VERSION = 1;

    // Constructor
    public DataBaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase) {
        // Create table query
        String createTableQuery = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " (" +
                COL_1 + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_2 + " TEXT, " +
                COL_3 + " INTEGER)";
        sqLiteDatabase.execSQL(createTableQuery);
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int oldVersion, int newVersion) {
        // Drop and recreate table if database version changes
        sqLiteDatabase.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
        onCreate(sqLiteDatabase);
    }

    // Insert a new task into the database
    public void insertTask(ToDoModel model) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(COL_2, model.getTask());
        contentValues.put(COL_3, 0); // Default status as 0 (incomplete)

        db.insert(TABLE_NAME, null, contentValues);
    }

    // Update an existing task by ID
    public void updateTask(int id, String task) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(COL_2, task);

        db.update(TABLE_NAME, contentValues, COL_1 + "=?", new String[]{String.valueOf(id)});
    }

    // Update the status of a task (completed or not)
    public void updateStatus(int id, int status) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(COL_3, status);

        db.update(TABLE_NAME, contentValues, COL_1 + "=?", new String[]{String.valueOf(id)});
    }

    // Delete a task by ID
    public void deleteTask(int id) {
        SQLiteDatabase db = this.getWritableDatabase();
        db.delete(TABLE_NAME, COL_1 + "=?", new String[]{String.valueOf(id)});
    }

    // Get all tasks from the database
    public List<ToDoModel> getAllTask() {
        SQLiteDatabase db = this.getWritableDatabase();
        List<ToDoModel> taskList = new ArrayList<>();
        Cursor cursor = null;

        try {
            cursor = db.query(TABLE_NAME, null, null, null, null, null, null);
            if (cursor != null && cursor.moveToFirst()) {
                do {
                    ToDoModel toDoModel = new ToDoModel();
                    toDoModel.setId(cursor.getInt(cursor.getColumnIndex(COL_1)));
                    toDoModel.setTask(cursor.getString(cursor.getColumnIndex(COL_2)));
                    toDoModel.setStatus(cursor.getInt(cursor.getColumnIndex(COL_3)));
                    taskList.add(toDoModel);
                } while (cursor.moveToNext());
            }
        } finally {
            if (cursor != null) {
                cursor.close();
            }
        }

        return taskList;
    }
}
