% f1のデータを解析するプログラムを記述

% 初期化
clear;

% データがある箇所のフォルダを検索フォルダに追加
addpath('..');

% 力データの読み込み

force_l = readmatrix('../force_l_typeA.csv');

% 力データの編集
time = force_l(:, 1);
force_c3 = force_l(:, 3);
force_c3 = -1 .* force_c3;

force_pos = force_c3(force_c3 >= 0);
force_neg = force_c3(force_c3 < 0);

time_pos = time(force_c3 >= 0);
time_neg = time(force_c3 < 0);

figure;
grid on;
hold on;

title('Magnitude of force at contact point1');
xlabel('time [s]');
ylabel('f [N]');

scatter(time_pos, force_pos, 'filled', 'b');
scatter(time_neg, force_neg, 'filled', 'r');