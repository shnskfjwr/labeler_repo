# labeler_repo

GitHubのリポジトリに対し、ラベルを一括設定するスクリプトです。

- labels.ymlに定義されたラベルを設定
- nameが同じ場合は登録済みと判定し、色と説明に変更がある場合は更新
- labels.ymlに定義されていないラベルが存在した場合は削除

大量のリポジトリに1つ1つラベルを入れていくのが面倒だった＆既存のlabelerツールはAPIの実行制御が雑で実行数上限に引っかかってしまう作成しました。

## 前提条件
- 作業端末にpipenvがインストール済みであること
- 初期設定したいリポジトリの管理者権限を持つGitHubパーソナルアクセストークンが払い出し済みであること
- 初期設定したいリポジトリのオーナーがPro、Team、Enterpriseユーザーであること

## 実行方法

```bash
# 初期インストール
export PIPENV_VENV_IN_PROJECT=true
pipenv install

# 環境変数設定
cp .env_example .env

# GITHUB_TOKENとSEARCH_WORDを設定

pipenv shell
python labeler_repo.py

```

