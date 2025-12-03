
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader('https://www.saboresajinomoto.com.br/')
lista_documentos = loader.load() # nessa variável pedimos para extrair(scrap) todas as informações do site e armazenar


documentos = ''

for doc in lista_documentos:
    documentos += doc.page_content

# API KEY segura via Secrets
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model = 'llama-3.1-8b-instant')

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é uma assistente chamado AI_AGENT e tem acesso as seguintes informações: {documentos_informados}'),
    ('user', '{input}')

])

chain = template | chat
resposta = chain.invoke({
    'documentos_informados': documentos,
    'input': 'Quais as melhores receitas no top5?'
       
})

print(resposta.content)