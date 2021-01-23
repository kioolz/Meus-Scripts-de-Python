// Projeto 3 - Semáforo

int ledDelay = 1000;
int Vermelho = 12;
int Verde = 11;
int Amarelo = 13;
int AzulBranco = 10;




void setup() {
  
// Liberando 5V de tensão para as entradas dos LEDs
pinMode(Vermelho, OUTPUT);
pinMode(Amarelo, OUTPUT);
pinMode(Verde, OUTPUT);
pinMode(AzulBranco, OUTPUT);
}

void loop() {
  digitalWrite(Vermelho, HIGH); //Acende os LEDS vermelhos
  delay(ledDelay); //Espera 1 segundo ou 1000miliseg

  digitalWrite(Amarelo, HIGH); //Acende o amarelo depois de 1seg
  delay(2000); //Espera 2 segundos

  digitalWrite(Verde, HIGH); //Acende a luz verde
  digitalWrite(Vermelho, LOW); //Apaga a luz vermelha
  digitalWrite(Amarelo, LOW); // Apaga a luz amarela
  digitalWrite(AzulBranco, HIGH);//Acende a luz branca e azul
  delay(ledDelay); // Espera o tempo da variável ledDelay

  digitalWrite(Amarelo, HIGH); //Acende a luz Amarela
  digitalWrite(AzulBranco, LOW);// Apaga a luz branca&azul
  delay(2000);

  digitalWrite(Amarelo, LOW); // Apaga a luz amarela

}
