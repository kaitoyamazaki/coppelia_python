% シミュレーションで取得した角速度データをプロットする

clear;

addpath('.', '-end');
addpath('use_data', '-end');

filepath = 'use_data/object_moment_3000_283.mat';
data = load(filepath);
data = data.object_moment;

time = data(:, 1);
moment_hand = data(:, 2);
moment_cog = data(:, 3);

% 移動平均フィルタ
size = 5;
moment_hand = movmean(moment_hand, size);
moment_cog = movmean(moment_cog, size);

figure;

hold on;
grid on;

plot(time, moment_hand);

xlabel('time [s]');
ylabel('\omega [Nm]');
xlim([0, 70]);
ylim([-0.001, 0.001]);

title('ハンド中心のモーメント')

hold off;

figure;

hold on;
grid on;

plot(time, moment_cog);

xlabel('time [s]');
ylabel('\omega [Nm]');
xlim([0, 70]);
ylim([-0.001, 0.001]);

title('物体重心のモーメント')

hold off;