from trafilatura import fetch_url, extract

async def get_content_by_url(url: str):
    try:
        downloaded = fetch_url(url)

        # メインのコンテンツをプレーンテキストで抽出
        result = extract(downloaded, with_metadata=True, output_format="markdown")

        # メタデータを取り出す
        metadata = {}
        content = []
        if result:
            lines = result.split('\n')
            in_metadata = False
            for line in lines:
                if line.strip() == '---':
                    in_metadata = not in_metadata
                    continue
                if in_metadata:
                    key, value = line.split(': ', 1)
                    metadata[key.strip()] = value.strip()
                else:
                    content.append(line)

        return metadata, '\n'.join(content).strip()

    except Exception as e:
        raise Exception(f"Error in get_content_by_url: {e}")
