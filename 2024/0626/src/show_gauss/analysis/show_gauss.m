% 取得したwrenchデータより, モーメントを利用して正規分布を展開する.

clear;

addpath('.', '-end');
addpath('../data', '-end');

filepath = '../data/object_wrench.mat';
data = load(filepath);
data = data.object_wrench;
data(isnan(data)) = 0;

row = size(data,1);

% 移動平均フィルタを適用する
size = 5;
fx = movmean(data(:,2), size);
fy = movmean(data(:,3), size);
m = movmean(data(:,4), size);

data = [data(:,1), fx, fy, m];
negative_row = 1000;

for i = 1:row
    if(data(i, 2) > 0)
        negative_row = i;
        break;
    end
end

data = data(1:negative_row, :);

data_moment = data(:,4);

pd = fitdist(data_moment, 'Normal');

mu = pd.mu;
sigma = pd.sigma;

%  xの範囲を設定
x = linspace(min(data_moment), max(data_moment), 100);

% 正規分布の確率密度関数を計算
y = pdf(pd, x);

% グラフを描画
figure;
%histogram(data_moment, 'Normalization', 'pdf');
hold on;

plot(x, y, 'LineWidth', 2);

xlabel('値');
ylabel('確率密度');
grid on;
hold off;