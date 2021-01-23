int Verde = 11;
int Vermelho = 10
;
int Amarelo = 12;
int AzulBranco = 13;


void setup() {
  // put your setup code here, to run once:



pinMode(Verde, OUTPUT);
pinMode(Amarelo, OUTPUT);
pinMode(Vermelho, OUTPUT);
pinMode(AzulBranco, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

 //Acendendo o LED um de cada vez até que todos estejam acesos 
 digitalWrite(Vermelho, HIGH); //Acende os LEDS vermelhos
 delay(100);
 digitalWrite(Verde, HIGH); //Acende a luz verde
 delay(100);
 digitalWrite(Amarelo, HIGH); //Acende a luz amarela
 delay(100);
 digitalWrite(AzulBranco, HIGH);//Acende a luz branca e azul
 delay(100);

 // Ao fim de 10 segundos, todos são apagados de uma vez
 digitalWrite(Vermelho,LOW);
 digitalWrite(Verde, LOW);
 digitalWrite(Amarelo, LOW);
 digitalWrite(AzulBranco, LOW);
 delay(100);

 //Daí eu torno a acender um por 1 a cada 2,5 seg
 digitalWrite(Vermelho, HIGH); //Acende os LEDS vermelhos
 delay(100);
 digitalWrite(Verde, HIGH); //Acende a luz verde
 delay(100);
 digitalWrite(Amarelo, HIGH); //Acende a luz amarela
 delay(100);
 digitalWrite(AzulBranco, HIGH);//Acende a luz branca e azul
 delay(100);

 
 //Então vou apagando um de cada vez 
 digitalWrite(Vermelho, LOW);
 delay(100);
 digitalWrite(Verde, LOW);
 delay(100);
 digitalWrite(Amarelo, LOW);
 delay(100);
 digitalWrite(AzulBranco, LOW);
 delay(100);

 //Depois acendo todos de uma vez
 digitalWrite(Vermelho,HIGH);
 digitalWrite(Verde, HIGH);
 digitalWrite(Amarelo, HIGH);
 digitalWrite(AzulBranco, HIGH);
 delay(100);

 // E apago todos de uma vez
 digitalWrite(Vermelho,LOW);
 digitalWrite(Verde, LOW);
 digitalWrite(Amarelo, LOW);
 digitalWrite(AzulBranco, LOW);
 
 // Torno a acender um de cada vez
 digitalWrite(Vermelho, HIGH); //Acende os LEDS vermelhos
 delay(100);
 digitalWrite(Verde, HIGH); //Acende a luz verde
 delay(100);
 digitalWrite(Amarelo, HIGH); //Acende a luz amarela
 delay(100);

 //Porém no último, vou acender o azul enquanto apago o vermelho
 digitalWrite(AzulBranco, HIGH);//Acende a luz branca e azul
 digitalWrite(Vermelho, LOW);
 delay(100);







}
