# mpc-learning

MP-SPDZをDocker上で動かし、秘密計算プログラムを実装・実行するための学習用リポジトリ。

## ディレクトリ構成

```text
mpc-learning/
├── README.md
├── MP-SPDZ/        # MP-SPDZ本体（Git管理対象外）
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

### 自作プログラムの実行（MP-SPDZ内に直接置く場合）

`MP-SPDZ/Programs/Source/` に `.mpc` ファイルを置いてDockerイメージに含めたい場合は、
ファイルを置いたあとにDockerイメージをビルドし直す必要がある。

ビルド済みのDockerイメージには、ビルド後にホスト側で追加したファイルは反映されない。

## 学習予定

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
oblivious search
```
