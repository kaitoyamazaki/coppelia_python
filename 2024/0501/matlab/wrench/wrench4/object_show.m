x = [-20, -20, -5, -5, -20, -20, 20, 20, 5, 5, 20, 20];
y = [40, 30, 30, -30, -30, -40, -40, -30, -30, 30, 30, 40];

x_c1 = 7.5;
y_c1 = 27.5;

x_c2 = -13.5;
y_c2 = 27.5;

r = 2.5;
r2 = 1;

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

% 図形のプロット
figure;

hold on;

fill(x, y, [1, 0.66, 0.66]); % 赤色で図形を塗りつぶす
fill(x_cir1, y_cir1, [0.7, 1, 0.7])
fill(x_cir2, y_cir2, [0.7, 1, 0.7])
fill(x_cir11, y_cir11, [0.0, 0.0, 0.0])
fill(x_cir21, y_cir21, [0.0, 0.0, 0.0])
axis equal; % 各軸のスケールを等しく保持

xlim([-50, 50]); % X軸の範囲を設定
ylim([-50, 50]); % Y軸の範囲を設定

hold off;