#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import package
import paho.mqtt.client as mqtt
#add for output
import RPi.GPIO as GPIO


# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "room/lamp"
#
windowLamp = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(windowLamp, GPIO.OUT)
try:
  # Define on connect event function
  # We shall subscribe to our Topic in this function
  def on_connect(self,mosq, obj, rc):
     mqttc.subscribe(MQTT_TOPIC, 0)
     print("Connect on "+MQTT_HOST)
  # Define on_message event function. 
  # This function will be invoked every time,
  # a new message arrives for the subscribed topic 
  def on_message(mosq, obj, msg):
     if (msg.payload=='ON'):
           GPIO.output(windowLamp,True)
           print 'lamp aan'
           print "Topic: " + str(msg.topic)
           print "QoS: " + str(msg.qos)
     if (msg.payload=='OFF'):
           GPIO.output(windowLamp,False)
           print 'lamp uit'
           print "Topic: " + str(msg.topic)
           print "QoS: " + str(msg.qos)

  def on_subscribe(mosq, obj, mid, granted_qos):
          print("Subscribed to Topic: " + 
          MQTT_TOPIC + " with QoS: " + str(granted_qos))

    # Initiate MQTT Client
  mqttc = mqtt.Client()

    # Assign event callbacks
  mqttc.on_message = on_message
  mqttc.on_connect = on_connect
  mqttc.on_subscribe = on_subscribe

    # Connect with MQTT Broker
  mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    # Continue monitoring the incoming messages for subscribed topic
  mqttc.loop_forever()

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C
    GPIO.cleanup()  
#finally:  
    #GPIO.cleanup() # this ensures a clean exit  
