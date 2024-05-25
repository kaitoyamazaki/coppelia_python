% 部分拘束typeAのwrench coneに関するプログラム
% 面倒であるため行列を使う予定
% 2つのエッジから成る平面に指定するベクトルを描画予定

% 初期化
clear;

% パスの追加
addpath('.', '-end');
addpath('function', '-end');
addpath('data', '-end');

% グラフデータの取得と出力
openfig('data/wrench_typeA.fig');

hold on;

% 法線ベクトルの定義(行列で行うため, ここでは単位ベクトルの絶対値を定義)
f1 = 1;
f2 = 1;
f3 = 1;

% 法線ベクトルの位置ベクトルの定義
l1 = [0.0075; 0.03; 0.0];
l2 = [0.005; 0.0275; 0.0];
l3 = [-0.0125; 0.03; 0.0];

for i = 0:0.01:0.5
    [p1, p2] = show_f1_f2(i, l1, f1, l2, f2, l3, f3);
    pause(0.1);
end

hold off;