[X, Y, Z] =sphere;
r = 0.282;
r2 = 2*r;
X = X * r;
Y = Y * r;
Z = Z * r;
surf(X,Y,Z);hold on;
surf(X,Y,Z-r2)
title('Gráfica de p_z en coordenadas esféricas')
axis equal