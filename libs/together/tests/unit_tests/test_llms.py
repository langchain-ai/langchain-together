from typing import cast

from langchain_core.pydantic_v1 import SecretStr
from pytest import CaptureFixture, MonkeyPatch  # type: ignore[import-not-found]

from langchain_together import Together


def test_together_api_key_is_secret_string() -> None:
    """Test that the API key is stored as a SecretStr."""
    llm = Together(
        together_api_key="secret-api-key",  # type: ignore[call-arg]
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0.2,
        max_tokens=250,
    )
    assert isinstance(llm.together_api_key, SecretStr)


def test_together_api_key_masked_when_passed_from_env(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture
) -> None:
    """Test that the API key is masked when passed from an environment variable."""
    monkeypatch.setenv("TOGETHER_API_KEY", "secret-api-key")
    llm = Together(  # type: ignore[call-arg]
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0.2,
        max_tokens=250,
    )
    print(llm.together_api_key, end="")
    captured = capsys.readouterr()

    assert captured.out == "**********"


def test_together_api_key_masked_when_passed_via_constructor(
    capsys: CaptureFixture,
) -> None:
    """Test that the API key is masked when passed via the constructor."""
    llm = Together(
        together_api_key="secret-api-key",  # type: ignore[call-arg]
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0.2,
        max_tokens=250,
    )
    print(llm.together_api_key, end="")
    captured = capsys.readouterr()

    assert captured.out == "**********"


def test_together_uses_actual_secret_value_from_secretstr() -> None:
    """Test that the actual secret value is correctly retrieved."""
    llm = Together(
        together_api_key="secret-api-key",  # type: ignore[call-arg]
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0.2,
        max_tokens=250,
    )
    assert cast(SecretStr, llm.together_api_key).get_secret_value() == "secret-api-key"


def test_together_uses_actual_secret_value_from_secretstr_api_key() -> None:
    """Test that the actual secret value is correctly retrieved."""
    llm = Together(
        api_key="secret-api-key",  # type: ignore[arg-type]
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0.2,
        max_tokens=250,
    )
    assert cast(SecretStr, llm.together_api_key).get_secret_value() == "secret-api-key"


def test_together_model_params() -> None:
    # Test standard tracing params
    llm = Together(
        api_key="secret-api-key",  # type: ignore[arg-type]
        model="foo",
    )
    ls_params = llm._get_ls_params()
    assert ls_params == {
        "ls_provider": "together",
        "ls_model_type": "llm",
        "ls_model_name": "foo",
        "ls_max_tokens": 200,
    }

    llm = Together(
        api_key="secret-api-key",  # type: ignore[arg-type]
        model="foo",
        temperature=0.2,
        max_tokens=250,
    )
    ls_params = llm._get_ls_params()
    assert ls_params == {
        "ls_provider": "together",
        "ls_model_type": "llm",
        "ls_model_name": "foo",
        "ls_max_tokens": 250,
        "ls_temperature": 0.2,
    }
