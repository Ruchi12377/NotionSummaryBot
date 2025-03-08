# Notion Summary Bot

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

## 使い方

1. Botを起動します:

```shell
python bot.py
```

2. DiscordのチャンネルでBotをメンションし、URLを含めたメッセージを送信します:

```
@NotionSummaryBot https://example.com/article
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
