#include "PID_lib.h"

int temp2analog(int temp){
  return temp*2 + 103;
}

PID pid_controller(3, 7, 10, 0, 4, 100);
void setup() {
  Serial.begin(9600);
  pid_controller.setAim(temp2analog(35));
}

void loop() {
  int output;
  output = pid_controller.readData();
  int power = pid_controller.calculateOutput();
  pid_controller.setOutput();
  Serial.println("st");
  Serial.println(output);
  Serial.println(millis());
  pid_controller.wait();
}
