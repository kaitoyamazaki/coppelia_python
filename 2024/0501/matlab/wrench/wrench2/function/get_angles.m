% 角度を計算する関数

function [internal_points] = get_angles(coeff1, coeff2, coeff3);
    internal_points = [];

    x_range = linspace(-1, 1, 100);
    y_range = linspace(-1, 1, 100);
    z_range = linspace(-0.03, 0.03, 100);
    %z_range = 0;

    for x = x_range
        for y = y_range
            for z = z_range
                % 不等式が成り立つのか条件式でチェック
                if (coeff1(1)*x + coeff1(2)*y + coeff1(3)*z <= 0) && (coeff2(1)*x + coeff2(2)*y + coeff3(3)*z <= 0) && (coeff3(1)*x + coeff3(2)*y + coeff3(3)*z <=0)
                    point = [x, y, z];
                    internal_points = [internal_points; x, y, z];
            end
        end
    end
end