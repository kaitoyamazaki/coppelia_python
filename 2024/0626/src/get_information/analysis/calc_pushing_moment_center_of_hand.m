% シミュレータ内で取得したcsvファイル(時間, cop_x, cop_y, p_x, p_y)

clear;

addpath('.', '-end');
addpath('../moment_data', '-end');

filepath = '../moment_data/まっすぐ並進運動時のデータ_位置ベクトルと位置偏差_ハンド中心.csv';
data = readmatrix(filepath);

old_data = data(1, :);
dp_row = [];

for i = 1:size(data, 1)
    dp = data(i, :) - old_data;
    dp_row = [dp_row; dp];
    old_data = data(i, :);
end

velocity_and_pos_vector = [];

for i = 1:size(dp_row, 1)
    time = dp_row(i, 1);

    v = [dp_row(i, 2)/time dp_row(i, 3)/time data(i, 4) data(i, 5)];
    velocity_and_pos_vector = [velocity_and_pos_vector; v];
end

velocity_direction_and_pos_vector = [];

for i = 1:size(velocity_and_pos_vector, 1)
    theta = atan2(velocity_and_pos_vector(i, 2), velocity_and_pos_vector(i, 1));
    v_d = [theta velocity_and_pos_vector(i, 3) velocity_and_pos_vector(i, 4)];

    velocity_direction_and_pos_vector = [velocity_direction_and_pos_vector; v_d];
end


mu = 0.80;
m = 0.01484;
g = 9.81;

friction = mu * m * g;

object_moment = [];

for i = 1:size(velocity_direction_and_pos_vector, 1)
    friction_x = friction * cos(velocity_direction_and_pos_vector(i,1));
    friction_y = friction * sin(velocity_direction_and_pos_vector(i,1));
    friction_vector = [friction_x friction_y 0];
    pos_vector = [velocity_direction_and_pos_vector(i, 2) velocity_direction_and_pos_vector(i, 3) 0];
    moment = cross(pos_vector, friction_vector);
    want_data = [data(i, 1) moment(3)];
    object_moment = [object_moment; want_data];
end