%Paso temporal
numPasos=10000;
step=20*pi/numPasos;

%Matriz A
A=[[0,1];[-1,0]];

%Definición de vectores y condiciones iniciales
U=zeros(2*numPasos,1);
X=zeros(numPasos,1);
V=zeros(numPasos,1);
U(1,1)=1;
U(2,1)=0;
X(1,1)=1;
V(1,1)=0;

%Integrador de Euler
for i = 1:numPasos
    Un=A*([U(2*i-1,1);U(2*i,1)]);
    U(2*i+1,1)=Un(1,1);
    X(i+1)=Un(1,1);
    U(2*i+2,1)=Un(2,1);
    V(i+1)=Un(2,1);
    
end

figure
plot(X,V)
title('Órbita')
xlabel('X(t)')
ylabel('V(t)')
grid on

t=(1:1:100);
figure
plot(t,X(1:100))
title('Oscilador')
xlabel('t')
ylabel('X(t)')
grid on 
