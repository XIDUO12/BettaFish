import os

# [MySQL数据库配置]
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "your_password")
DB_NAME = os.environ.get("DB_NAME", "mindspider")
DB_CHARSET = os.environ.get("DB_CHARSET", "utf8mb4")

# [LLM配置]
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "your_api_key_here")
OPENAI_API_BASE = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")

# ... 其他配置将使用默认值 ...
