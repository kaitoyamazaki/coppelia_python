% f1, f2から成るベクトルを描画する関数(プロトタイプ1)
% どちらも同じノルムで変化するようにする

function [p1, p2] = show_f1_f2(i, l1, f1, l2, f2, l3, f3)

    A = [0 -1 0;
         1 0 1;
         l1(1) l2(2) l3(1)];

    edit_f1 = i * f1;
    edit_f2 = i * f2;
    edit_f3 = 0;

    all_f1 = [edit_f1; 0; 0];
    all_f2 = [0; edit_f2; 0];

    ans_f1 = A * all_f1;
    ans_f2 = A * all_f2;

    
    %^m1 = cross(l1, edit_f1);
    %^m2 = cross(l2, edit_f2);

    wrench1 = [ans_f1(1) ans_f1(2) ans_f1(3)];
    wrench2 = [ans_f2(1) ans_f2(2) ans_f2(3)];

    wrench = wrench1 + wrench2;

    p1 = plot3([0, wrench1(1)], [0, wrench1(2)], [0, wrench1(3)], 'Color', [1.0, 1.0, 0.0], 'LineWidth', 4.0);
    p2 = plot3([0, wrench2(1)], [0, wrench2(2)], [0, wrench2(3)], 'Color', [1.0, 0.65, 0.0], 'LineWidth', 4.0);
    w_v = plot3([0, wrench(1)], [0, wrench(2)], [0, wrench(3)], 'Color', [1.0, 0.33, 0.65], 'LineWidth', 4.0);
end