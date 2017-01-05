#include "PID_lib.h"

PID::PID(int pinOtput, int pinInput, int kp, int kd, int ki, int period){
  _period = period + 100;
  calculateVariables(kp, kd, ki);
  _pinInput = pinInput;
  _pinOutput = pinOtput;
  

}

int PID::readData(){
  return data = analogRead(_pinInput);
}

int PID::calculateOutput(){
  error_signal[2] = error_signal[1];
  error_signal[1] = error_signal[0];
  error_signal[0] = aim - data;
  output_val[1] = output_val[0];
  output_val[0] = output_val[1] + q_values[0]*error_signal[0] + q_values[1]*error_signal[1] + q_values[2]*error_signal[2];
  if(output_val[0] > 255){
    output_val[0] = 255;
  }
  if(output_val[0] < 0){
    output_val[0] = 0;
  }
  return output_val[0];
}

void PID::setOutput() {
  analogWrite(_pinOutput, output_val[0]);
}
void PID::wait() {
  delay(_period);
}

void PID::calculateVariables(int kp, int kd, int ki){
  float delay_s =(float) _period / 1000.0;
  q_values[0] = round(kp*(1.0+kd/(delay_s)));
  q_values[1] = round(kp*(-1 + delay_s*ki/2.0 - 2*kd/(delay_s)));
  q_values[2] = round(kp*(ki*delay_s/2 + kd/delay_s));
}

void PID::setVariables(int kp, int kd, int ki) {
  calculateVariables(kp, kd, ki);
}

void PID::setAim(int temp){
  aim = temp;
}

