m1=1; %masas
m2=2*m1;

%trayectorias en el sistema CM
t=1:3600;
radio=10;

x1=radio.*cos(t*pi/180)*m2/(m1+m2);
y1=radio.*sin(t*pi/180)*m2/(m1+m2);
x2=-radio.*cos(t*pi/180)*m1/(m1+m2);
y2=-radio.*sin(t*pi/180)*m1/(m1+m2);
hold on
plot(x1,y1)
plot(x2,y2)
plot(0,0,'o','markersize',6,'markerfacecolor','r') %centro masas

%posición de los cuerpos
pos=150;
line([x1(pos),x2(pos)],[y1(pos),y2(pos)],'lineStyle','--', 'color','k')
plot(x1(pos),y1(pos),'o','markersize',4,'markerfacecolor','k')
plot(x2(pos),y2(pos),'o','markersize',4,'markerfacecolor','k')
hold off
axis equal
grid on
legend('m_1','m_2')
xlabel('x')
ylabel('y')
title('Trayectorias de dos cuerpos')
