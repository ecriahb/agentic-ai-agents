from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_template(
    "Explain this incident in exactly three evidence-aware bullets: {incident}"
)
llm = ChatOllama(model="qwen2.5:3b", temperature=0)
parser = StrOutputParser()

chain = prompt | llm | parser

print(chain.invoke({
    "incident": "AKS deployment failed after an NSG rule was removed"
}))
