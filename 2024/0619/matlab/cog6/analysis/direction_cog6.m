% シミュレーションから取得したデータからcog6がどのように方向が変化しているか出力する

% 初期化
clear;

% 検索フォルダの読み込み
addpath('.', '-end');
addpath('..', '-end');
addpath('res', '-end');

% ファイルの読み込み
filepath = '../cog6_pos2.csv';
cog6_direction = readmatrix(filepath);

row = size(cog6_direction, 1);

figure;
hold on;
grid on;

xlim([-0.005, 0.005]);
ylim([-0.005, 0.005]);

for i = 1:row
    if(i > 1 && cog6_direction(i-1) == cog6_direction(i))
        continue
    end

    vector_x = cog6_direction(i, 2);
    vector_y = cog6_direction(i, 3);
    vector = [vector_x vector_y];

    h1 = quiver(0.0, 0.0, vector(1), vector(2), 'Color', 'k', 'LineWidth', 2.0, 'AutoScale', 'off');
    pause(0.01);
    %pause(0.0025);
    delete(h1);
end

hold off;