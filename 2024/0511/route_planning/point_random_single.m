%　部分高速typeAの経路を表示する
%　データは以前作成したものを利用

clear;

addpath('.', '-end');
addpath('function', '-end');

load('data/random_point.mat', 'random_point');

apply_points = [];
first_pos = [0.069, 0.150];
goal_pos = [0.0, 0.35];


min_theta = 90;
max_theta = 114.4;
half_range = max_theta - min_theta;
average_theta = (min_theta + max_theta) / 2;

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

% ここはプログラム実行のための準備
origin_point = first_pos;
row_number = 0;
apply_points = [apply_points; first_pos];
diff_x_goal = goal_pos(1) - first_pos(1);
diff_y_goal = goal_pos(2) - first_pos(2);
goal_pos_theta = atan2(diff_y_goal, diff_x_goal);
goal_pos_theta = rad2deg(goal_pos_theta);

% ここから実施
% 手始めに一つずつ実施する
[return_point, all_points] = search_apply_point(first_pos, goal_pos, random_point, min_theta, max_theta, origin_point, goal_pos_theta);
apply_points = [apply_points; return_point];
origin_point = apply_points(end, :);
scatter(origin_point(1), origin_point(2), 100, 'filled', "k", 'MarkerEdgeColor', 'k', 'LineWidth', 2);