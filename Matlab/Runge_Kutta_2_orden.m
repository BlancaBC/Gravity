function [Out] = Runge_Kutta_2_orden(paso_temp,F,U)
    U2 = U + paso_temp*0.5*F;
    Out = U + paso_temp*0.5*(F+ oscilador(U2));
end

