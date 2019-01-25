function [Out] = Runge_Kutta_2_orden(paso_temp,F,U)
    G = 1.0;
m1=1.0;
m2=0.001;
mu=G*(m1+m2);
    U2 = U + paso_temp*0.5*F;
    Out = U + paso_temp*0.5*(F+ oscilador(U2));
end

