function [U] = Euler(paso_temp,F,U)
    U = U + paso_temp*F(U);
    return 
end