# mpc-learning

MP-SPDZをDocker上で動かし、秘密計算プログラムを実装・実行するための学習用リポジトリ。

## ディレクトリ構成

```text
mpc-learning/
├── README.md
├── MP-SPDZ/        # MP-SPDZ本体（Git管理対象外）
├── Player-Data/    # 秘密入力ファイル（Git管理対象外）
├── programs/       # 自作 .mpc ファイル
└── python/         # mpcに対応するPythonプログラム
```

## セットアップと実行

### MP-SPDZの取得

`MP-SPDZ/` がまだない場合だけ実行する。

```bash
make get-mpspdz
```

### Dockerイメージのビルド

```bash
make build
```

### tutorial の実行

```bash
make tutorial
```

### コンテナ内の作業ディレクトリ

```bash
make pwd
```

出力は以下になる。

```text
/usr/src/MP-SPDZ
```

### 自作 `.mpc` ファイルの配置

Dockerで実行する場合は、ホスト側の `programs/` をコンテナ内の
`Programs/Source/user_programs/` にマウントするのが扱いやすい。

このリポジトリでは、以下のように配置する。

```text
programs/tutorial_ja.mpc
```

コンテナ内では以下として見える。

```text
/usr/src/MP-SPDZ/Programs/Source/user_programs/tutorial_ja.mpc
```

### 自作プログラムの実行

例：`programs/tutorial_ja.mpc` を実行する場合。

```bash
make run PROGRAM=tutorial_ja
```

別のファイルを実行する場合は、拡張子 `.mpc` を外して指定する。

```bash
make run PROGRAM=max_min
make run PROGRAM=bubble_sort
```

`PROGRAM` を省略した場合は `tutorial_ja` を実行する。

### 秘密入力ファイルを使う場合

秘密入力は `Player-Data/Input-P<i>-0` に置く。
`Player-Data/` はDocker実行時にコンテナ内の `Player-Data/` としてマウントされる。

例: Party 0 が配列、Party 1 が探索対象を入力する場合。

```text
Player-Data/Input-P0-0
0 2 4 9 16
```

```text
Player-Data/Input-P1-0
4
```

### 自作プログラムの実行（MP-SPDZ内に直接置く場合）

`MP-SPDZ/Programs/Source/` に `.mpc` ファイルを置いてDockerイメージに含めたい場合は、
ファイルを置いたあとにDockerイメージをビルドし直す必要がある。

ビルド済みのDockerイメージには、ビルド後にホスト側で追加したファイルは反映されない。

## 学習予定

### アルゴリズム
```text
tutorial
↓
max/min
↓
compare-and-swap
↓
bubble sort
↓
linear search
↓
binary search
```

### 入力形式

`.mpc` 内に入力値を直書き → 複数パーティの秘密入力
- 例: Party 0 が配列を入力し、Party 1 が探索対象の値を入力する
- 配列長などのサイズ情報は公開値として `.mpc` 側に固定しておく
