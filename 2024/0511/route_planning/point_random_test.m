% 部分拘束typeAにおけるプランニングのテスト

clear;

apply_points = [];
first_pos = [0.069, 0.150];
goal_pos = [-0.009, 0.302];

points = 5000;

% xとyの乱数を生成 (-1, 1の範囲)

random_point = [0.6 * rand(points, 1) - 0.3, 0.6 * rand(points, 1)];


figure;

hold on;

grid on;

axis([-0.3 0.3 0.0 0.6]);
scatter(random_point(:, 1), random_point(:, 2), 'filled');
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

title('Random Points in a Space.')

hold off;