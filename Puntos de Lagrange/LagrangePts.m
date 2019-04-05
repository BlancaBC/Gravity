% Resolucion sistema de ec diferenciales no lineales
clc
clear all
close all

syms x y z 
vars=[x,y,z];
mu=0.0122;

L=LagrangePtsCalculator(mu,vars);

%% Estabilidad puntos de Lagrange

in=input('Punto de Lagrange (1:5)\n');
x_in=L(in,1); y_in=L(in,2); z_in=L(in,3);

Matrix=double(subs(JacobianMatrix(mu,x,y,z),[x,y,z],[x_in,y_in,z_in]));
Lambda=eig(Matrix);

%% Integración de órbitas con ode45 (Dormann-Prince)

tspan=[0,100];
InitCond=[L(in,1),L(in,2),L(in,3), 10^-2,0 ,0]';
opt=odeset('RelTol',1e-13,'AbsTol',1e-20);

tic
[~,U_sol]=ode45(@(t,U) systemFunction(t,U,mu),tspan, InitCond,opt);
toc

figure
plot(U_sol(:,1),U_sol(:,2))
xlabel('Coord x')
ylabel('Coord y')
title('trayectoria Dopri')

%% Integración con Ode113 (Adams-Basforth)

tspan=[0,100];
InitCond=[L(in,1),L(in,2),L(in,3), 10^-2,0 ,0]';
opt=odeset('RelTol',1e-13,'AbsTol',1e-20);

tic
[t,U_sol]=ode113(@(t,U) systemFunction(t,U,mu),tspan, InitCond,opt);
toc 

figure
plot(U_sol(:,1),U_sol(:,2))
xlabel('Coord x')
ylabel('Coord y')
title('trayectoria ABM')

