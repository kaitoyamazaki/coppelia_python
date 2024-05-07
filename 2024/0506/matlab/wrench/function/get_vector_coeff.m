% 線形結合するための係数を導出するプログラム

function [alpha, beta, gamma, Flg] = get_vector_coeff(m1, m2, m3, point)
    syms a b c

    eq1 = a*m1(1) + b*m2(1) + c*m3(1) == point(1);
    eq2 = a*m1(2) + b*m2(2) + c*m3(2) == point(2);
    eq3 = a*m1(3) + b*m2(3) + c*m3(3) == point(3);

    assume(0 <= a & a <= 1);
    assume(0 <= b & b <= 1);
    assume(0 <= c & c <= 1);

    %disp(['eq1: ', char(eq1)]);
    %disp(['eq2: ', char(eq2)]);
    %disp(['eq3: ', char(eq3)]);

    solutions = solve([eq1, eq2, eq3], [a, b, c], 'ReturnConditions', true);
    if isempty(solutions.a) || isempty(solutions.b) || isempty(solutions.c)
        disp('解が存在しません。');
        alpha = 0;
        beta = 0;
        gamma = 0;
        Flg = 1;
    else
        %disp(solutions.a);
        %disp(solutions.b);
        %disp(solutions.c);
        alpha = solutions.a;
        beta = solutions.b;
        gamma = solutions.c;
        Flg = 0;
    end
end