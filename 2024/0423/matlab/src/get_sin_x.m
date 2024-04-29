% 定数の設定
increment = 0.01; % グラフの精度を設定
theta = 0:increment:2*pi; % thetaの範囲を0から2*piまで設定

% 式の計算
y = 2.072 * sin(theta + 1.3736);

% 結果のプロット
figure;
plot(theta, y);
hold on;
yline(0, '--'); % y = 0 の線を追加
xlabel('\theta (radians)');
ylabel('2.072*sin(\theta + 1.3736)');
title('Graph of 2.072*sin(\theta + 1.3736)');

% thetaの範囲を表示するためのコード
theta_positive = theta(y > 0); % yが正のtheta値を抽出
disp('Theta ranges where 2.072*sin(theta + 1.3736) > 0:');
disp(['From ', num2str(min(theta_positive)), ' to ', num2str(max(theta_positive)), ' radians']);

% 他の範囲も計算する場合
%k = 1; % kを変更して異なる範囲を調べる
%while max(theta_positive) + 2*k*pi <= 10 % 調べたい上限値まで
%    additional_range = theta_positive + 2*k*pi;
%    disp(['From ', num2str(min(additional_range)), ' to ', num2str(max(additional_range)), ' radians']);
%    k = k + 1;
%end