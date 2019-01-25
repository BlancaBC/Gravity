clear, clc
%Definición del paso de integración 
numPasos=10000;
paso_temp=20*pi/numPasos;

%Condiciones iniciales
X0=1;
V0=0;

U = [X0;V0];
Utotal = zeros(numPasos*2,1);
F=oscilador(U);
X = zeros(numPasos,1);
V = zeros(numPasos,1);

for i = 1: numPasos
    F=oscilador(U);
    U = Runge_Kutta_2_orden(paso_temp,F,U);
    Utotal(i*2-1:i*2) = U;
    
    X(i) = Utotal(i*2-1);
    V(i) = Utotal(i*2);
end

plot(X,V)
title('Órbita')
xlabel('X(t)')
ylabel('V(t)')
grid on


 


    

