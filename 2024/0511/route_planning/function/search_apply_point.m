% 1回のみの経路を探す関数

function [final_apply_point, apply_points] = search_apply_point(first_pos, goal_pos, random_point, min_theta, max_theta, origin_point, goal_theta)
    apply_points = [];
    weight = 0;
    rows = size(random_point, 1);
    average_theta = (max_theta + min_theta) / 2;

    if (goal_theta < average_theta)
        max_theta = average_theta;
    else
        min_theta = goal_theta;
    end

    % 全範囲での適用点を探す処理
    for i = 1:rows
        point = [];
        diff_x = random_point(i, 1) - origin_point(1);
        diff_y = random_point(i, 2) - origin_point(2);
        now_rad = atan2(diff_y, diff_x);
        diff_theta = rad2deg(now_rad);
        if (min_theta <= diff_theta) && (diff_theta <= max_theta)
            %disp('現在の角度');
            %disp(diff_theta);
            point = random_point(i, :);
            apply_points = [apply_points; point];
        end
    end

    % 全範囲から一部分の範囲に変更して適用点を探す処理

    apply_rows = size(apply_points, 1);
    now_distance = 100;
    now_row = 0;

    %disp('適用点の個数');
    %disp(apply_rows);

    for i = 1:apply_rows
        distance = norm(apply_points(i, :) - origin_point);
        %disp(distance);
        if(distance < now_distance)
            now_distance = distance;
            now_row = i;
        end
    end


    final_apply_point = apply_points(now_row, :);

    diff_goal_x = goal_pos(1) - final_apply_point(1);
    diff_goal_y = goal_pos(2) - final_apply_point(2);
    diff_goal = [diff_goal_x, diff_goal_y];
    disp(diff_goal);
    if (diff_goal_x < 0) && (diff_goal_y > 0)
        diff_goal = [diff_goal_x, diff_goal_y];
    else
        final_apply_point = goal_pos;
        flg = 10;
    end
        

    scatter(apply_points(:,1), apply_points(:,2), 'filled', 'k');
end