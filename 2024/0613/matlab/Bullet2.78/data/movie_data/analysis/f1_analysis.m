% f1のデータを解析するプログラムを記述

% 初期化
clear;

% データがある箇所のフォルダを検索フォルダに追加
addpath('..');

% 力データの読み込み

force_r = readmatrix('../force_r_typeA.csv');

% 力データの編集
time = force_r(:, 1);
force_c1 = force_r(:, 3);
force_c1 = -1 .* force_c1;
force_pos = force_c1(force_c1 >= 0);
force_neg = force_c1(force_c1 < 0);
time_pos = time(force_c1 >= 0);
time_neg = time(force_c1 < 0);

% 値を導出

% 平均値
mean_value_f1 = mean(force_c1);

% 中央値
median_value_f1 = median(force_c1);

% 分散
variance_value_f1 = var(force_c1);

% 標準値
std_deviation_f1 = std(force_c1);

% 移動平均
window_size = 3;
moving_ave_f1 = movmean(force_c1, window_size);


% 
figure;
grid on;
hold on;

title('Magnitude of force at contact point1');
xlabel('time [s]');
ylabel('f [N]');

ylim([-1, 1]);

scatter(time_pos, force_pos, 'filled', 'b');
scatter(time_neg, force_neg, 'filled', 'r');

average_value_txt = sprintf('平均値: %f', mean_value_f1);
median_value_txt = sprintf('中央値: %f', median_value_f1);
standard_deviation_txt = sprintf('標準偏差: %f', std_deviation_f1);
disp(average_value_txt);
disp(median_value_txt);
disp(standard_deviation_txt);