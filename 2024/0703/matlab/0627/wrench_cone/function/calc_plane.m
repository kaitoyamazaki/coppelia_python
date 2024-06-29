% レンチの端点から点群データを計算する
% 点群データをmesh()関数が適用しやすいように変換して出力する

function [x, y, z] = calc_plane(point1, point2)

    number_rows = 100000;

    points = zeros(number_rows, 3);
    count = 1;

    plane_coefficient = cross(point1, point2);

    for lamda = 0.0:0.01:1.0
        for mu = 0.0:0.01:1.0
            if(lamda + mu <= 1.0)
                point = lamda*point1 + mu*point2;

                if abs(plane_coefficient(1)*point(1) + plane_coefficient(2)*point(2) + plane_coefficient(3)*point(3)) < 1e-10
                    points(count, :) = point;
                    count = count + 1;
                end
            end
        end
    end

    remainder = rem(count, 5);

    x = reshape(points(1:count-remainder, 1), [], 5);
    y = reshape(points(1:count-remainder, 2), [], 5);
    z = reshape(points(1:count-remainder, 3), [], 5);
end