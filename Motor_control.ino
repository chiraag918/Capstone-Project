void setup() {
  // put your setup code here, to run once:
    Serial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    byte motor1=64,motor2=192;
    
    data=Serial.read();
  
    if(data==49)
    {
     motor1=70;
     motor2=180;
     Serial.write(motor1);
     Serial.write(motor2);
    }
    else if(data==50)
    {
     motor1=70;
     motor2=192;
     Serial.write(motor1);
     Serial.write(motor2);
    }
    else if(data==51)
    {
     motor1=64;
     motor2=180;
     Serial.write(motor1);
     Serial.write(motor2);
    }
    else if(data==52)
    {
     motor1=64;
     motor2=192;
     Serial.write(motor1);
     Serial.write(motor2);
    }
    else
    {
     motor1=64;
     motor2=192;
     Serial.write(motor1);
     Serial.write(motor2);
    }
}
}
