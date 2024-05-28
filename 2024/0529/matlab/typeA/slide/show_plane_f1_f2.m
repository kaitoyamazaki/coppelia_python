% 今週のスライド用のやつ

% 初期化
clear;

% 検索フォルダを追加
addpath('function', '-end');
addpath('.', '-end');
addpath('graph_data', '-end');

% 法線ベクトルの定義

f1 = 1;
f2 = 0;
f3 = 1;

% 法線ベクトルの位置ベクトルの定義
l1 = [0.0075; 0.03; 0.0];
l2 = [0.005; 0.0275; 0.0];
l3 = [-0.0125; 0.03; 0.0];


% グラフ描画開始

openfig('graph_data/edge_f1_f2.fig');

hold on;

%pause(10);

wrench_pos = [];

for i = 0:0.01:1

    for j = 0:0.01:1

        A = [0 -1 0;
            1 0 1;
            l1(1) l2(2) l3(1)];

        edit_f1 = i * f1;
        edit_f2 = 0;
        edit_f3 = j * f3;

        all_f1 = [edit_f1; 0; 0];
        all_f2 = [0; edit_f2; 0];
        all_f3 = [0; 0; edit_f3];

        ans_f1 = A * all_f1;
        ans_f2 = A * all_f2;
        ans_f3 = A * all_f3;

        wrench1 = [ans_f1(1) ans_f1(2) ans_f1(3)];
        wrench2 = [ans_f2(1) ans_f2(2) ans_f2(3)];
        wrench3 = [ans_f3(1) ans_f3(2) ans_f3(3)];

        wrench = wrench1 + wrench2 + wrench3;
        wrench_pos = [wrench_pos; wrench];

    end
end

remainder = rem(size(wrench_pos, 1), 5);

wrench_x = reshape(wrench_pos(1:size(wrench_pos, 1) - remainder, 1), [], 5);
wrench_y = reshape(wrench_pos(1:size(wrench_pos, 1) - remainder, 2), [], 5);
wrench_z = reshape(wrench_pos(1:size(wrench_pos, 1) - remainder, 3), [], 5);

mesh1 = mesh(wrench_x, wrench_y, wrench_z, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);

hold off;