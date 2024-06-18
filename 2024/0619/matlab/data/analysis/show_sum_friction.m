% friction_moment.mを実行後の利用を推奨
% friction_moment.mで計算した合摩擦力の合モーメントを描画するプログラム

% 変数の初期化
clear;

% 検索フォルダの追加
addpath('.', '-end');
addpath('res', '-end');

% .matファイルの読み込み
load_data = load('res/sum_friction_moment.mat');
Friction_moment = load_data.sum_friction_moment;

figure;

hold on;
grid on;

x = Friction_moment(:, 1);
y = Friction_moment(:, 2);

ylim([-0.00025, 0.00025]);
%ylim([-0.005, 0.005]);

plot(x, y);

hold off;