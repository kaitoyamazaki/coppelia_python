% 部分拘束typeAのwrench coneに関するプログラム
% f3, f1のみから成る平面上を動くベクトルを描画

% 初期化
clear;

% パスの追加
addpath('.', '-end');
addpath('../function', '-end');
addpath('function', '-end');
addpath('../data', '-end');

% グラフデータの取得と出力
openfig('../data/wrench_typeA3.fig');

hold on;

% 法線ベクトルの定義(行列で行うため, ここでは単位ベクトルの絶対値を定義)
f1 = 1;
f2 = 1;
f3 = 1;

% 法線ベクトルの位置ベクトルの定義
l1 = [0.0075; 0.03; 0.0];
l2 = [0.005; 0.0275; 0.0];
l3 = [-0.0125; 0.03; 0.0];

pause(10);

for i = 0:0.01:1.0

    for j = 0:0.01:1.0

        if (1 - i - j > 0 && 1 - i - j < 1)
            [p1, p2, p3, p, b1, b2, b3, b4] = show_all_edge(i, j, l1, f1, l2, f2, l3, f3);
            pause(0.1);

            if(i == 0.99 && j == 0.01)
                disp('');
            else
                delete(p1);
                delete(p2);
                delete(p3);
                delete(p);
                delete(b1);
                delete(b2);
                delete(b3);
                delete(b4);

                disp('iの値 : ');
                disp(i);

                disp('jの値 : ');
                disp(j);
            end
        else
            disp('');
        end
    end
end

hold off;