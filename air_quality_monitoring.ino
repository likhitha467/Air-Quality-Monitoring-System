
const int gasPin = A0;
const int greenLED = 7;
const int redLED = 8;

int gasValue = 0;
const int threshold = 500;

void setup() {
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  gasValue = analogRead(gasPin);

  Serial.print("Simulated Gas Sensor Value: ");
  Serial.println(gasValue);

  if (gasValue < threshold) {
    digitalWrite(greenLED, HIGH);
    digitalWrite(redLED, LOW);

    Serial.println("Status: NORMAL");
  }
  else {
    digitalWrite(greenLED, LOW);
    digitalWrite(redLED, HIGH);

    Serial.println("Status: HIGH INPUT");
  }

  delay(1000);
}
