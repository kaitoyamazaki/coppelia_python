% ベクトル a と b の定義（ランダムな例）
a = [2 * rand - 1, 2 * rand - 1, 2 * rand - 1];
b = [2 * rand - 1, 2 * rand - 1, 2 * rand - 1];

% u と v のメッシュグリッドを生成
[u, v] = meshgrid(0:0.05:1, 0:0.05:1);

% メッシュグリッド内のすべての点について u + v <= 1 の条件を満たすものを選択
mask = (u + v <= 1);
u = u(mask);
v = v(mask);

% 平面上の点を計算
P = bsxfun(@times, u, a) + bsxfun(@times, v, b);

% 3次元空間に平面をプロット
scatter3(P(:, 1), P(:, 2), P(:, 3), 'filled');

% 軸のラベルとグリッドを追加
xlabel('X');
ylabel('Y');
zlabel('Z');
grid on;
axis equal;  % 各軸のスケールを同じにする
