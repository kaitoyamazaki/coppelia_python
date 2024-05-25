% 法線ベクトルの値によってレンチベクトルが変化するものを作成

function [p, text_box] = show_quiver_f3(i, f, l)
    % 関数を動かすために返り値を記述
    h = 0;

    % 力とモーメントを計算
    edit_f = i * f;
    m = cross(l, edit_f);
    wrench = [edit_f(1) edit_f(2) m(3)];

    %disp('fxの大きさ ');
    %disp(edit_f(1));

    %disp('fyの大きさ ');
    %disp(edit_f(2));

    %disp('ωの大きさ');
    %disp(m(3));

    test = 0.001;
    %h = quiver3(0.0, 0.0, 0.0, wrench(1), wrench(2), wrench(3), 1, 'Color', 'r', 'LineWidth', 4.0, 'AutoScale', 'off', 'MaxHeadSize', 1.0);
    p = plot3([0, wrench(1)], [0, wrench(2)], [0, wrench(3)], 'Color', [0.8824, 0.3922, 0.4353], 'LineWidth', 4.0);
    text_box = annotation('textbox', [0.0, 0.9, 0.1, 0.1], 'String', sprintf('f3 = (%.4f, %.4f, %.4f)', wrench(1), wrench(2), wrench(3)), 'FitBoxToText', 'on', 'Color', 'k', 'EdgeColor', 'none', 'FontSize', 12);
end