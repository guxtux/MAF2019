fplot(@(x) sin(pi*log(x)),[1, exp(1)])
hold on
fplot(@(x) sin(2*pi*log(x)),[1, exp(1)],'--')
hold on
fplot(@(x) sin(3*pi*log(x)),[1, exp(1)], ':k')
hold on
fplot(@(x) sin(4*pi*log(x)),[1, exp(1)],'-.')
hold on
plot([1 exp(1)], [0 0], 'k')
ylim([-1.2 1.2])
title('Primeras eigenfunciones y(x)', 'FontName', 'times', 'FontSize', 14)
