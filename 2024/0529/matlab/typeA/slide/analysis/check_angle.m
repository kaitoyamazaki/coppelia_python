% 角度をチェックするプログラム

clear;

addpath('.', '-end');
addpath('data', '-end');

% データの読み込み
load('data/wrench_pos_new.mat');

angle_rad = [];
angle_deg = [];

for i = 1:size(wrench_pos,1)
    angle = atan2(wrench_pos(i, 2), wrench_pos(i, 1));
    deg = rad2deg(angle);

    angle_rad = [angle_rad; angle];
    angle_deg = [angle_deg; deg];
end

angle_rad = sort(angle_rad);
angle_deg = sort(angle_deg);