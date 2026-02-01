from pydantic import BaseModel, Field
from typing import Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI(model='gpt-4o')
class ClassifySchema(BaseModel):
    category: Literal["billing_delivery","technical","abuse","general"]=Field(description="Classfiy the text based on this category")
    sentiment: Literal["positive","neutral","negative"]=Field(description="Classify the sentiment")
    urgency: Literal["low","medium","high"]= Field(description="Classify the urgency based on this")