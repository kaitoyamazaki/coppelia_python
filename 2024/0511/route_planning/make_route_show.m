%　部分高速typeAの経路を表示する
%　データは以前作成したものを利用

clear;

addpath('.', '-end');
addpath('function', '-end');
addpath('data', '-end');

load('data/apply_points.mat', 'apply_points');


%apply_points = [];
first_pos = [0.069, 0.150];
goal_pos = [0.0, 0.350];

figure;

hold on;

grid on;

axis([-0.3 0.3 0.0 0.6]);

scatter(first_pos(1), first_pos(2), 100, 'filled', "g", 'MarkerEdgeColor', 'k', 'LineWidth', 2);
scatter(goal_pos(1), goal_pos(2), 100, 'filled', "r", 'MarkerEdgeColor', 'k', 'LineWidth', 2);

% x軸の描画
%line([0 0.2], [0 0], 'Color', 'red', 'LineWidth', 2); 
quiver(0.0, 0.0, 0.15, 0.0, 'Color', 'red', 'LineWidth', 3);
% y軸の描画
%line([0 0], [0 0.2], 'Color', 'green', 'LineWidth', 2); 
quiver(0.0, 0.0, 0.0, 0.15, 'Color', 'green', 'LineWidth', 3);


xlabel('X  [m]');
ylabel('Y  [m]');

title('Random Points in a Space.');

x = apply_points(:, 1);
y = apply_points(:, 2);

plot(x, y, 'LineWidth', 3, 'Color', 'g', 'Marker', 'o', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'k', 'MarkerSize', 3);
