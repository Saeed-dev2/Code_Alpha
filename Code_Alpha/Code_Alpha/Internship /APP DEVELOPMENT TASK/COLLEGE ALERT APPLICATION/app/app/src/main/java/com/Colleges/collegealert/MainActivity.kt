package com.example.collegealert

import android.app.AlarmManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity() {

    private lateinit var editTextEventName: EditText
    private lateinit var editTextEventTime: EditText
    private lateinit var buttonSetReminder: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        editTextEventName = findViewById(R.id.editTextEventName)
        editTextEventTime = findViewById(R.id.editTextEventTime)
        buttonSetReminder = findViewById(R.id.buttonSetReminder)

        buttonSetReminder.setOnClickListener {
            val eventName = editTextEventName.text.toString()
            val eventTime = editTextEventTime.text.toString()

            if (eventName.isNotEmpty() && eventTime.isNotEmpty()) {
                setEventReminder(eventName, eventTime)
            } else {
                Toast.makeText(this, "Please enter event name and time", Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun setEventReminder(eventName: String, eventTime: String) {
        val sdf = SimpleDateFormat("HH:mm", Locale.getDefault())
        val eventCalendar = Calendar.getInstance()
        
        try {
            eventCalendar.time = sdf.parse(eventTime)
            if (eventCalendar.before(Calendar.getInstance())) {
                eventCalendar.add(Calendar.DAY_OF_YEAR, 1) // Set for next day if time is passed
            }

            val alarmManager = getSystemService(Context.ALARM_SERVICE) as AlarmManager
            val intent = Intent(this, NotificationReceiver::class.java)
            intent.putExtra("eventName", eventName)

            val pendingIntent = PendingIntent.getBroadcast(this, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT)

            alarmManager.setExact(AlarmManager.RTC_WAKEUP, eventCalendar.timeInMillis, pendingIntent)

            Toast.makeText(this, "Reminder set for $eventName at $eventTime", Toast.LENGTH_SHORT).show()
        } catch (e: Exception) {
            Toast.makeText(this, "Invalid time format", Toast.LENGTH_SHORT).show()
        }
    }
}
