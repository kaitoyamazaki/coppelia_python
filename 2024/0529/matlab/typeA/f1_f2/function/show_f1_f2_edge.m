% f1, f2エッジから成るベクトルを描画する関数
% 今回はそれぞれのベクトルに掛ける媒介変数を変化させる予定

function [p1, p2, p, box1, box2, box3, box4] = show_f1_f2_edge(i, l1, f1, l2, f2, l3, f3)

    A = [0 -1 0;
         1 0 1;
         l1(1) l2(2) l3(1)];

    edit_f1 = i * f1;
    edit_f2 = (1-i) / 2 * f2;
    edit_f3 = 0;

    all_f1 = [edit_f1; 0; 0];
    all_f2 = [0; edit_f2; 0];

    ans_f1 = A * all_f1;
    ans_f2 = A * all_f2;

    wrench1 = [ans_f1(1) ans_f1(2) ans_f1(3)];
    wrench2 = [ans_f2(1) ans_f2(2) ans_f2(3)];

    wrench = wrench1 + wrench2;

    p1 = plot3([0, wrench1(1)], [0, wrench1(2)], [0, wrench1(3)], 'Color', [1.0, 1.0, 0.0], 'LineWidth', 4.0);
    p2 = plot3([0, wrench2(1)], [0, wrench2(2)], [0, wrench2(3)], 'Color', [1.0, 0.65, 0.0], 'LineWidth', 4.0);
    p = plot3([0, wrench(1)], [0, wrench(2)], [0, wrench(3)], 'Color', [1.0, 0.33, 0.65], 'LineWidth', 4.0);
    box1 = annotation('textbox', [0.0, 0.9, 0.1, 0.1], 'String', sprintf('f1 = (%.1f, %.4f, %.4f)', wrench1(1), wrench1(2), wrench1(3)), 'FitBoxToText', 'on', 'Color', [0.8, 0.8, 0.0], 'EdgeColor', 'none', 'FontSize', 12);
    box2 = annotation('textbox', [0.0, 0.85, 0.1, 0.1], 'String', sprintf('f2 = (%.4f, %.1f, %.4f)', wrench2(1), wrench2(2), wrench2(3)), 'FitBoxToText', 'on', 'Color', [1.0, 0.65, 0.0], 'EdgeColor', 'none', 'FontSize', 12);
    box3 = annotation('textbox', [0.0, 0.8, 0.1, 0.1], 'String', sprintf('f3 = (%.1f, %.1f, %.1f)', 0, 0, 0), 'FitBoxToText', 'on', 'Color', [0.5, 0.0, 0.5], 'EdgeColor', 'none', 'FontSize', 12);
    box4 = annotation('textbox', [0.0, 0.75, 0.1, 0.1], 'String', sprintf('wrench = (%.4f, %.4f, %.4f)', wrench(1), wrench(2), wrench(3)), 'FitBoxToText', 'on', 'Color', [1.0, 0.33, 0.65], 'EdgeColor', 'none', 'FontSize', 12);

    if(i == 0.5)
        disp('f1の値 ');
        disp(wrench1);

        disp('f2の値 ');
        disp(wrench2);

        disp('wrenchの値 ');
        disp(wrench);
end