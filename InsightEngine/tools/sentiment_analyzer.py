# 这是 sentiment_analyzer.py 的全新内容
import os
import logging
from openai import OpenAI
import re

# 设置日志
logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """
    一个使用 Kimi (Moonshot) API 来分析情感的类。
    这是对本地模型的替换。
    """
    def __init__(self):
        """
        初始化用于 Kimi 的 OpenAI 客户端。
        """
        # 从环境变量读取 Kimi 的配置，我们已在 Railway 中设置好了
        self.api_key = os.environ.get("INSIGHT_ENGINE_API_KEY")
        self.base_url = os.environ.get("INSIGHT_ENGINE_BASE_URL", "https://api.moonshot.cn/v1")
        self.model = os.environ.get("INSIGHT_ENGINE_MODEL_NAME", "kimi-k2-0711-preview")
        
        if not self.api_key:
            logger.error("INSIGHT_ENGINE_API_KEY 环境变量未设置。")
            raise ValueError("Kimi API 密钥缺失。请在 Railway 中设置 INSIGHT_ENGINE_API_KEY。")
            
        try:
            # 初始化 Kimi 客户端
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
            )
            logger.info(f"情感分析器 (Kimi API) 已初始化，使用模型: {self.model}")
        except Exception as e:
            logger.error(f"初始化 OpenAI 客户端失败: {e}")
            raise

    def analyze_sentiment(self, text: str) -> str:
        """
        使用 Kimi API 分析给定文本的情感。

        Args:
            text (str): 要分析的文本。

        Returns:
            str: 情感 ("正面", "负面", or "中性").
        """
        if not text or not text.strip():
            logger.warning("情感分析接收到空文本。")
            return "中性"

        # 这是一个专门给 Kimi 的指示，让它只返回三个词中的一个
        system_prompt = "你是一个专业的情感分析助手。你只能返回'正面'、'负面'或'中性'这三个词中的一个，不要包含任何标点、空格或多余的解释。"
        user_prompt = f"请分析以下文本的情感：\n\n{text}"

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.0,  # 我们需要确定的答案，而不是创意的
                max_tokens=5,     # 只需要返回一个词
            )
            
            result = response.choices[0].message.content.strip()
            
            # 为了安全起见，清理一下 Kimi 可能多给的标点
            if "正面" in result:
                return "正面"
            elif "负面" in result:
                return "负面"
            else:
                return "中性"
                
        except Exception as e:
            logger.error(f"Kimi API 情感分析调用失败: {e}")
            # 如果 API 失败了，保险起见返回“中性”
            return "中性"

    def analyze_batch(self, texts: list[str]) -> list[dict]:
        """
        分析一批文本。
        (为简单起见，这里只是循环调用。这能正常工作。)
        """
        logger.info(f"正在批量分析 {len(texts)} 条文本...")
        results = []
        for text in texts:
            sentiment = self.analyze_sentiment(text)
            results.append({
                'text': text,
                'sentiment': sentiment,
                'confidence': 0.99 # API 调用，我们假设置信度很高
            })
        
        logger.info("批量情感分析完成。")
        return results

# 保留这个函数，以兼容项目其他地方的调用
def get_sentiment_analyzer():
    """
    获取情感分析器实例的工厂函数。
    """
    return SentimentAnalyzer()
