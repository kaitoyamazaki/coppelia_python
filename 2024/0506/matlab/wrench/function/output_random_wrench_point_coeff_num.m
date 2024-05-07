% typeBにおいて適用可能である点の中でランダムに値を選択し, そのときの係数を導出する

function [random_points, coeff_nums] = output_random_wrench_point_coeff_num(m1, m2, m3, points)
    random_points = [];
    coeff_nums = [];

    rows = size(points, 1);

    for i = 1:1:100
        num = randi([1, rows]);
        point = points(num, :);
        [alpha, beta, gamma, Flg] = get_vector_coeff(m1, m2, m3, point);

        if(Flg == 0)
            random_points = [random_points; point];
            coeff_nums = [coeff_nums; alpha, beta, gamma];
        end
    end
end