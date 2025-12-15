# 🏦 Banco DevBrito.py - Sistema Bancário Modular

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%Andamento-success?style=for-the-badge)

> Projeto desenvolvido como parte do desafio de **Back-End com Python** da **DIO (Digital Innovation One)** em parceria com a **Luiza Labs**.

## 📄 Sobre o Projeto

Este projeto consiste na evolução de um sistema bancário simples para uma aplicação modular e estruturada. O objetivo foi refatorar o código monolítico inicial, aplicando boas práticas de programação, **validação de dados robusta** e separação de responsabilidades.

O sistema simula operações bancárias via terminal, gerenciando clientes e contas em memória utilizando estruturas de dados relacionais (Dicionários e Listas).

## ✨ Funcionalidades

O sistema conta com um menu interativo que oferece as seguintes operações:

### 👤 Gestão de Clientes e Contas
* **Cadastrar Usuário:** Criação de perfil com validação rigorosa de dados.
* **Cadastrar Conta Bancária:** Criação de conta vinculada a um CPF existente. O sistema suporta múltiplas contas para um mesmo usuário.
* **Listar Usuários:** Exibição detalhada dos clientes, cruzando informações para mostrar todas as contas vinculadas a cada CPF.

### 💰 Operações Financeiras
* **Depositar:** Adição de valores ao saldo (Argumentos *positional-only*).
* **Sacar:** Retirada de valores com verificação de saldo, limite diário e quantidade de saques (Argumentos *keyword-only*).
* **Extrato:** Visualização do histórico de transações e saldo atual.


## 🛡️ Camada de Validação e Segurança

Diferente de sistemas básicos, esta versão implementa funções dedicadas para garantir a integridade ("sanitization") dos dados inseridos:

* ✅ **Validação de CPF:** Impede CPFs com letras ou tamanho incorreto (deve ter 11 dígitos).
* ✅ **Validação de Nome:** Impede cadastro de nomes vazios ou contendo números.
* ✅ **Validação de Data:** Garante o formato `DD/MM/AAAA` e verifica logicamente se dia, mês e ano são válidos (ex: impede mês 13 ou dia 32).
* ✅ **Endereço:** Impede o cadastro de endereços em branco.


## 🛠️ Destaques Técnicos (Implementação)

O projeto foca no uso avançado de assinaturas de funções em Python e estruturação de dados:

### 1. Positional-Only Parameters (`/`)
Utilizado na função `depositar`. Obriga que os argumentos sejam passados apenas pela ordem, garantindo uma interface limpa.
```python
def depositar(valor, saldo, extrato, /): ...
```
### 2.Keyword-Only Parameters (*)
Utilizado na função sacar. Obriga que argumentos críticos (como limites e valores) sejam nomeados explicitamente na chamada.
```python
def sacar(*, p_valor, p_saldo, ...): ...
``` 
### 3. Estrutura de Dados Relacional
O sistema simula um banco de dados relacional em memória:
O dicionário de usuários armazena uma lista `["contas"]`.
Ao criar uma conta, o ID dela é anexado à lista do usuário correspondente.
A função `listar_usuarios` faz um "join" manual entre os dicionários para exibir o relatório completo.

## 👨‍💻 Autor

Desenvolvido por Jovem Brito Jr.

### Links Úteis:
LinkedIn: https://www.linkedin.com/in/israelbritojr/
GitHub: https://github.com/israelbritodev?tab=repositories
Instagram: https://www.instagram.com/jovembritojr/