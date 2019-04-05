function [L]=LagrangePtsCalculator(mu,vars)
x=vars(1); y=vars(2); z=vars(3);

eqns=[x-(1-mu)*(x+mu)/((x+mu)^2+y^2+z^2)^(3/2)-mu*(x-1+mu)/((x-1+mu)^2+y^2+z^2)^(3/2) == 0
    
     y-(1-mu)*y/((x+mu)^2+y^2+z^2)^(3/2)-mu*y/((x-1+mu)^2+y^2+z^2)^(3/2) == 0
     
     -(1-mu)*z/((x+mu)^2+y^2+z^2)^(3/2)-mu*z/((x-1+mu)^2+y^2+z^2)^(3/2) == 0];
 
 pts=solve(eqns,vars);
 
 L=LagrangePtsOrder(pts);
 
end