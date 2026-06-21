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
cd mpc-learning
git clone https://github.com/data61/MP-SPDZ.git
```

### Dockerイメージのビルド

Dockerfileは `MP-SPDZ/` の中にあるため、そこでビルドする。

```bash
cd mpc-learning/MP-SPDZ
docker build --tag mpspdz:mascot-party --build-arg machine=mascot-party.x .
```

### tutorial の実行

```bash
docker run --rm -it -e PLAYERS=2 mpspdz:mascot-party ./Scripts/compile-run.py mascot tutorial
```

### コンテナ内の作業ディレクトリ

```bash
docker run --rm -it mpspdz:mascot-party pwd
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
cd mpc-learning
docker run --rm -it \
  -e PLAYERS=2 \
  -v "$PWD/programs:/usr/src/MP-SPDZ/Programs/Source/user_programs:ro" \
  mpspdz:mascot-party \
  ./Scripts/compile-run.py mascot user_programs/tutorial_ja
```

別のファイルを実行する場合は、拡張子 `.mpc` を外して指定する。

```text
programs/max_min.mpc        -> user_programs/max_min
programs/bubble_sort.mpc    -> user_programs/bubble_sort
```

### MP-SPDZ内に直接置く場合

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
