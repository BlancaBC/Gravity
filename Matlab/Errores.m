%Definición de constantes
G = 1.0;
m1=1.0;
m2=0.001;
mu=G*(m1+m2);
N=10000;
t=linspace(0.0, 1000.0, N);
t2=linspace(0.0, 1000.0, 2 * N);

step1 = t(2) - t(1);
step2 = t2(2)- t(1);

%Orden del integrador
orden = 2;
%#Condiciones iniciales
y0=[1.0, 0.0, 0.0, 1.2];

%Condiciones uniciales para lo solución1
 
U = y0;

%Matriz con los resultados

Utotal1 = zeros(N,4); %Dimensiones de t
Utotal1(1,1:4) = U;

%Itengración con el primer step

for i = 1:(N) %Dimensiones de t
    F = func(U,mu);
    U = Runge_Kutta_2_orden(step1,F,U);
    Utotal1(i,1:4) = U;
end

sol1 = Utotal1(:,:) ;
%Condiciones iniciales para la solucion1
    
U = (y0);
F = func(y0,mu);
Utotal2 = zeros(2*N,4); %dimensiones de t2;
Utotal2(1,1:4) = U;

%Itengración con el segundo step
for i = 1:(2*N)
    F = func(U,mu);
    U = Runge_Kutta_2_orden(step2,F,U);
    Utotal2(i,1:4) = U;
end  

%Para comparar la sol1 con la sol2, necesito cada 2 elememtos
sol2 = Utotal2(1:2:end,:);

%Error mediante Richardson
E=zeros(N,4);
E(1:end,:)=(sol1-sol2)/(1-0.5^orden);

%Gráficas de resultados
figure
plot(t,abs(E(:,1)))
