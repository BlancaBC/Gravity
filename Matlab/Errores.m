%Definición de constantes
G = 1.0;
m1= 1.0;
m2= 0.001;
mu= G*(m1+m2);
N=10000;
t=linspace(0.0, 1000.0, N);
t2=linspace(0.0, 1000.0, 2 * N);
orden = 4; %Orden del integrador

%Condiciones iniciales
y0=[1.0, 0.0, 0.0, 1.2];

%Dimensionado de los vectores de estado
U1 = zeros(N,4);
U2 = zeros(2*N,4);

%Función de cálculo de la órbita
orbit=@(t,U)[U(3);U(4);-mu*U(1)/sqrt(U(1)^2+U(2)^2);-mu*U(2)/sqrt(U(1)^2+U(2)^2)];

%Itengración con el primer step
[t,U]=ode45(orbit,t,y0);
U1(:,1:4) = U;
sol1 = U1;

%Itengración con el segundo step
[t2,U]=ode45(orbit,t2,y0);
U2(:,1:4) = U;  
sol2 = U2(1:2:end,:); %cada dos elementos

%Error mediante Richardson
E=zeros(N,4);
E(1:end,:)=(sol1-sol2)/(1-0.5^orden);

%Gráficas de resultados
figure
plot(t,abs(E(:,1)))
xlabel('time')
ylabel('E')
title('Error')
