

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    static bool ledStatus = LOW;

    if (Serial.available())
    {
        char x = Serial.read();

        if (x == 'x') {
            if (ledStatus)
                ledStatus = LOW;
            else
                ledStatus = HIGH;
        }

        digitalWrite(13, ledStatus);
    }

    delay(20);
}
