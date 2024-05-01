% wrenchベクトルを導出するための関数

function [x, y, z] = get_wrench_vec(point)
    x = [0, point(1)];
    y = [0, point(2)];
    z = [0, point(3)];
end