function [A]=JacobianMatrix(mu,x,y,z)

d=sqrt((x+mu)^2+y^2+z^2);
r=sqrt((x-1+mu)^2+y^2+z^2);

omega_xx=1-(1-mu)/d^3-mu/r^3+3*(1-mu)*(x+mu)^2/d^5+3*mu*(x-1+mu)^2/r^5;
omega_yy=1-(1-mu)/d^3-mu/r^3+3*(1-mu)*y^2/d^5+3*mu*y^2/r^5;
omega_zz=-(1-mu)/d^3-mu/r^3+3*(1-mu)*z^2/d^5+3*mu*(x-1+mu)^2/r^5;
omega_xy=3*(1-mu)*(x+mu)*y/d^5+3*mu*(x-1+mu)*y/r^5;
omega_yx=omega_xy;
omega_xz=3*(1-mu)*(x+mu)*z/d^5+3*mu*(x-1+mu)*z/r^5;
omega_zx=omega_xz;
omega_yz=3*(1-mu)*z*y/d^5+3*mu*z*y/r^5;
omega_zy=omega_yz;
A=vpa([0           0       0       1    0   0;
       0           0       0       0    1   0;
       0           0       0       0    0   1;
     omega_xx omega_xy omega_xz    0    2   0;
     omega_xy omega_yy omega_yz   -2    0   0;
     omega_xz omega_yz omega_zz    0    0   0]);
end