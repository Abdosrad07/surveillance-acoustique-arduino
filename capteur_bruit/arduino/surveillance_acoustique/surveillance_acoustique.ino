#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16,2);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Station bruit");
}

void loop() {
  // put your main code here, to run repeatedly:
  int bruit = analogRead(A0);
  Serial.println(bruit);
  lcd.setCursor(0,1);
  lcd.print("Niveau; ");
  lcd.print(bruit);
  lcd.print("   ");
  delay(200);
}
