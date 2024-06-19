% シミュレーションから取得したデータからcog1がどのように方向が変化しているか出力する

% 初期化
clear;

% 検索フォルダの読み込み
addpath('.', '-end');
addpath('..', '-end');
addpath('res', '-end');

% ファイルの読み込み
filepath = '../cog1_pos.csv';
cog1_direction = readmatrix(filepath);

% 質量や摩擦係数, 物体座標系での位置ベクトル
mass = 0.00159;
mu = 0.80;
position_vector = [0.0, -0.0125, 0.0350];
cog1_friction = mass * mu;

row = size(cog1_direction, 1);

data = [];
nece_data = [];

for i = 1:row
    if(i > 1 && cog1_direction(i-1) == cog1_direction(i))
        continue
    end

    % 方向ベクトル
    direction = [cog1_direction(i, 2) cog1_direction(i, 3)];

    % 方向ベクトルのノルム入手
    now_norm = sqrt(sum(direction.^2));

    % 方向ベクトルの単位ベクトル
    unit_direction = [direction(1) / now_norm direction(2) / now_norm];

    % 単位ベクトルを利用し, 摩擦力ベクトルを計算
    friction_vector = cog1_friction * unit_direction;
    neg_friction_vector = -1 * friction_vector;

    % 摩擦力モーメントを計算
    now_friction_force = [neg_friction_vector(1); neg_friction_vector(2); 0];
    position_cog1 = [position_vector(2), position_vector(3), 0];

    friction_moment = cross(position_cog1, now_friction_force);
    friction_moment = friction_moment(3);

    data(end+1) = cog1_direction(i, 1);
    data(end+1) = friction_moment;

    nece_data = [nece_data; data];
    data = [];
end

friction_moment = nece_data;

figure;
hold on;
grid on;

x = friction_moment(:, 1);
y = friction_moment(:, 2);

ylim([-0.00025, 0.00025]);

plot(x, y);

hold off;