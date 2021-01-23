void setup() { 

  // O comando abaixo é desnecessário caso o modo seja DEFAULT

  //Comunicação com a porta lógica 9600 do ARduino com o Monitor Serial
  Serial.begin(9600);

}

// Inicio do codigo
void loop(){

  //Le a tensao como uma variavel real
  float quedatensaoresistor = analogRead(A0);
  //Escreve uma equação para a variavel real
  quedatensaoresistor = quedatensaoresistor*5/1023;


  //Exibe o valor lido na tela
  Serial.println(quedatensaoresistor);

  delay(100);
}
