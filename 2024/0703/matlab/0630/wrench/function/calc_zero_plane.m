% ゼロ点である平面を作成するための関数

function [x, y, z] = calc_zero_plane(data)
    row = size(data, 1);
    remainder = rem(row, 5);

    x = reshape(data(1:row-remainder, 1), [], 5);
    y = reshape(data(1:row-remainder, 2), [], 5);
    z = reshape(data(1:row-remainder, 3), [], 5);

end