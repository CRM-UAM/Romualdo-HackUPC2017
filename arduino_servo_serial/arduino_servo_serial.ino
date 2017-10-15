#include <Servo.h>

Servo myservo;

void setup() {
  delay(1000);
  Serial.begin(115200);
  myservo.attach(8);
}

int pos = 0;

void loop() {
  int target = Serial.parseInt();
  if(target > 0) {
    if(target > 170) target = 170;
    while(pos < target) {
      pos++;
      myservo.write(pos);
      //delay(3);
    }
    while(pos > target) {
      pos--;
      myservo.write(pos);
      //delay(3);
    }
  }
}
