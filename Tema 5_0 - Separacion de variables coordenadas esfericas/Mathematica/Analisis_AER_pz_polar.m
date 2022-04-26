theta = 0:0.01:2*pi;
rho = 0.4886*cos(theta);
rho2 = (0.4886^2*cos(theta).^2);
polarplot(theta, rho,'r');hold on;
polarplot(theta, -rho,'r');
polarplot(theta, rho2,'b')
title('Gráfica de p_z y p_z^2')