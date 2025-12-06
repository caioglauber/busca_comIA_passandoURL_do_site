Nesse projeto se for feito no VScode pressione ctrl+shift+ p para mudar a vesão do python. 
Nesse escolhi a versão 3.11 do pytho para evitar incompatibilidade de versões.

  No termional do VsCode instale as bibliotecas:
pip install langchain
pip install langchain-groq
pip install langchain-community

## 🔐 Configuração da API Key (Groq)

Este projeto utiliza a API da Groq para geração de respostas com IA.

Antes de executar o projeto, configure a variável de ambiente `GROQ_API_KEY` com sua chave de acesso.

###  Digite no CMD, PowerShell ou terminal do VSCODE:
setx GROQ_API_KEY "SUA_CHAVE_AQUI"
