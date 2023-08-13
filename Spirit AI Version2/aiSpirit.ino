const int ledPin = 3;  // Pin to which the LED is connected

void setup() {
  Serial.begin(9600);  // Start serial communication
  pinMode(ledPin, OUTPUT);  // Set the LED pin as an output
}

void loop() {
  if (Serial.available() > 0) {  // If data is available to read
    char command = Serial.read();  // Read the incoming data

    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
      Serial.println("Lights turned on");
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);  // Turn off the LED
      Serial.println("Lights turned off");
    }
  }
}
