byte  motor=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  /*
  motor = 'a';
  motor=Serial.read();
  */
  if(Serial.available() > 0)
  {
    byte data=0,motor1=64,motor2=192;
    data=Serial.read();
    Serial.write(data);
   Serial.print("You sent me: ");
   Serial.println(data);
    
  }
  

}
