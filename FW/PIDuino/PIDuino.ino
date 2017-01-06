#include "PID_lib.h"

int temp2analog(int temp) {
  return temp * 2 + 103;
}
PID pid_controller(3, 7, 10, 0, 4, 100);
int aim = 35;
void setup() {
  Serial.begin(9600);
  pid_controller.setAim(temp2analog(aim));
}

void loop() {
  int output;
  char data_b[4];
  output = pid_controller.readData();
  int power = pid_controller.calculateOutput();
  pid_controller.setOutput();
  Serial.println("st");
  Serial.println(output);
  Serial.println(power);
  Serial.println(pid_controller.aim);
  Serial.println(millis());
  if(Serial.available() > 0){
    Serial.readBytes(data_b, 4);
    String buf2st(data_b);
    pid_controller.setAim(temp2analog(buf2st.toInt()/100)); 
  }
  pid_controller.wait();
}
