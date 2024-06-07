% シミュレータで得たデータを素に, レンチ空間をスパンする

% 初期化
clear;

% 検索フォルダの読み込み
addpath('.', '-end');
addpath('function', '-end');
addpath('data', '-end');

% 力データの読み込み

force_r = readmatrix('data/force_r_typeA.csv');
force_l = readmatrix('data/force_l_typeA.csv');

force_c1 = force_r(:, 2);
force_c2 = force_r(:, 1);
force_c3 = force_l(:, 2);