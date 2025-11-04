import os

# [MySQL数据库配置]
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "your_password")
DB_NAME = os.environ.get("DB_NAME", "mindspider")
DB_CHARSET = os.environ.get("DB_CHARSET", "utf8mb4")

# [LLM配置] - 必填
# Kimi / Moonshot
INSIGHT_ENGINE_API_KEY = os.environ.get("INSIGHT_ENGINE_API_KEY")
INSIGHT_ENGINE_BASE_URL = os.environ.get("INSIGHT_ENGINE_BASE_URL", "https://api.moonshot.cn/v1")
INSIGHT_ENGINE_MODEL_NAME = os.environ.get("INSIGHT_ENGINE_MODEL_NAME", "kimi-k2-0711-preview")

MEDIA_ENGINE_API_KEY = os.environ.get("INSIGHT_ENGINE_API_KEY") # 默认共用
MEDIA_ENGINE_BASE_URL = os.environ.get("INSIGHT_ENGINE_BASE_URL", "https://api.moonshot.cn/v1")
MEDIA_ENGINE_MODEL_NAME = os.environ.get("INSIGHT_ENGINE_MODEL_NAME", "kimi-k2-0711-preview")

QUERY_ENGINE_API_KEY = os.environ.get("INSIGHT_ENGINE_API_KEY") # 默认共用
QUERY_ENGINE_BASE_URL = os.environ.get("INSIGHT_ENGINE_BASE_URL", "https://api.moonshot.cn/v1")
QUERY_ENGINE_MODEL_NAME = os.environ.get("INSIGHT_ENGINE_MODEL_NAME", "kimi-k2-0711-preview")

# 其他配置... (保持原样即可)
# （注意：为了简洁，我省略了原文件中的其他配置项，它们会使用默认值或暂时用不到）
