from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an evidence-first DevOps incident analyst."),
    ("human", "Environment: {environment}\nIncident: {incident}\nGive only evidence-aware next checks."),
])
llm = ChatOllama(model="qwen2.5:3b", temperature=0)
chain = prompt | llm

result = chain.invoke({
    "environment": "production",
    "incident": "AKS deployment failed after Terraform networking change",
})
print(result.content)
