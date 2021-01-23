// Controlar um LED através da saída digital

int LED = 13; // Saída 13 do Arduino.


void setup() {
  // O comando abaixo é desnecessário caso o modo seja o DEFAULT
  analogReference(DEFAULT);

  // Cria a comunicação serial para exibir os valores no monitor serial
  Serial.begin(9600);
  
pinMode (LED, OUTPUT); // Define o pino de saída
}
void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(LED,HIGH); //Acende o LED (Nível 1 do pino)

float tensao = analogRead(A0);
tensao = tensao*5/1023;

//Exibe o valor lido
Serial.println(tensao);
//cria um atraso em cada medida
delay(100);

}
