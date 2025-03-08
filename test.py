import unittest
import os
from util.md2notionpage import parse_md

class TestParseMarkdown(unittest.TestCase):
    def test_from_file(self):
        # Test parsing markdown from test.md file
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'test.md')
            with open(file_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

            result = parse_md(markdown_content)
            self.assertIsNotNone(result)

            # Log or print content for debugging
            print(f"Parsed Markdown file: {file_path}")
            print(f"Result type: {type(result)}")
            print(f"Result preview: {str(result)}...")

            # Add assertions based on expected content in test.md
            # For example:
            # self.assertIn("Expected heading", str(result))
        except FileNotFoundError:
            self.fail(f"Test file not found: {file_path}")


if __name__ == "__main__":
    unittest.main()
