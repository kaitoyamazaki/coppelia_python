% direction_friction.mで計算した結果より, 速度を計算する

clear;

addpath('.', '-end');
addpath('..', '-end');
addpath('../data', '-end');

filepath = '../data/cog_dp_se2.mat';
load(filepath, 'all_dp');

row = size(all_dp, 1);
velocity = [];

for i = 1:row
    vx = all_dp(i, 2) / all_dp(i, 1);
    vy = all_dp(i, 3) / all_dp(i, 1);
    omega = all_dp(i, 4) / all_dp(i, 1);

    v = [vx vy omega];

    velocity = [velocity; v];
end