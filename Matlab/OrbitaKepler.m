%Definición de constantes
G=1.0;
m1=1.0;
m2=0.001;
mu=G*(m1+m2);
N=10000;
DeltaT=1000/N;
t=linspace(0.0,1000.0,N);

%Condiciones iniciales
y0=[1.0, 0.0, 0.0, 1.2];

% Integracion con 'ode45'                                                                                                 
[t,solucion]=ode45(@func,t,y0);
r=solucion(:, 1:2);     % vector de posición                                                                      
v=solucion(:, 2:end) ;    % vector de velocidad   

%gráficos
figure
plot(r(end,0),r(end,1))
xlabel('x')
ylabel('y')
title('Órbita Kepleriana')

figure
plot(r(end,0),v(end,0))
xlabel('x')
ylabel('v_x')
title('Velocidad orbital')

figure
plot(r(end,1),v(end,1))
xlabel('y')
ylabel('v_y')
title('Velocidad orbital')
