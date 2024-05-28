% 今週のスライド用のやつ

% 初期化
clear;

% 検索フォルダを追加
addpath('../function', '-end');
addpath('.', '-end');
addpath('../graph_data', '-end');

% 法線ベクトルの定義

f1 = 1;
f2 = 1;
f3 = 1;

% 法線ベクトルの位置ベクトルの定義
l1 = [0.0075; 0.03; 0.0];
l2 = [0.005; 0.0275; 0.0];
l3 = [-0.0125; 0.03; 0.0];


% グラフ描画開始

figure;

hold on;

grid on;

% グラフタイトル
title('normal force in Wrench Space');

% グラフの視点
view(55, 30);

%ラベルの描画
xlabel('fx  [N]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'r');
ylabel('fy  [N]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'g');
zlabel('ω  [Nm]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'b');

%グラフの範囲を設定
xlim([-1, 1]);
ylim([-1, 1]);
zlim([-0.03, 0.03]);

% 軸線を描画
line([min(xlim) max(xlim)], [0 0], [0 0], 'Color', 'red', 'LineWidth', 1.0);
line([0 0], [min(ylim), max(ylim)], [0 0], 'Color', 'green', 'LineWidth', 1.0);
line([0 0], [0 0], [min(zlim) max(zlim)], 'Color', 'blue', 'LineWidth', 1.0);

pause(10);

for i = 0:0.1:1
    for j = 0:0.02:1

        s = i;
        t = j;
        u = 1 - s - t;

        if(0 <= s && s <= 1 && 0 <= t & t <= 1 && 0 <= u && u <= 1)

            A = [0 -1 0;
                1 0 1;
                l1(1) l2(2) l3(1)];

            edit_f1 = s * f1;
            edit_f2 = t * f2;
            edit_f3 = u * f3;

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

            p1 = plot3([0, wrench1(1)], [0, wrench1(2)], [0, wrench1(3)], 'Color', [0.8, 0.8, 0.0], 'LineWidth', 4.0);
            p2 = plot3([0, wrench2(1)], [0, wrench2(2)], [0, wrench2(3)], 'Color', [1.0, 0.65, 0.0], 'LineWidth', 4.0);
            p3 = plot3([0, wrench3(1)], [0, wrench3(2)], [0, wrench3(3)], 'Color', [0.5, 0.0, 0.5], 'LineWidth', 4.0);
            p = plot3([0, wrench(1)], [0, wrench(2)], [0, wrench(3)], 'Color', [1.0, 0.33, 0.65], 'LineWidth', 4.0);
            box1 = annotation('textbox', [0.0, 0.9, 0.1, 0.1], 'String', sprintf('ベクトル 係数 : s = (%.2f)', s), 'FitBoxToText', 'on', 'Color', [0.0, 0.0, 0.0], 'EdgeColor', 'none', 'FontSize', 12);
            box2 = annotation('textbox', [0.0, 0.85, 0.1, 0.1], 'String', sprintf('ベクトル 係数 : t = (%.2f)', t), 'FitBoxToText', 'on', 'Color', [0.0, 0.0, 0.0], 'EdgeColor', 'none', 'FontSize', 12);
            box3 = annotation('textbox', [0.0, 0.80, 0.1, 0.1], 'String', sprintf('ベクトル 係数 : u = (%.2f)', u), 'FitBoxToText', 'on', 'Color', [0.0, 0.0, 0.0], 'EdgeColor', 'none', 'FontSize', 12);


            pause(0.025);

            if(i == 1 && j == 0);
                disp('');
            else
                delete(box1);
                delete(p1);
                delete(p2);
                delete(p3);
                delete(p);
                delete(box2);
                delete(box3);
            end

            disp('i :');
            disp(i);

            disp('j : ');
            disp(j);
        end
    end

end

hold off;