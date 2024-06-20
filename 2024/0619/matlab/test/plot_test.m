% パラメータの設定
r_inner = 0.1; % 内側の円の半径
r_outer = 0.3; % 外側の円の半径
N = 50; % 生成する点の数

% 極座標でランダムな点を生成
theta = 2 * pi * rand(N, 1); % ランダムな角度
r = sqrt((r_outer^2 - r_inner^2) * rand(N, 1) + r_inner^2); % 均一分布を保証するランダムな半径

% デカルト座標に変換
x = r .* cos(theta);
y = r .* sin(theta);

% y > 0 の条件を満たす点のみを選択
idx = y > 0;
x = x(idx);
y = y(idx);
z = -180 + 360 * rand(sum(idx), 1);

% 3次元プロット
figure;
scatter3(x, y, z, 'filled');
xlabel('X軸');
ylabel('Y軸');
zlabel('Z軸');
title('内側と外側の円の間の領域にランダムな3次元点をプロット');
grid on;
xlim([-r_outer, r_outer]); % x軸の範囲を設定
ylim([0, r_outer]); % y軸の範囲を設定
