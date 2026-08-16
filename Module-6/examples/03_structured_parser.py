from typing import Literal
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


class RCA(BaseModel):
    root_cause: str
    impact: str
    next_check: str
    confidence: Literal["low", "medium", "high"]


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an evidence-first DevOps analyst. Do not invent facts."),
    ("human", "Incident: {incident}\nEvidence: {evidence}"),
])

llm = ChatOllama(model="qwen2.5:3b", temperature=0)
structured_llm = llm.with_structured_output(RCA)
chain = prompt | structured_llm

result = chain.invoke({
    "incident": "Production deployment failed",
    "evidence": "Deployment failed during Terraform Apply. NSG rule aks-subnet-allow was removed.",
})
print(result)
