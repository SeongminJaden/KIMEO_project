String inByteString;         // incoming serial byte
bool newByteComing = false;
char myString[10] = "";
int inByte;
int counter = 0;

void setup() {
  // start serial port at 9600 bps and wait for port to open:
  pinMode(13, OUTPUT);
  Serial.begin(9600, SERIAL_8N1);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }


}

void loop() {
  // if we get a valid byte, read analog ins:
  while (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();
    Serial.println(inByte,DEC);
    char inByteChar = (char) inByte;
    Serial.println(inByteChar);
    Serial.println(" from arduino");
    //Serial.print(inByte,DEC);
    newByteComing = true;
    myString[counter] = inByteChar;
    counter++;
    delay(50);
  }
  if(newByteComing){
    for(int i=0;i<10;i++){
      Serial.println("print string");
      Serial.println(myString[i]);
    }
    Serial.println(myString);
    char char1 = myString[0] ;
    if(strcmp (myString,"lightOn") == 0){
      Serial.println("lightwork on with strcmp");
      digitalWrite(13, HIGH);
    }
    if(strcmp (myString,"lightOff") == 0){
      Serial.println("lightwork off with strcmp");
      digitalWrite(13, LOW);
    }
    /*if(strcmp (char1,"L") == 0){
      Serial.println("lightwork with array");
    }*/
    /*if(inByte == "lightOn"){
      Serial.print(" turn on");
      digitalWrite(13, HIGH);
    }else if (inByte == "lightOff"){
      Serial.print(" turn off");
      digitalWrite(13, LOW);
    }*/
    newByteComing = false;
    counter = 0;
    for(int i=0;i<10;i++){
      myString[i] = (char)0;
    }
  }
}


/*
Processing code to run with this example:

// This example code is in the public domain.

import processing.serial.*;     // import the Processing serial library
Serial myPort;                  // The serial port

float bgcolor;      // Background color
float fgcolor;      // Fill color
float xpos, ypos;         // Starting position of the ball

void setup() {
  size(640,480);

  // List all the available serial ports
 // if using Processing 2.1 or later, use Serial.printArray()
  println(Serial.list());

  // I know that the first port in the serial list on my mac
  // is always my  Arduino module, so I open Serial.list()[0].
  // Change the 0 to the appropriate number of the serial port
  // that your microcontroller is attached to.
  myPort = new Serial(this, Serial.list()[0], 9600);

  // read bytes into a buffer until you get a linefeed (ASCII 10):
  myPort.bufferUntil('\n');

  // draw with smooth edges:
  smooth();
}

void draw() {
  background(bgcolor);
  fill(fgcolor);
  // Draw the shape
  ellipse(xpos, ypos, 20, 20);
}

// serialEvent  method is run automatically by the Processing applet
// whenever the buffer reaches the  byte value set in the bufferUntil()
// method in the setup():

void serialEvent(Serial myPort) {
  // read the serial buffer:
  String myString = myPort.readStringUntil('\n');
  // if you got any bytes other than the linefeed:
    myString = trim(myString);

    // split the string at the commas
    // and convert the sections into integers:
    int sensors[] = int(split(myString, ','));

    // print out the values you got:
    for (int sensorNum = 0; sensorNum < sensors.length; sensorNum++) {
      print("Sensor " + sensorNum + ": " + sensors[sensorNum] + "\t");
    }
    // add a linefeed after all the sensor values are printed:
    println();
    if (sensors.length > 1) {
      xpos = map(sensors[0], 0,1023,0,width);
      ypos = map(sensors[1], 0,1023,0,height);
      fgcolor = sensors[2];
    }
    // send a byte to ask for more data:
    myPort.write("A");
  }

*/
