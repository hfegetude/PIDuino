#include "PID_lib.h"

int temp2analog(int temp){
  return temp*2 + 103;
}

PID pid_controller(3, 7, 20, 20, 20, 500);
void setup() {
  Serial.begin(9600);
  pid_controller.setAim(temp2analog(35));
}

void loop() {
  int output;
  output = pid_controller.readData();
  pid_controller.calculateOutput();
  pid_controller.setOutput();
  Serial.print("output "); Serial.println(output);
  pid_controller.wait();
}
