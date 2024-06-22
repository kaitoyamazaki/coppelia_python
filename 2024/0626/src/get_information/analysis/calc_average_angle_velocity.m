% 摩擦力モーメントより計算した角速度を利用して, 平均の速度を求める

clear;

addpath('.', '-end');
addpath('use_data');

filepath = 'use_data/object_vel_data_理想値.mat';
data = load(filepath);
data = data.ang_vel_data;

data = data(1:476, :);

data2 = data(:, 2);
data2(isnan(data2)) = 0;

ave = mean(data2);
med = median(data2);
disp(ave);
disp(med);

time = data(end, 1);

theta = ave * time;