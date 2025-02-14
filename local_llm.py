from langchain_ollama import OllamaLLM


def get_llm(model_name: str):
    return OllamaLLM(model=model_name)


if __name__ == '__main__':
    llm = get_llm("deepseek-r1:8b")
    print(llm.invoke("How are you?"))