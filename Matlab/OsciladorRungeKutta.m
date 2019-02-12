clear, clc
%Definición del paso de integración 
numPasos=10000;
paso_temp=20*pi/numPasos;

%Condiciones iniciales
Ut = [1;0];
U = zeros(numPasos*2,1);

for i = 1: numPasos
    F=oscilador(Ut);
    Ut = Runge_Kutta_2_orden(paso_temp,F,Ut);
    U(i*2-1:i*2) = Ut;
end

plot(U(1:2:numPasos),U(2:2:numPasos))
title('Órbita')
xlabel('X(t)')
ylabel('V(t)')
grid on


 


    

