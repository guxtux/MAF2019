t = linspace(0,2*pi,100);
lt = zeros(length(t),1);
y = 0.4886*cos(t)
plot(t, y);
hline = refline(0, 0);
hline.Color = 'k';
xlim([0,2*pi]);
title('Gráfica de p_z contra \theta') 
%xticks([0 pi 2*pi]);
%xticklabels({'0','\pi','2\pi'});
%xticks([0 pi 2*pi])
%xticklabels({'0','\pi','2\pi'})
set(gca,'xtick',[0:pi/2:2*pi]) 
set(gca,'xticklabels',{'0','\pi/2', '\pi','3/2\pi','2\pi'})
