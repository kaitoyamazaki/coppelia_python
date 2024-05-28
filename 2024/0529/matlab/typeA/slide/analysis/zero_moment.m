% 今週のスライド用

% 初期化
clear;

% 検索フォルダのパスを追加

addpath('.', '-end');
addpath('function', '-end');

% 法線ベクトルの位置ベクトルの定義
l1 = [0.0075; 0.03; 0.0];
l2 = [0.005; 0.0275; 0.0];
l3 = [-0.0125; 0.03; 0.0];

% データの整理

wrench_pos = calc_wrench_pos(l1, l2, l3);

%load('data/wrench_pos.mat');

%figure;

%hold on;

%grid on;

%% グラフタイトル
%title('normal force in Wrench Space');

%% グラフの視点
%view(55, 30);

%%ラベルの描画
%xlabel('fx  [N]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'r');
%ylabel('fy  [N]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'g');
%zlabel('ω  [Nm]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'b');

%%グラフの範囲を設定
%xlim([-1, 1]);
%ylim([-1, 1]);
%zlim([-0.03, 0.03]);

%% 軸線を描画
%line([min(xlim) max(xlim)], [0 0], [0 0], 'Color', 'red', 'LineWidth', 1.0);
%line([0 0], [min(ylim), max(ylim)], [0 0], 'Color', 'green', 'LineWidth', 1.0);
%line([0 0], [0 0], [min(zlim) max(zlim)], 'Color', 'blue', 'LineWidth', 1.0);

%wrench = wrench_pos;

%x = wrench(:, 1);
%y = wrench(:, 2);
%z = wrench(:, 3);

%%scatter(wrench(:,1), wrench(:,2), wrench(:, 3), 'Color', 'b');
%scatter3(x, y, z);
%hold off;