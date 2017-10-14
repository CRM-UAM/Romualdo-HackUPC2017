#include <Servo.h>

Servo myservo;

void setup() {
  delay(1000);
  Serial.begin(115200);
  myservo.attach(8);
}

void loop() {
  int pos = Serial.parseInt();
  if(pos > 0) {
    if(pos > 170) pos = 170;
    myservo.write(pos);
  }
}
