clear variables
close all
x = linspace(1, exp(1), 100);
y = zeros(1,100);
N = 40;

for k = 1:N
    y = y + (2/(k*pi))*(((-1)^k - 1)/(k^2 * pi^2 - 1))* sin(k*pi*log(x));
end

plot(x, y, '-r')
ylim([-0.145 0])
set(gca, 'XAxisLocation', 'top')
title('Solución al ejercicio de expansión en eigenvalores')
