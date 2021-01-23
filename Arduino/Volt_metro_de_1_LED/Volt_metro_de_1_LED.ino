void setup() {
  // O comando abaixo é desnecessário caso o modo seja o DEFAULT
  analogReference(DEFAULT);

  // Cria a comunicação serial para exibir os valores no monitor serial
  Serial.begin(9600);
}

void loop() {
  // Mede o valor de 0 a 1023 e converte para tensão
  float tensao = analogRead(A0);
  tensao = tensao*5/1023;

  // Exibe o valor lido
  Serial.println(tensao);

  // Cria um pequeno atraso entre cada medição
  delay(100);
}
