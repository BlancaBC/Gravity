function [Out] = Runge_Kutta_2_orden(paso_temp,F,U)
    U2 = U + paso_temp*0.5*F(U);
    Out = U + paso_temp*0.5*(F(U)+ F(U2));
end

