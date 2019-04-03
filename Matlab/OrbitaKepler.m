%Definición de constantes
G=1.0;
m1=1.0;
m2=0.001;
mu=G*(m1+m2);
N=10000;
t=linspace(0.0,100.0,N);

%Condiciones iniciales
y0=[1.0, 0.0, 0.0, 1.0];

% Integracion con 'ode45' 
orbit=@(t,U)[U(3);U(4);-mu*U(1)/(sqrt(U(1)^2+U(2)^2))^3;-mu*U(2)/(sqrt(U(1)^2+U(2)^2))^3];
[t,U]=ode45(orbit,t,y0);

r=U(:, 1:2);     % vector de posición                                                                      
v=U(:, 3:end);  % vector de velocidad   

%gráficos
figure
plot(r(:,1),r(:,2))
xlabel('x')
ylabel('y')
title('Órbita Kepleriana')
