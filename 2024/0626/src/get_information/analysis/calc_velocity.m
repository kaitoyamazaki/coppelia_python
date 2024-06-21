% ファイル名はとりあえず仮
% 時間と位置データより, 速度データを取得予定

clear;

addpath('.', '-end');
addpath('../data', '-end');


filepath = '../data/まっすぐ並進運動時のデータ_283.csv';
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
    v = [dp_row(i, 2)/time dp_row(i, 3)/time dp_row(i, 4)/time dp_row(i, 5)/time]

    velocity_row = [velocity_row; v];
end