% typeBを実現するための円軌道を描くための座標導出プログラム

addpath('../../../', '-end')

first_pos = [-0.03361 0.17211];

num = 36;
point = zeros(0,2);
dtheta = 180 / num;
r = 0.1;

for i = 1:num
    theta = dtheta * i;
    x = r * cos(deg2rad(theta)) + first_pos(1);
    y = r * sin(deg2rad(theta)) + first_pos(2);
    p = [x, y];
    point = [point; p];
end