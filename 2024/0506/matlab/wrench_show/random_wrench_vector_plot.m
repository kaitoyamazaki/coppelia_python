% wrenchベクトルをランダムにプロットする

clear;

load('data/random_points_typeB.mat');
openfig(['data/typeB_wrench.fig']);

hold on;

rows = size(random_points_typeB, 1);
pause(5);

for i = 1:1:rows
    %h = quiver3(0, 0, 0, random_points_typeBs_in_wrench_typeB(i, 1), random_points_typeB(i, 2), random_points_typeB(i, 3), 'LineWidth', 1.5);
    h = quiver3(0, 0, 0, random_points_typeB(i, 1), random_points_typeB(i, 2), random_points_typeB(i, 3), 'Color', 'k', 'LineWidth', 1.5);
    pause(0.20);
    delete(h);
end

hold off;