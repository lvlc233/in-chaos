"""
Image to Markdown OCR using DeepSeek-OCR via SiliconFlow API.

Requires:
    pip install openai pillow

Usage:
    python ocr.py image.png
    python ocr.py scan.jpg --output result.md
"""

import base64
import sys
import argparse
from pathlib import Path

from openai import OpenAI

API_KEY = "sk-gdzmlhbvhiylarhcsildshslbqbdyxtjawhgmfqufzsqcsgn"
BASE_URL = "https://api.siliconflow.cn/v1"
MODEL = "deepseek-ai/DeepSeek-OCR"


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def image_to_markdown(image_path: str) -> str:
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    ext = Path(image_path).suffix.lower()
    mime_map = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
                ".webp": "image/webp", ".bmp": "image/bmp", ".gif": "image/gif"}
    mime_type = mime_map.get(ext, "image/png")

    b64 = encode_image(image_path)
    data_uri = f"data:{mime_type};base64,{b64}"

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": data_uri}},
                {"type": "text", "text": "<image>\n<|grounding|>Convert the document to markdown."},
            ]
        }],
        temperature=0.0,
        max_tokens=8192,
    )

    return response.choices[0].message.content


def main():
    parser = argparse.ArgumentParser(description="Convert image to markdown via DeepSeek-OCR")
    parser.add_argument("image", help="Path to image file")
    parser.add_argument("--output", "-o", help="Output markdown file (print to stdout if not set)")
    args = parser.parse_args()

    if not Path(args.image).is_file():
        print(f"Error: image file not found: {args.image}", file=sys.stderr)
        sys.exit(1)

    print(f"Processing: {args.image}", file=sys.stderr)
    result = image_to_markdown(args.image)

    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
        print(f"Saved to: {args.output}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
