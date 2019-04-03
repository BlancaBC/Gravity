function [F]=systemFunction(~,U)

% U(1)=x  U(2)=y   U(3)=z   U(4)=x'  U(5)=y'   U(6)=z'
mu=0.0122;
d=sqrt((U(1)+mu)^2+U(2)^2+U(3)^2);
r=sqrt((U(1)-1+mu)^2+U(2)^2+U(3)^2);


F=[ U(4);
    U(5);
    U(6);
    U(1)+2*U(5)-(1-mu)*(U(1)+mu)/d^3-mu*(U(1)-1+mu)/r^3;
    U(2)-2*U(4)-(1-mu)*U(2)/d^3-mu*U(2)/r^3;
    -(1-mu)*U(3)/d^3-mu*U(3)/r^3];

end