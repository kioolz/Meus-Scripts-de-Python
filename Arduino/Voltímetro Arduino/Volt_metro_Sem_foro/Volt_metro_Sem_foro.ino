// Controlar um LED através da saída digital

int LED = 13; // Saída 13 do Arduino.
int LEDi = 12;
int LEDii = 11;

void setup() {
  // put your setup code here, to run once:
  // O comando abaixo é desnecessário caso o modo seja o DEFAULT
  analogReference(DEFAULT);

  // Cria a comunicação serial para exibir os valores no monitor serial
  Serial.begin(9600);
  
pinMode (LED, OUTPUT); // Define o pino de saída
pinMode (LEDi, OUTPUT);
pinMode (LEDii, OUTPUT);

}
void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(LED,HIGH); //Acende o LED (Nível 1 do pino)
digitalWrite(LEDi, HIGH);
digitalWrite(LEDii, HIGH);

float tensao = analogRead(A0);
float tensoa = analogRead(A1);
float tenaos = analogRead(A2);
tensao = tensao*((5-3)/1023);
tensoa = tensoa*((5)/1023);
tenaos = tenaos*((5)/1023);

//Exibe o valor lido
Serial.println(tensao);
delay(100);
Serial.println(tensoa);
delay(100);
Serial.println(tenaos);
//cria um atraso em cada medida
delay(100);

}
