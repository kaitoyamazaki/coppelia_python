% 適用されるポイントをプロットする

clear;

load('data/all_apply_points.mat');
openfig(['data/typeA_wrench.fig']);
view(170, 30);

hold on;

rows = size(points, 1);

for i = 1:rows
    plot3(points(i, 1), points(i, 2), points(i, 3), '-o');
end

hold off;