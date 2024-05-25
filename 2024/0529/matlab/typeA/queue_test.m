% 部分拘束typeAで定義したベクトルの式で変化があるかチェックする

clear;
addpath('.', '-end');
addpath('function', '-end');

% 法線ベクトルの定義
f1 = 1;
f2 = 1;
f3 = 1;


% 法線ベクトルの位置ベクトルの定義
l1 = [0.0075; 0.003; 0.0];
l2 = [0.005; 0.00275; 0.0];
l3 = [-0.005; 0.003; 0.0];

for i=0:0.01:1

    A = [0 1 0;
         1 0 1;
         l1(1) l2(2) l3(1)];
    
    edit_f1 = i * f1;
    %m1 = l1(1) * edit_f1;
    edit_f2 = 0;
    edit_f3 = 0;

    f = [edit_f1; edit_f2; edit_f3];

    ans = A * f;

    disp(ans);
    %disp(edit_f1);
    %disp(m1);
end