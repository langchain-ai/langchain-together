"""Standard LangChain interface tests"""

from typing import Tuple, Type

from langchain_core.embeddings import Embeddings
from langchain_standard_tests.unit_tests.embeddings import EmbeddingsUnitTests

from langchain_together import TogetherEmbeddings


class TestTogetherStandard(EmbeddingsUnitTests):
    @property
    def embeddings_class(self) -> Type[Embeddings]:
        return TogetherEmbeddings

    @property
    def embeddings_params(self) -> dict:
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
