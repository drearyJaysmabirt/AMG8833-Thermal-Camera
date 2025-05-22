#include <Wire.h>
#include <Adafruit_AMG88xx.h>

Adafruit_AMG88xx amg;

void setup() {
  Serial.begin(115200);  // Faster baud rate
  while (!Serial);       // Wait for serial port
  
  if (!amg.begin()) {
    Serial.println("AMG88xx sensor error! Check wiring.");
    while (1);
  }
}

void loop() {
  float pixels[64];
  amg.readPixels(pixels);
  
  // Send data as CSV (for matplotlib)
  for (int i = 0; i < 64; i++) {
    Serial.print(pixels[i]);
    if (i < 63) Serial.print(",");  // No trailing comma
  }
  Serial.println();  // Newline after each frame
  delay(10);        // ~20 FPS (adjust as needed)
}