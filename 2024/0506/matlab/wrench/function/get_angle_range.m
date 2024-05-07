% 与えられたwrench空間での最大の角度と最小の角度を導出するプログラム

function [Max, Min] = get_angle_range(p1, p2, p3)
    coeff1 = cross(p1, p2);
    coeff2 = cross(p2, p3);
    coeff3 = cross(p3, p1);

    internal_points = [];

    x_range = linspace(-1, 1, 100);
    y_range = linspace(-1, 1, 100);
    z_range = linspace(-0.0, 0.0, 100);
    %z_range = 0;

    for x = x_range
        for y = y_range
            for z = z_range

                % 不等式が成立するか条件式でチェック
                if (coeff1(1)*x+ coeff1(2)*y + coeff1(3)*z >= 0) && (coeff2(1)*x + coeff2(2)*y + coeff2(3)*z >= 0) && (coeff3(1)*x + coeff3(2)*y + coeff3(3)*z >= 0)
                    point = [x, y, z];
                    internal_points = [internal_points; point];
                end
            end
        end
    end

    angles = [];
    [rows, cols] = size(internal_points);

    for i = 1:rows
        angle = atan2(internal_points(i, 2), internal_points(i, 1));
        angle = rad2deg(angle);
        angles = [angles; angle];
    end

    Max = max(angles(:));
    Min = min(angles(:));
end