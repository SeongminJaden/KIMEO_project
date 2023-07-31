int relay = 10; // Use Pin 10 as our Input

void setup() {
  pinMode(relay, OUTPUT);
}

void loop() {
  analogWrite(relay, HIGH);
  delay(2000);
  analogWrite(relay, LOW);
  delay(2000);
}
