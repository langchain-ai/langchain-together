"""Standard LangChain interface tests"""

from typing import Tuple, Type

from langchain_core.language_models import BaseChatModel
from langchain_tests.unit_tests import ChatModelUnitTests

from langchain_together import ChatTogether


class TestTogetherStandard(ChatModelUnitTests):
    @property
    def chat_model_class(self) -> Type[BaseChatModel]:
        return ChatTogether

    @property
    def chat_model_params(self) -> dict:
        return {"model": "meta-llama/Llama-3-8b-chat-hf"}

    @property
    def init_from_env_params(self) -> Tuple[dict, dict, dict]:
        return (
            {
                "TOGETHER_API_KEY": "api_key",
                "TOGETHER_API_BASE": "https://base.com",
            },
            {},
            {
                "together_api_key": "api_key",
                "together_api_base": "https://base.com",
            },
        )
