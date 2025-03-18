import os
from pathlib import Path

API_ALIAS = {
    'OPENAI': 'OPENAI_API_KEY',
    'ANTHROPIC': 'ANTHROPIC_API_KEY',
    'GEMINI': 'GEMINI_API_KEY',
    'TOGETHER': 'TOGETHER_API_KEY',
    'GOOGLE_SEARCH': 'GOOGLE_API_KEY',
    'GOOGLE_CSE': 'GOOGLE_CSE_ID'
}

def load_api_keys(key_cfg=None, keys={}):
    if key_cfg:
        keys = Path(key_cfg).open("r")
        for line in keys:
            if line.startswith("#"):
                continue
            tag, k = line.strip().split("=")
            os.environ[API_ALIAS[tag]] = k
        keys.close()
    elif keys:
        for k, v in keys.items():
            os.environ[API_ALIAS[k]] = v