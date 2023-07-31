//Henry's Bench
//KY-031 Knock Sensor Tutorial

int knockPin = 10; // Use Pin 10 as our Input
int knockVal = 0;
unsigned long lastKnockTime; // Record the time that we measured a shock
int counter = 0;

int knockAlarmTime = 500; // Number of milli seconds to keep the knock alarm high


void setup ()
{
  Serial.begin(9600);  
  pinMode (knockPin, INPUT) ; // input from the KY-031
}
void loop ()
{
  knockVal = digitalRead(knockPin) ; // read KY-031 Value
  
  
  if(knockVal == 0){
    counter += 1;
    Serial.println(counter);
    delay(1000);
  }
}
