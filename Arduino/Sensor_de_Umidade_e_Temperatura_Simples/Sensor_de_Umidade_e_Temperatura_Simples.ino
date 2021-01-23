#include "dht.h" //Inclusão da biblioteca

const int pinoDHT11 = A2; // DEFINE O PINO ANALÓGICO UTILIZADO PELO DHT11 PARA A LEITURA NO MONITOR SERIAL
 
dht DHT; //VARIÁVEL DO TIPO DHT
 
void setup(){
  Serial.begin(9600); //INICIALIZA A PORTA DE COMUNICAÇÃO 9600
  delay(2000); //INTERVALO DE 2 SEGUNDO ANTES DE INICIAR
}
 
void loop(){
  DHT.read11(pinoDHT11); //LÊ AS INFORMAÇÕES DO SENSOR
  Serial.print("Umidade: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(DHT.humidity); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO
  Serial.print("%"); //ESCREVE O TEXTO EM SEGUIDA
  Serial.print(" / Temperatura: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(DHT.temperature, 0); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO E REMOVE A PARTE DECIMAL
  Serial.println("*C"); //IMPRIME O TEXTO NA SERIAL
  delay(500); //INTERVALO DE 0,5 SEGUNDOS * NÃO DIMINUIR ESSE VALOR
}
