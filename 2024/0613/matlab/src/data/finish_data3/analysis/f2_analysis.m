% f1のデータを解析するプログラムを記述

% 初期化
clear;

% データがある箇所のフォルダを検索フォルダに追加
addpath('..');

% 力データの読み込み

force_r = readmatrix('../force_r_typeA.csv');

% 力データの編集
time = force_r(:, 1);
force_c2 = force_r(:, 2);
%force_c1 = -1 .* force_c1;

force_pos = force_c2(force_c2 >= 0);
force_neg = force_c2(force_c2 < 0);

time_pos = time(force_c2 >= 0);
time_neg = time(force_c2 < 0);

figure;
grid on;
hold on;

title('Magnitude of force at contact point2');
xlabel('time [s]');
ylabel('f [N]');

ylim([-1, 1]);

scatter(time_pos, force_pos, 'filled', 'b');
scatter(time_neg, force_neg, 'filled', 'r');