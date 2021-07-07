byte motor=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  motor=70;
  Serial.write(motor);
  motor=180;
  Serial.write(motor);
}
