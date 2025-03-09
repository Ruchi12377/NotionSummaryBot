import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

prompt = """あなたはwebサイト上からスクレイピングされたテキストを要約するAIです。
    これからユーザーがテキストを入力します。そのテキストを日本語で要約してください.
    要約する際には以下の点を考慮してください:
    - 要約の結果にはMarkdownを用いることができます。
    - 要約はできるだけテキストだけではなく、箇条書きやリストを用いてわかりやすく要約してください。
    - 元の記事が構造的になっている場合、箇条書き等を用いてわかりやすく要約してください。
    - 要約時は元のテキストの要点を押さえ、冗長な情報は省いてください。
    - 要約の結果は日本語で出力してください。
    - 要約の結果には、元のテキストのリンクを含めないでください。
    - 元のテキストには記事の本文以外にも、広告やコメントなどが含まれることがありますが、要約の際には本文のみを要約してください。
"""

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def summarize_text(text):
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=text,
        config=types.GenerateContentConfig(
            system_instruction=[
                prompt
            ]
        )
    )
    return response.text