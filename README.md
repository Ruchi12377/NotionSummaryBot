# Notion Summary Bot

> **⚠️ 注意:** このプロジェクトはJavaScriptで書き換えられ、新しいバージョンが公開されています。  
> 最新のバージョンは [こちら](https://github.com/Ruchi12377/NotionMaid.git) を使用してください。

Discord Botがメンションされた際にURLを含むメッセージを検出し、そのURLのコンテンツを要約してNotionのページとして保存するBotです。

## 機能

- Discord上でボットがメンションされると、そのメッセージからURLを検出
- URLからコンテンツを抽出
- 抽出したコンテンツをGemini AIを使って要約
- 要約された内容をNotionページとして保存

## 環境のセットアップ

以下の手順に従って、仮想環境をアクティベートします。

1. 仮想環境を作成します

```shell
python3 -m venv venv
```

2. 仮想環境をアクティベートします。

    ```sh
    ./venv/Scripts/activate
    ```

    ```shell
    source ./venv/bin/activate
    ```

3. 必要なパッケージをインストールします。

    ```sh
    pip install -r requirements.txt
    ```

## 環境変数の設定

プロジェクトのルートディレクトリに`.env`ファイルを作成し、以下の環境変数を設定します:

```
DISCORD_TOKEN=your_discord_bot_token
NOTION_TOKEN=your_notion_integration_token
NOTION_PAGE_ID=your_parent_page_id
GEMINI_API_KEY=your_gemini_api_key
```

- DISCORD_TOKEN: Discord Developer Portalで取得したBot Token
- NOTION_TOKEN: Notionインテグレーションで取得したAPIトークン
- NOTION_PAGE_ID: ページを作成する親ページのID
- GEMINI_API_KEY: Google AI StudioでのGemini APIキー

## APIキーの取得方法

### 1. Notion APIの取得方法

Notion APIを利用するには、以下の手順でAPIキー（インテグレーショントークン）を取得します。

1. [Notionの開発者向けページ](https://www.notion.so/my-integrations)にアクセスし、Notionアカウントでログインします。
2. 「新しいインテグレーションを作成」し、必要な情報を入力してインテグレーションを作成します。
3. 作成後、表示される「インテグレーショントークン」をコピーして`.env`ファイルの`NOTION_TOKEN`に設定します。
4. Notionデータベースまたはページに作成したインテグレーションを共有（接続）する必要があります。使用したいページを開き、右上の「・・・」メニューから「接続を追加」を選択し、作成したインテグレーションを選択します。
5. 接続したページのIDを`.env`ファイルの`NOTION_PAGE_ID`に設定します。ページIDはURLの`https://www.notion.so/workspace/[ページID]`の部分から取得できます。

### 2. Gemini APIの取得方法

Gemini APIを利用するには、以下の手順でAPIキーを取得します。

1. [Google AI Studio](https://ai.google.dev/)にアクセスし、Googleアカウントでログインします。
2. 「Get API key」をクリックし、プロジェクトを作成またはプロジェクトを選択します。
3. 「APIキーを作成」をクリックし、表示されるAPIキーをコピーして`.env`ファイルの`GEMINI_API_KEY`に設定します。

### 3. Discord APIの取得方法

Discord APIを利用するには、以下の手順でBotトークンを取得します。

1. [Discord Developer Portal](https://discord.com/developers/applications)にアクセスし、Discordアカウントでログインします。
2. 「New Application」をクリックし、アプリケーション名を入力して作成します。
3. 左側のメニューから「Bot」を選択し、「Add Bot」をクリックしてBotを追加します。
4. 「Reset Token」をクリックしてトークンを生成し、表示される「TOKEN」をコピーして`.env`ファイルの`DISCORD_TOKEN`に設定します。
5. 左側のメニューから「OAuth2」→「URL Generator」を選択します。
6. 「Scopes」で「bot」を選択し、「Bot Permissions」で必要な権限（メッセージを送信する）を選択します。
7. 生成されたURLをブラウザで開き、Botを追加したいサーバーを選択します。

## 使い方

1. Botを起動します:

```shell
python main.py
```

2. DiscordのチャンネルでBotをメンションし、URLを含めたメッセージを送信します:

```
@NotionMaid https://example.com/article
```

3. Botは自動的にURLのコンテンツを取得し、要約して、Notionページとして保存します。

## プロジェクト構造

- `bot.py` - Discord Botのメイン実装
- `util/`
  - `get_content_by_url.py` - URLからコンテンツを抽出
  - `has_url_in_message.py` - メッセージにURLが含まれているか確認
  - `md2notionpage.py` - MarkdownをNotionページに変換
  - `symmarize_text.py` - Gemini AIを使用してテキストを要約
- `test.py` - Markdownパース機能のテスト

## テスト

テストを実行するには:

```shell
python test.py
```
