% 部分拘束typeAにおけるプランニングのテスト

clear;

apply_points = [];
first_pos = [0.069, 0.150];
goal_pos = [-0.009, 0.302];

points = 1000;
points = points - 1;

min_theta = 90;
max_theta = 105.5;
half_range = max_theta - min_theta;
average_theta = (min_theta + max_theta) / 2;

% xとyの乱数を生成 (-1, 1の範囲)

load('random_point.mat');

% 経路計画試作(自分が考えたもの, 今後他のアルゴリズムを確認しなければならない)
%apply_points = [apply_points; first_pos];

flg = 1;
origin_point = first_pos;
row_number = 0;

while true
    if (flg == 1)
        disp('start program')
        flg = 0;
    else
        origin_point = apply_points(end, :);
    end


    point = [];
    weight = 0;
    rows= size(random_point, 1);
    for i = 1:rows
        diff_x = random_point(i, 1) - origin_point(1);
        diff_y = random_point(i, 2) - origin_point(2);
        now_rad = atan2(diff_y, diff_x);
        diff_theta = rad2deg(now_rad) - average_theta;
        disp(diff_theta);
        conditional_expression = abs(rad2deg(now_rad) - average_theta) / half_range;
        if (0 <= conditional_expression && conditional_expression <= 1)
            now_weight = 1 - conditional_expression;
            if(now_weight > weight)
                weight = now_weight;
                point = [diff_x, diff_y];
                row_number = i;
            end
        end

        if(i == rows)
            apply_points = [apply_points; point];
            random_point(row_number, :) = [];

            %disp(rad2deg(now_rad));
            %disp('状態');
            %disp(conditional_expression);
        end
    end

    if(size(apply_points, 1) > 0)
        if(apply_points(end, :) == goal_pos)
            break;
        end
    end
end



% 結果をプロット

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