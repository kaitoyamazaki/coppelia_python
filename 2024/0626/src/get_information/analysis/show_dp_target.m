% 取得した偏差データを可視化するプログラム

clear;

addpath('.', '-end');
addpath('use_data', '-end');


filepath = 'use_data/dp_data_target_並進運動時_283.mat';

data = load(filepath);
data = data.dp_row;

figure;
hold on;
grid on;
title('ハンド中心の時間あたりの偏差')

xlim([-0.00025, 0.00025]);
ylim([-0.00025, 0.00025]);
xlabel('x [m]');
ylabel('y [m]');

pause(5);

for i = 1:size(data, 1)
    h1 = quiver(0.0, 0.0, data(i, 2), data(i, 3), 'Color', 'k', 'LineWidth', 2.0, 'AutoScale', 'off');
    pause(0.05);
    delete(h1);
end

hold off;