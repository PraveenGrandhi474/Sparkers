char t; //bluetooth received variable
int k,x=0,y=0,a=0,b=0,m,n; //location on map

#define RM 2
#define LM 4
#define RM1 3
#define LM1 5

void setup()
{
  pinMode(13,OUTPUT); // working indication
  pinMode(2,OUTPUT);  // Right Motor +
  pinMode(3,OUTPUT);  // Right Motor -
  pinMode(4,OUTPUT);  // Left Motor +
  pinMode(5,OUTPUT);  // Left Motor -
  pinMode(6,INPUT);   // IRL Input
  pinMode(7,INPUT);   // IRR Input
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(13,HIGH);
  delay(200);
  digitalWrite(13,LOW);
  delay(200);
  if(Serial.available())
  {
    t=Serial.read();
    switch(t)
    {
      case '0':
        a=0,b=0;
        break;
      case '1':
        a=0,b=1;
        break;
      case '2':
        a=0,b=2;
        break;
      case '3':
        a=1,b=0;
        break;
      case '4':
        a=1,b=1;
        break;
      case '5':
        a=1,b=2;
        break;
      case '6':
        a=2,b=0;
        break;
      case '7':
        a=2,b=1;
        break;
      case '8':
        a=2,b=2;
        break;
    }
    k=r(0,a);
    k=r(0,b);
    if(Serial.available())
      t=Serial.read();
    if(t=='9')
    {
      k=r(0,a);
      k=r(0,b);
    }
  }
}
int r(int m,int n)
{
  while(m<n)
  {
    if(digitalRead(6) and digitalRead(7))//both obstacles
    {
      digitalWrite(13,HIGH);
      digitalWrite(LM,HIGH);
      digitalWrite(LM1,LOW);
      digitalWrite(RM,HIGH);
      digitalWrite(RM1,LOW);
      delay(2000);
      digitalWrite(13,LOW);
      m++;
    }
    if(!digitalRead(6) and digitalRead(7))//right obstacle
    {
      digitalWrite(LM,HIGH);
      digitalWrite(LM1,LOW);  
      digitalWrite(RM,LOW);
      digitalWrite(RM1,HIGH);
    }
    if(digitalRead(6) and !digitalRead(7))//left obstacle
    {
      digitalWrite(LM,LOW);  
      digitalWrite(LM1,LOW);
      digitalWrite(RM,HIGH);
      digitalWrite(RM1,LOW);
    }
    if(!digitalRead(6) and !digitalRead(7))//no obstacles
    {  
      digitalWrite(LM,HIGH);
      digitalWrite(LM1,LOW);  
      digitalWrite(RM,HIGH);
      digitalWrite(RM1,LOW);
    }
  }
  digitalWrite(LM,HIGH);
  digitalWrite(LM1,LOW);  
  digitalWrite(RM,LOW);
  digitalWrite(RM1,LOW);
  digitalWrite(13,HIGH);
  delay(2000);
  digitalWrite(13,LOW);
  digitalWrite(LM,LOW);
  digitalWrite(LM1,LOW);
  digitalWrite(RM,LOW);
  digitalWrite(RM1,LOW);
  return 0;
}
