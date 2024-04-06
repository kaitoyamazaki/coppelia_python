% 凸包の内部点を見つけるためのサンプリング範囲とステップサイズを設定
x_range = linspace(-1, 1, 100);
y_range = linspace(-1, 1, 100);
z_range = linspace(-0.03, 0.03, 100);

% 内部点を保存するための配列を初期化
internal_points = [];

% すべてのx, y, zの組み合わせに対して条件をチェック
for x = x_range
    for y = y_range
        for z = z_range
            % すべての不等式を満たすかチェック
            if (0.0275*x - 0.0075*y + z <= 0) && (-0.0275*x - 0.0125*y - z <= 0) && (0.02*x <= 0)
                % 条件を満たす点を配列に追加
                internal_points = [internal_points; x, y, z];
            end
        end
    end
end

% プロット初期化
figure;
hold on;

plot3(internal_points(:,1), internal_points(:,2),internal_points(:,3), '.');

% 軸ラベル
xlabel('x');
ylabel('y');
zlabel('z');

% 表示範囲の設定
%axis equal;
xlim([-1, 1]);
ylim([-1, 1]);
zlim([-0.03, 0.03]);

% グリッド表示
grid on;

% X軸
line([min(get(gca, 'XLim')) max(get(gca, 'XLim'))], [0 0], [0 0], 'Color', 'red', 'LineWidth', 2);

% Y軸
line([0 0], [min(get(gca, 'YLim')) max(get(gca, 'YLim'))], [0 0], 'Color', 'green', 'LineWidth', 2);

% Z軸
line([0 0], [0 0], [min(get(gca, 'ZLim')) max(get(gca, 'ZLim'))], 'Color', 'blue', 'LineWidth', 2);

view(45, 45);

hold off;