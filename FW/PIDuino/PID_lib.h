#ifndef PID_lib_h
#define PID_lib_h
#include "Arduino.h"

class PID {
public:
  int error_signal[3];
  int output_val[2];
  int q_values[3];
  int data;
  int aim;
  int _pinInput;
  int _pinOutput;
  int _period;
  PID(int pinOtput, int pinInput, int kp, int kn, int kd, int period);
  int readData();
  int calculateOutput();
  void setOutput();
  void wait();
  void setVariables(int kp, int kd, int ki);
  void setAim(int temp);
private:
  void calculateVariables(int kp, int kd, int ki);
};
#endif
