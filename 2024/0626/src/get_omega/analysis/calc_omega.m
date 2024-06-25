% 偏差データから角速度, 角加速度などを計算するプログラム

clear;

addpath('.', '-end');
addpath('../data');

filepath = '../data/斜めに並進運動時のデータ_0_283.csv';
%filepath = '../data/斜めに並進運動時のデータ_1680_283.csv';
%filepath = '../data/斜めに並進運動時のデータ_2680_283.csv';
%filepath = '../data/斜めに並進運動時のデータ_3000_283.csv';
%filepath = '../data/斜めに並進運動時のデータ_5080_283.csv';

data = readmatrix(filepath);
old_data = data(1, :);
dp_row = [];

for i = 1:size(data, 1)
    dp = data(i, :) - old_data;
    dp_row = [dp_row; dp];
    old_data = data(i, :);
end

omega_row = [];

for i = 1:size(dp_row, 1)
    time = dp_row(i, 1);
    omega = [data(i,1) dp_row(i,2)/time dp_row(i,3)/time];
    omega_row = [omega_row; omega];
end

omega_acc_row = [];

for i = 1:size(omega_row, 1)
    time = dp_row(i, 1);
    omega_acc = [data(i, 1) omega_row(i,2)/time omega_row(i,3)/time];
    omega_acc_row = [omega_acc_row; omega_acc];
end

object_moment = [];
inertia = 0.00091;

for i = 1:size(omega_acc_row,1)
    time = data(i, 1);
    torque = [time omega_acc_row(i,2)*inertia omega_acc_row(i,3)*inertia];
    object_moment = [object_moment; torque];
end

%filepath_omega = 'use_data/omega_0_283.mat';
%filepath_omega = 'use_data/omega_1680_283.mat';
%filepath_omega = 'use_data/omega_2680_283.mat';
%filepath_omega = 'use_data/omega_3000_283.mat';
%filepath_omega = 'use_data/omega_5080_283.mat';

%filepath_moment = 'use_data/object_moment_0_283.mat';
%filepath_moment = 'use_data/object_moment_1680_283.mat';
%filepath_moment = 'use_data/object_moment_2680_283.mat';
%filepath_moment = 'use_data/object_moment_3000_283.mat';
%filepath_moment = 'use_data/object_moment_5080_283.mat';

%save(filepath_omega, 'omega_row');
%save(filepath_moment, 'object_moment');