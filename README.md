# 🦜️🔗 LangChain Together

This repository contains 1 package with Together integrations with LangChain:

- [langchain-together](https://pypi.org/project/langchain-together/)

## Setup for Testing

```bash
cd libs/together
poetry install --with lint,typing,test,test_integration,
```

## Running the Unit Tests

```bash
cd libs/together
make tests
```

## Running the Integration Tests

```bash
cd libs/together
export TOGETHER_API_KEY=<your-api-key>
make integration_tests
```