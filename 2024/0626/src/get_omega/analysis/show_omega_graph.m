% シミュレーションで取得した角速度データをプロットする

clear;

addpath('.', '-end');
addpath('use_data', '-end');

filepath = 'use_data/omega_3000_283.mat';
data = load(filepath);
data = data.omega_row;

time = data(:, 1);
omega_hand = data(:, 2);
omega_cog = data(:, 3);

% 移動平均フィルタ
size = 5;
omega_hand = movmean(omega_hand, size);
omega_cog = movmean(omega_cog, size);

figure;

hold on;
grid on;

plot(time, omega_hand);

xlabel('time [s]');
ylabel('omega [rad/s]');
xlim([0, 70]);
ylim([-0.1, 0.1]);

title('ハンド中心の角速度')

hold off;

figure;

hold on;
grid on;

plot(time, omega_cog);

xlabel('time [s]');
ylabel('omega [rad/s]');
xlim([0, 70]);
ylim([-0.1, 0.1]);

title('物体重心の角速度')

hold off;