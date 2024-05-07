x = [-20, -20, -5, -5, -20, -20, 20, 20, 5, 5, 20, 20];
y = [40, 30, 30, -30, -30, -40, -40, -30, -30, 30, 30, 40];

x_c1 = 7.5;
y_c1 = 27.5;

x_c2 = -7.5;
y_c2 = 15.0;

x_cop = (x_c1 + x_c2) / 2;
y_cop = (y_c1 + y_c2) / 2;

r = 2.5;
r2 = 1;
r3 = 1.5;

p1 = [x_c1, y_c1+r];
p2 = [x_c1-r, y_c1];
p3 = [x_c2, y_c2+r];

alpha = 10;
beta = -10;
gamma = 10;

theta = linspace(0, 2*pi, 100);
theta2 = linspace(0, 2*pi, 100);

x_cir1 = r * cos(theta) + x_c1;
y_cir1 = r * sin(theta) + y_c1;

x_cir2 = r * cos(theta2) + x_c2;
y_cir2 = r * sin(theta2) + y_c2;

x_cir11 = r2 * cos(theta) + x_c1;
y_cir11 = r2 * sin(theta) + y_c1;

x_cir21 = r2 * cos(theta2) + x_c2;
y_cir21 = r2 * sin(theta2) + y_c2;

cog_x = r3 * cos(theta);
cog_y = r3 * sin(theta);

Cop_x = r3 * cos(theta) + x_cop;
Cop_y = r3 * sin(theta) + y_cop;


% 図形のプロット
figure;

hold on;

grid on;

fill(x, y, [1, 0.66, 0.66]); % 赤色で図形を塗りつぶす
fill(x_cir1, y_cir1, [0.7, 1, 0.7]);
fill(x_cir2, y_cir2, [0.7, 1, 0.7]);
fill(x_cir11, y_cir11, [0.0, 0.0, 0.0]);
fill(x_cir21, y_cir21, [0.0, 0.0, 0.0]);
fill(cog_x, cog_y, [0.0, 0.0, 0.0]);
fill(Cop_x, Cop_y, [0.0, 0.0, 0.0]);

axis equal; % 各軸のスケールを等しく保持

xlim([-50, 50]); % X軸の範囲を設定
ylim([-50, 50]); % Y軸の範囲を設定
xlabel('X   [mm]');
ylabel('Y   [mm]');


load('data/typeB_coeffs.mat');

rows = size(coeff_num);

pause(5);

for i=1:rows(1);
    edit_alpha = alpha;
    edit_beta = beta;
    edit_gamma = gamma;

    edit_alpha = edit_alpha * coeff_num(i, 1);
    edit_beta = edit_beta * coeff_num(i, 2);
    edit_gamma = edit_gamma * coeff_num(i, 3);

    edit_cop_x = edit_alpha;
    edit_cop_y = edit_beta + edit_gamma;
    %coeffs = [edit_alpha, edit_beta, edit_gamma];
    %disp(coeffs);
    h1 = quiver(7.5, 30, 0.0, edit_alpha, 'Color', 'k', 'LineWidth', 2.0, 'AutoScale', 'off');
    h2 = quiver(5.0, 27.5, edit_beta, 0.0, 'Color', 'k', 'LineWidth', 2.0, 'AutoScale', 'off');
    h3 = quiver(-5.0, 15.0, edit_gamma, 0.0, 'Color', 'k', 'LineWidth', 2.0, 'AutoScale', 'off');
    h4 = quiver(x_cop, y_cop, edit_cop_x, edit_cop_y, 'Color', 'r', 'LineWidth', 3.0, 'AutoScale', 'off');
    h5 = quiver(0.0, 0.0, -edit_cop_x, -edit_cop_y, 'Color', 'r', 'LineWidth', 3.0, 'AutoScale', 'off');
    pause(0.30);
    delete(h1);
    delete(h2);
    delete(h3);
    delete(h4);
    delete(h5);
end

hold off;