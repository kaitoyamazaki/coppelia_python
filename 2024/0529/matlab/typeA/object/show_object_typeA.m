% レンチの値によって出る法線ベクトルを２次元座標系でプロットするプログラム

% 多角形の座標系を定義
x = [-20, -20, -5, -5, -20, -20, 20, 20, 5, 5, 20, 20];
y = [40, 30, 30, -30, -30, -40, -40, -30, -30, 30, 30, 40];

% エンドエフェクタ1の定義
x_c1 = 7.5;
y_c1 = 27.5;

% エンドエフェクタ2の定義
x_c2 = -12.5;
y_c2 = 27.5;

% CoP(center of hand)の定義
x_cop = (x_c1 + x_c2) / 2;
y_cop = (y_c1 + y_c2) / 2;

% エンドエフェクタのサイズを定義
r = 2.5;

% エンドエフェクタの中心の円を定義
r2 = 1;

% CoPのサイズを定義
r3 = 1.5;

% 接触点の定義
p1 = [x_c1, y_c1+r];
p2 = [x_c1-r, y_c1];
p3 = [x_c2, y_c2+r];

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
xlabel('Fx   [N]');
ylabel('Fy   [N]');