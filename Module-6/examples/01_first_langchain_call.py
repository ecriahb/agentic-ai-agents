from langchain_ollama import ChatOllama


def main():
    llm = ChatOllama(model="qwen2.5:3b", temperature=0)
    response = llm.invoke("Explain AKS in two simple lines for a DevOps engineer.")
    print(response.content)


if __name__ == "__main__":
    main()
