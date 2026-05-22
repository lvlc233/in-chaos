---
name: image2md
description: Use when the user wants to convert an image (screenshot, document scan, table) to markdown text via OCR. Trigger words: 图片转md, 图片转markdown, OCR, 提取文字.
---

# Image to Markdown (image2md)

Convert images to markdown via DeepSeek-OCR hosted on SiliconFlow.

## Requirements

- `SILICONFLOW_API_KEY` environment variable
- Python 3 with `openai` and `pillow` packages

## Usage

```bash
python image2md.py <image_path> [--output result.md]
```

The tool sends the image to DeepSeek-OCR and returns markdown-formatted text, preserving tables, structure, and layout.
