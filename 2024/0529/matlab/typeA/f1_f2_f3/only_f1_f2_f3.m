% 部分拘束typeAのwrench coneに関するプログラム
% 面倒であるため行列を使う予定
% 2つのエッジから成る平面に指定するベクトルを描画予定

% 初期化
clear;

% パスの追加
addpath('.', '-end');
addpath('../function', '-end');
addpath('../f1_f2/function', '-end');
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

wrench1 = [];
wrench2 = [];
wrench3 = [];
wrench = [];

for i = 0:0.01:0.5
    [p1, p2, p, b1, b2, b3, b4, w1, w2, w3, w] = show_f1_f2_edge(i, l1, f1, l2, f2, l3, f3);
    wrench1 = [wrench1; w1];
    wrench2 = [wrench2; w2];
    wrench3 = [wrench3; w3];
    wrench = [wrench; w];
    pause(0.1);

    delete(p1);
    delete(p2);
    delete(p);
    delete(b1);
    delete(b2);
    delete(b3);
    delete(b4);
end

for i = 0:0.01:0.25
    [p1, p2, p3, p, b1, b2, b3, b4, w1, w2, w3, w] = show_all_edge(i, l1, f1, l2, f2, l3, f3);
    wrench1 = [wrench1; w1];
    wrench2 = [wrench2; w2];
    wrench3 = [wrench3; w3];
    wrench = [wrench; w];
    pause(0.1);

    if(i == 0.25)
        disp('')
    
    else
        delete(p1);
        delete(p2);
        delete(p3);
        delete(p);
        delete(b1);
        delete(b2);
        delete(b3);
        delete(b4);
    end
end

hold off;