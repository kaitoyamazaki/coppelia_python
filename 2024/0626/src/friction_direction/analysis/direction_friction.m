% 取得したcogのデータから時間あたりの速度を計算する.

clear;

addpath('.', '-end');
addpath('../data');


filepath = '../data/cog_se2.csv';
cog_se2 = readmatrix(filepath);

row = size(cog_se2, 1);

old_data = cog_se2(1,:);
all_dp = [];

for i = 1:row
    dp = cog_se2(i, :) - old_data;

    old_data = cog_se2(i, :);

    all_dp = [all_dp; dp];
end

save_filepath = '../data/cog_dp_se2.mat';
save(save_filepath, 'all_dp');