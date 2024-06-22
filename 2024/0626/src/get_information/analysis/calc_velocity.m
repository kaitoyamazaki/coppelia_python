% ファイル名はとりあえず仮
% 時間と位置データより, 速度データを取得予定

clear;

addpath('.', '-end');
addpath('../data', '-end');


%filepath = '../data/斜めに並進運動時のデータ2_283.csv';
filepath = '../data/斜めに並進運動時のデータ_target追加_283.csv';

data = readmatrix(filepath);

old_data = data(1, :);
dp_row = [];

velocity_row = [];

for i = 1:size(data, 1)
    dp = data(i, :) - old_data;
    dp_row = [dp_row; dp];
    old_data = data(i, :);
end

for i = 1:size(dp_row, 1)
    time = dp_row(i, 1);
    v = [dp_row(i, 2)/time dp_row(i, 3)/time dp_row(i, 4)/time dp_row(i, 5)/time];

    velocity_row = [velocity_row; v];
end

velocity_direction = [];

for i = 1:size(velocity_row, 1)
    theta_a = atan2d(velocity_row(i, 2), velocity_row(i, 1));
    theta_b = atan2d(velocity_row(i, 4), velocity_row(i, 3));
    v_d = [theta_a theta_b];

    velocity_direction = [velocity_direction; v_d];
end