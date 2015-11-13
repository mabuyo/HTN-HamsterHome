#include "Timer.h"
#include <Servo.h>

//water sensor variables
const int TEN_ML_PIN = 0;
const int THIRTY_ML_PIN = 1;
const int FIFTY_ML_PIN = 2;
int waterLevel;

// wheel sensor variables
const int TRIG_PIN = 3;
const int ECHO_PIN = 2;
int oldBinaryWheelValue = 0;
int newBinaryWheelValue = 0;
int quarterTurns = 0;
int fullTurns = 0;
int state;
int changeState = 0;
Timer t;

//*incoming data variables
char incomingChar;

//motor jazz
Servo myServo;
 
 
 
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  Serial.println("hello");
  
  // wheel sensor setup
  pinMode(TRIG_PIN,OUTPUT);
  pinMode(ECHO_PIN,INPUT);
  t.every(1000,uploadTurns);
  t.every(1000,checkWaterLevel);
  
  long duration, distanceCm;
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN,HIGH);
  // convert the time into a distance
  distanceCm = duration / 29.1 / 2 ;
  Serial.print("distance: ");
  Serial.println(distanceCm);
  //delay(10);
  if ((distanceCm <= 0)  || distanceCm >= 8){
    state = 0;
  } else {
    state = 1;
  }
  Serial.print(state);
  // Water sensor setup
  pinMode(TEN_ML_PIN,INPUT);
  pinMode(THIRTY_ML_PIN,INPUT);
  pinMode(FIFTY_ML_PIN,INPUT);
  Serial.flush();
  
  // Motor setup
  myServo.attach(9);
  myServo.write(90);


  }
 
 
 
void loop() {
  /************************** Wheel Sensor***************************/
  /******************************************************************/
  long duration, distanceCm;
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN,HIGH);
  // convert the time into a distance
  distanceCm = duration / 29.1 / 2 ;
  delay(10);
  //Serial.print("distance: ");
  //Serial.println(distanceCm);
  if ((distanceCm <= 0)  || distanceCm >= 6){
    newBinaryWheelValue = 0;
  } else {
    newBinaryWheelValue = 1;
  }
  //Serial.print("binary value:  ");
  //Serial.println(newBinaryWheelValue);
  if(newBinaryWheelValue != state) { //changed states
    changeState += 1;
  } else if (newBinaryWheelValue == state) {
    changeState = 0;
  }
  //Serial.print("changeState: ");
  //  Serial.print(changeState);
  if (changeState >= 2) {
    quarterTurns = quarterTurns + 1;
    //Serial.print("quarter turns:  ");
    //Serial.println(quarterTurns);
    state = newBinaryWheelValue;
    changeState = 0;
  }

  if(quarterTurns == 4) {
    fullTurns = fullTurns + 1;
    Serial.println(fullTurns); 
    quarterTurns = 0;
  }
 t.update();


  /**************************Incoming Data***************************/
  /******************************************************************/
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingChar = Serial.read();
    Serial.println(incomingChar);
    if (incomingChar == 'f') {
      feedHamster();
    }
  }
  
  
  

}




void uploadTurns() {
  Serial.print("/T");
  Serial.print(fullTurns);
  Serial.println("");
  fullTurns = 0;
}

void feedHamster() {
  myServo.write(100);
  delay(500);
  myServo.write(90);
}

void checkWaterLevel() {
  int tenML1 = analogRead(TEN_ML_PIN);
  int tenML2 = analogRead(TEN_ML_PIN);
  int tenML3 = analogRead(TEN_ML_PIN);
  int tenML4 = analogRead(TEN_ML_PIN);
  int tenML5 = analogRead(TEN_ML_PIN);
  int tenMLAve  = (tenML1 + tenML2 + tenML3 + tenML4 + tenML5)/5; 
  
  int thirtyML1 = analogRead(THIRTY_ML_PIN);
  int thirtyML2 = analogRead(THIRTY_ML_PIN);
  int thirtyML3 = analogRead(THIRTY_ML_PIN);
  int thirtyML4 = analogRead(THIRTY_ML_PIN);
  int thirtyML5 = analogRead(THIRTY_ML_PIN);
  int thirtyMLAve  = (thirtyML1 + thirtyML2 + thirtyML3 + thirtyML4 + thirtyML5)/5; 
  
  int fiftyML1 = analogRead(FIFTY_ML_PIN);
  int fiftyML2 = analogRead(FIFTY_ML_PIN);
  int fiftyML3 = analogRead(FIFTY_ML_PIN);
  int fiftyML4 = analogRead(FIFTY_ML_PIN);
  int fiftyML5 = analogRead(FIFTY_ML_PIN);
  int fiftyMLAve  = (fiftyML1 + fiftyML2 + fiftyML3 + fiftyML4 + fiftyML5)/5; 
  
  if (tenMLAve < 860) {
    waterLevel = 0;
  } else if (thirtyMLAve < 860) {
    waterLevel = 1;
  } else if (fiftyMLAve < 860) {
    waterLevel = 2;
  } else {
    waterLevel = 3;
  }
  Serial.print("/W");
  Serial.print(waterLevel);
  Serial.println("");
  
}

