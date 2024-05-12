% 1回のみの経路を探す関数

function [final_apply_point, apply_points] = search_apply_point(first_pos, goal_pos, random_point, min_theta, max_theta, origin_point, goal_pos_theta)
    apply_points = [];
    weight = 0;
    rows = size(random_point, 1);

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

    apply_rows = size(apply_points, 1);
    now_distance = 100;
    now_row = 0;

    %disp('適用点の個数');
    %disp(apply_rows);

    for i = 1:apply_rows
        distance = norm(apply_points(i, :) - origin_point);
        disp(distance);
        if(distance < now_distance)
            now_distance = distance;
            now_row = i;
        end

    end

    final_apply_point = apply_points(now_row, :);

    scatter(apply_points(:,1), apply_points(:,2), 'filled', 'k');
end