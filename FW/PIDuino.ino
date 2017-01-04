void readTemperature(int pin){
  int volt;
  volt = analogRead(pin);
  s_vars.CurrentTemperature = volt /1000;
}

typedef struct SystemVars_t{
  double Pn0 = 0;
  double Pn1 = 0;
  double En0 = 0;
  double En1 = 0;
  double En2 = 0;
  double q0;
  double q1;
  double q2;
  double DesTemp;
  double CurrentTemperature;
} SystemVars;

int calculatePower(){
  s_vars.En0 = s_vars.DesTemp - s_vars.CurrentTemperature;
  double s_vars.Pn0 = s_vars.Pn1 + s_vars.q0*s_vars.En0 + s_vars.q1* s_vars.En1 +  s_vars.q2* s_vars.En2;

  if(s_vars.Pn0 > 255){
    s_vars.Pn0 = 255;
  }
  if (s.vars.Pn0 < 0) {
    s_vars.Pn0 = 0;
  }
  //Reorg
  s_vars.Pn1 = s_vars.Pn0;
  s_vars.En2 = s_vars.En1;
  s_vars.En1 = s_vars.En0;

}

void SetPower(){
  analogWrite(3, s_vars.Pn0)
}

void sendPowerData(){
  Serial.prinln(s_vars.Pn0);
}
SystemVars s_vars;
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  readData();
  calculatePower();
  setPower();
  sendPowerData();
  wait();
}
