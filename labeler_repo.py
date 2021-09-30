import os
import time
import yaml
from dotenv import load_dotenv
from github import Github

load_dotenv()
g = Github(os.environ['GITHUB_TOKEN'])


def handler():

    # ラベル設定ファイル読み込み
    with open('labels.yml', 'r') as yml:
        new_labels = yaml.safe_load(yml)

    # アクセス可能な全リポジトリから特定文字列を含むリポジトリを抽出
    for repo in g.get_user().get_repos():
        if os.environ['SEARCH_WORD'] in repo.name:
            print(repo.name)
            labeling(repo, new_labels)
            # API実行上限調整
            time.sleep(2)


def labeling(repo, new_labels):

    required_labels = []

    # 設定済みラベルチェック
    for label in repo.get_labels():
        for new_label in new_labels:
            # nameで同一ラベルか判断
            if label.name == new_label['name']:
                required_labels.append(label.name)
                # 色か説明に変更があった場合は更新
                if label.color != new_label['color'] or label.description != new_label['description']:
                    label.edit(
                        name=new_label['name'],
                        color=new_label['color'],
                        description=new_label['description'],
                    )
                    print(f'update: {repo.name} {label.name}')

                continue

        # 不要なラベルは削除
        if label.name not in required_labels:
            print(f'delete: {repo.name} {label.name}')
            label.delete()

    # 新規ラベルの追加
    for new_label in new_labels:
        if new_label['name'] not in required_labels:
            repo.create_label(
                name=new_label['name'],
                color=new_label['color'],
                description=new_label['description'],
            )

            print(f'create: {repo.name} {new_label["name"]}')


if __name__ == '__main__':
    handler()
