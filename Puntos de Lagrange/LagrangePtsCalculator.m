function [L]=LagrangePtsCalculator(mu,vars)
eqns=[vars(1)-(1-mu)*(vars(1)+mu)/((vars(1)+mu)^2+vars(2)^2+vars(3)^2)^(3/2)-mu*(vars(1)-1+mu)/((vars(1)-1+mu)^2+vars(2)^2+vars(3)^2)^(3/2)==0
     vars(2)-(1-mu)*vars(2)/((vars(1)+mu)^2+vars(2)^2+vars(3)^2)^(3/2)-mu*vars(2)/((vars(1)-1+mu)^2+vars(2)^2+vars(3)^2)^(3/2)==0
     -(1-mu)*vars(3)/((vars(1)+mu)^2+vars(2)^2+vars(3)^2)^(3/2)-mu*vars(3)/((vars(1)-1+mu)^2+vars(2)^2+vars(3)^2)^(3/2)==0];
 
 pts=solve(eqns,vars);
 
 L=LagrangePtsOrder(pts);
 
end