% wrenchベクトルをランダムにプロットする

clear;

load('data/random_point.mat');
openfig(['data/typeA_wrench2.fig']);
view(170, 20);

hold on;

rows = size(random_point, 1);
pause(5);

for i = 1:1:rows
    %h = quiver3(0, 0, 0, random_point(i, 1), random_point(i, 2), random_point(i, 3), 'LineWidth', 1.5);
    h = quiver3(0, 0, 0, random_point(i, 1), random_point(i, 2), random_point(i, 3), 'Color', 'k', 'LineWidth', 1.5);
    pause(0.20);
    delete(h);
end

hold off;