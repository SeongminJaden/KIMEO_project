String inByte;         // incoming serial byte
bool newByteComing = false;
int knockPin = 10; // Use Pin 10 as our Input
int knockVal = HIGH;
unsigned long lastKnockTime; // Record the time that we measured a shock
int knockAlarmTime = 10000; // Number of milli seconds to keep the knock alarm high
bool knockActive = true;
int ledRight = 9;
int ledLeft = 3;
int ledTest = 13;

int brightness = 0;    // how bright the LED is
int fadeAmount = 30;    // how many points to fade the LED by

bool turnOn = false;

void setup() {
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  pinMode(ledRight, OUTPUT);
  pinMode(ledLeft, OUTPUT);
  pinMode(ledTest, OUTPUT);
  pinMode (knockPin, INPUT) ; // input from the KY-031
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }


}

void loop() {
  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.readString();
    //Serial.print(inByte,DEC);
    newByteComing = true;
  }
  if(newByteComing){
    if(inByte == "lightOn"){
      digitalWrite(ledRight, HIGH);
      digitalWrite(ledLeft, HIGH);
      digitalWrite(ledTest, HIGH);
    }else if (inByte == "lightOff"){
      digitalWrite(ledRight, LOW);
      digitalWrite(ledLeft, LOW);
      digitalWrite(ledTest, LOW);
    }
    if(inByte == "lightOnSlow"){
      turnOn = true;
    }else if (inByte == "lightOffSlow"){
      turnOn = false;
    }
    else if (inByte == "knockActive"){
      knockActive = true;
    }
    else if (inByte == "knockDesactive"){
      knockActive = false;
    }
    newByteComing = false;
  }
  if(knockActive && millis() - lastKnockTime > knockAlarmTime){
    knockVal = digitalRead(knockPin) ;
    if(knockVal == LOW){
      Serial.println("knock");
      lastKnockTime = millis();
    }
  }
  if(brightness > 255){
    brightness = 255;
  }
  if(brightness < 0){
    brightness = 0;
  }
  if(turnOn && brightness < 255){
    analogWrite(ledRight, brightness);
    analogWrite(ledLeft, brightness);
    digitalWrite(ledTest, HIGH);
    delay(100);
  }
  if(!turnOn && brightness > 0){
    analogWrite(ledRight, brightness);
    analogWrite(ledLeft, brightness);
    digitalWrite(ledTest, LOW);
    delay(100);
  }
  
  //delay(20); //keep arduino calm no more for geet knock sensing
}

