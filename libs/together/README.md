# langchain-together

This package contains the LangChain integration with Together AI.

## Installation

```bash
pip install langchain-together
```

## Chat Models

`ChatTogether` supports the various [models](https://docs.together.ai/docs/inference-models) available via the Together API:

```python
from langchain_together import ChatTogether
import os


os.environ["TOGETHER_API_KEY"] = "my-key"


llm = ChatTogether(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # api_key="...",  # if not set in environment variable
)
```

## Structured Outputs, Function Calls, JSON Mode

`ChatTogether` supports structured outputs using Pydantic models, dictionaries, or JSON schemas. This feature allows you to get reliable, structured responses from Together AI models. See here the docs for more info about [function calling](https://docs.together.ai/docs/function-calling) and [structured outputs](https://docs.together.ai/docs/json-mode)


```python
from langchain_together import ChatTogether
from pydantic import BaseModel, Field
from typing import Optional

class Joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline of the joke")
    rating: Optional[int] = Field(default=None, description="How funny the joke is from 1-10")

# Use a model that supports function calling
llm = ChatTogether(model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
structured_llm = llm.with_structured_output(Joke.model_json_schema(), method="json_schema")

result = structured_llm.invoke("Tell me a joke about programming")
print(f"Setup: {result.setup}")
print(f"Punchline: {result.punchline}")
print(f"Rating: {result.rating}")
```

### Function Calling  


```python

# Use a model that supports function calling
llm = ChatTogether(model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
structured_llm = llm.with_structured_output(Joke, method="function_calling")

result = structured_llm.invoke("Tell me a joke about programming")
print(f"Setup: {result.setup}")
print(f"Punchline: {result.punchline}")
print(f"Rating: {result.rating}")
```

### JSON Mode 

For models that support JSON mode, you can also use this method:

```python
from langchain_together import ChatTogether
from pydantic import BaseModel, Field

class Response(BaseModel):
    message: str = Field(description="The main message")
    category: str = Field(description="Category of the response")

# Use a model that supports JSON mode
llm = ChatTogether(model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
structured_llm = llm.with_structured_output(Response.model_json_schema(), method="json_mode")

result = structured_llm.invoke(
    "Respond with a JSON containing a message about cats and categorize it. "
    "Use the exact keys 'message' and 'category'."
)
```

## Embeddings

```python
from langchain_together import TogetherEmbeddings

embeddings = TogetherEmbeddings(model="BAAI/bge-base-en-v1.5")
```