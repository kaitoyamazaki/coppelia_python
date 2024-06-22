% 取得したデータからハンド中心の時間辺りの速度を可視化する

clear;

addpath('.', '-end');
addpath('use_data', '-end');

filepath = 'use_data/velocity_data_target_並進運動時_283.mat';

data = load(filepath);
data = data.velocity_row;

figure;
hold on;
grid on;
title('追従のベースと成る点の時間当たりの速度')

xlim([-0.005, 0.005]);
ylim([-0.005, 0.005]);
xlabel('x [m / s]');
ylabel('y [m / s]');

pause(5);

for i = 1:size(data, 1)
    h1 = quiver(0.0, 0.0, data(i, 1), data(i, 2), 'Color', 'k', 'LineWidth', 2.0, 'AutoScale', 'off');
    pause(0.05);
    delete(h1);
end

hold off;