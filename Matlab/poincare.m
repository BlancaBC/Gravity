clc, clear
%plotear seccion de poincare
ps=zeros(2,1);

[x,y]=ode45(@func,[0:0.001:100],[0.5 0.5 0.5]); %poner uno de nuestros integradores
plot(y(:,1),y(:,2)); %projeccion del espacio fase
hold

n=size(x);
np=1;%numero de puntos de poincare
for i=1:n(1)
  if(y(i,3)>=(2*pi)*np)
          ps(np,1)=y(i,1);
          ps(np,2)=y(i,2);
          np=np+1;
  end
end
for i=1:np-1
    plot(ps(i,1),ps(i,2),'r*')
end

%llamar a uno de nuestros osciladores
function dy=func(x,y)
a=1; b=3;
dy=zeros(3,1);
dy(1)=y(2);
dy(2)=-(a)*y(1);
dy(3)=b;
end