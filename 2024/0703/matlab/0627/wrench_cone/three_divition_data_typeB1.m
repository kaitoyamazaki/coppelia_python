% ３次元のプログラム　テスト用コード

clear;

f1 = 1;
f2 = 1;
f3 = 1;

l1 = [7.5, 30.0, 0.0];
l2 = [5.0, 27.5, 0.0];
l3 = [-5.0, 14.271, 0.0];

l1 = l1 / 1000;
l2 = l2 / 1000;
l3 = l3 / 1000;

A = [0 -1 1;
     1 0 0;
     l1(1) l2(2) -l3(2)];

wrench_point = [];

for i = 0:0.025:1.0
    for j = 0:0.025:1.0
        for k = 0:0.025:1.0
            edit_f1 = i*f1;
            edit_f2 = j*f2;
            edit_f3 = k*f3;

            all_f1 = [edit_f1; 0; 0];
            all_f2 = [0; edit_f2; 0];
            all_f3 = [0; 0; edit_f3];

            ans_f1 = A *  all_f1;
            ans_f2 = A * all_f2;
            ans_f3 = A * all_f3;

            wrench1 = [ans_f1(1) ans_f1(2) ans_f1(3)];
            wrench2 = [ans_f2(1) ans_f2(2) ans_f2(3)];
            wrench3 = [ans_f3(1) ans_f3(2) ans_f3(3)];
            wrench = wrench1 + wrench2 + wrench3;

            wrench_point = [wrench_point; wrench];
        end
    end
end

figure;

hold on;
grid on;

%グラフの範囲を設定
xlim([-1, 1]);
ylim([-1, 1]);
zlim([-0.03, 0.03]);

%ラベルの描画
xlabel('fx  [N]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'r');
ylabel('fy  [N]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'g');
zlabel('ω  [Nm]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'b');

plot3(wrench_point(:, 1), wrench_point(:, 2), wrench_point(:, 3), '.');

hold off;