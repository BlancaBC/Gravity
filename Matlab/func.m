function F =func(y,mu)
    r=y(1:2);
    v=y(2:end);
    F=[v(1), v(2), -(mu)*r(1)/norm(r)^3, -(mu)*r(2)/norm(r)^3];
end