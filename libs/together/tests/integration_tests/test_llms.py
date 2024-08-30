"""Test Together API wrapper.
In order to run this test, you need to have an Together api key.
You can get it by registering for free at https://api.together.ai/.
A test key can be found at https://api.together.xyz/settings/api-keys
You'll then need to set TOGETHER_API_KEY environment variable to your api key.
"""

import pytest as pytest  # type: ignore[import-not-found]

from langchain_together import Together


def test_together_call() -> None:
    """Test simple call to together."""
    llm = Together(  # type: ignore[call-arg]
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0.2,
        max_tokens=250,
    )
    output = llm.invoke("Say foo:")

    assert llm._llm_type == "together"
    assert isinstance(output, str)
    assert len(output) > 0


async def test_together_acall() -> None:
    """Test simple call to together."""
    llm = Together(  # type: ignore[call-arg]
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0.2,
        max_tokens=250,
    )
    output = await llm.agenerate(["Say foo:"], stop=["bar"])

    assert llm._llm_type == "together"
    output_text = output.generations[0][0].text
    assert isinstance(output_text, str)
    assert output_text.count("bar") <= 1
