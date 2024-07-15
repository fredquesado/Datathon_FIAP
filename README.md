# TechChallenge4
 Tech Challenge 4 para a pós na FIAP de Data Analytics

 Site com o trabalho: https://techchallenge4.streamlit.app/
 
# Análise e Previsão do Preço do Petróleo Brent

## Descrição
Esta aplicação utiliza dados históricos do preço do petróleo Brent para realizar diversas análises e visualizações, ajudando a identificar padrões e tendências no mercado de petróleo.

## Instalação
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/Vandrade85/TechChallenge4.git
cd TechChallenge4
pip install -r requirements.txt

### Deploy de Aplicações com Streamlit Cloud e GitHub

**Sumário**
1. Introdução
2. Preparação do Ambiente de Desenvolvimento
3. Configuração do GitHub
4. Integração com Streamlit Cloud
5. Automatização do Deploy com GitHub Actions
6. Monitoramento e Manutenção
7. Conclusão
8. Referências

---

### 1. Introdução

**1.1 O que é Deploy e por que é Importante**

O termo "deploy" refere-se ao processo de disponibilizar uma aplicação ou software para uso em um ambiente de produção, após a fase de desenvolvimento e testes. Este processo envolve configurar o software em servidores ou plataformas de hospedagem, garantindo que ele esteja acessível aos usuários finais ou sistemas que dele dependem. O deploy pode ser realizado manualmente ou de forma automatizada, sendo a automação frequentemente integrada em sistemas de integração contínua e entrega contínua (CI/CD).

**Importância do Deploy:**
1. **Acesso dos Usuários:** Tornar a aplicação disponível para os usuários finais é o principal objetivo do deploy. Sem um deploy eficaz, o software, por mais bem desenvolvido que seja, permanece inacessível e, portanto, inútil para aqueles para quem foi projetado.
2. **Ambiente de Produção Real:** Permite que o software opere em um ambiente de produção real, essencial para avaliar o desempenho da aplicação em condições práticas. Isso é fundamental, pois um ambiente de produção pode diferir significativamente dos ambientes de desenvolvimento e teste em termos de configuração, carga de uso e integração com outros sistemas.
3. **Feedback e Iterações:** Uma vez que o software está em produção, os desenvolvedores podem coletar dados reais e feedback dos usuários. Esse feedback é crucial para iterar sobre o produto, corrigindo bugs, melhorando funcionalidades e ajustando o desempenho com base nas necessidades e experiências reais dos usuários.
4. **Continuidade de Negócios e Atualizações:** Um deploy eficaz assegura que as atualizações e manutenções do software possam ser realizadas com o mínimo de interrupção para os usuários. Isso é especialmente importante em ambientes empresariais, onde tempo de inatividade pode significar perda de produtividade e receita.
5. **Escalabilidade e Gestão de Recursos:** Através do deploy, as organizações podem gerenciar e escalar a infraestrutura de acordo com a demanda. Isso é crucial para manter a eficiência operacional e controlar custos, especialmente com o uso de soluções baseadas em nuvem que permitem ajustar recursos rapidamente.
6. **Segurança:** Um deploy bem planejado inclui medidas robustas de segurança para proteger o aplicativo e os dados dos usuários contra ameaças e vulnerabilidades. Isso é fundamental para manter a confiança dos usuários e cumprir regulamentos de proteção de dados.
7. **Vantagem Competitiva:** Empresas que conseguem deployar inovações de software de forma rápida e eficiente geralmente têm uma vantagem competitiva. Isso permite que elas respondam melhor às tendências do mercado e às demandas dos clientes.

**1.2 Apresentação do Streamlit e GitHub como Ferramentas para Desenvolvimento e Deploy de Aplicações**

**Streamlit:** Streamlit é uma ferramenta de código aberto que permite aos desenvolvedores criar e compartilhar aplicações de dados de maneira rápida e fácil, utilizando apenas Python. Ele é amplamente utilizado para criar dashboards interativos e aplicações de machine learning. A simplicidade de uso e a capacidade de criar interfaces de usuário interativas com poucas linhas de código tornam o Streamlit uma escolha popular entre cientistas de dados e desenvolvedores.

**Características Principais do Streamlit:**
- **Facilidade de Uso:** Permite criar aplicações web interativas com Python puro, sem necessidade de conhecimentos em frontend.
- **Desenvolvimento Rápido:** Facilita a prototipagem rápida e iterativa.
- **Integração com Machine Learning:** Permite a integração fácil com modelos de machine learning e bibliotecas de visualização de dados como Matplotlib e Plotly.

**GitHub:** GitHub é uma plataforma de hospedagem de código-fonte baseada em Git, que oferece controle de versão e colaboração. Ele permite que múltiplos desenvolvedores trabalhem em projetos de forma simultânea e organizada, facilitando o gerenciamento de versões de código, a revisão de código e a integração contínua.

**Características Principais do GitHub:**
- **Controle de Versão:** Facilita o acompanhamento de mudanças e a colaboração em código.
- **Integração com CI/CD:** Oferece GitHub Actions para configurar pipelines de integração e entrega contínua.
- **Colaboração:** Permite a colaboração eficiente entre desenvolvedores através de pull requests e revisões de código.

**Integração Streamlit e GitHub:** A combinação de Streamlit e GitHub oferece uma poderosa ferramenta para o desenvolvimento e deploy de aplicações. O código pode ser versionado e colaborado no GitHub, enquanto o Streamlit pode ser usado para criar a interface do usuário e hospedar a aplicação de maneira simples e eficaz. A integração com GitHub Actions permite a automação do deploy, garantindo que as atualizações sejam aplicadas de forma rápida e sem interrupções significativas.

---

### 2. Preparação do Ambiente de Desenvolvimento

**2.1 Descrição dos Requisitos para Iniciar um Projeto com Streamlit**

Para iniciar um projeto com Streamlit, é essencial atender a alguns requisitos básicos que garantem um ambiente de desenvolvimento adequado e eficiente. Aqui estão os requisitos principais:
1. **Hardware:** Computador com capacidade razoável de processamento e memória RAM (mínimo 4GB recomendável). Conexão à internet estável para baixar pacotes e dependências.
2. **Sistema Operacional:** Streamlit é compatível com Windows, macOS e Linux. Certifique-se de que o sistema operacional está atualizado.
3. **Python:** Streamlit requer o Python 3.6 ou superior. Verifique a versão do Python instalada no seu sistema:
     ```bash
     python --version
     ```
4. **Gerenciador de Pacotes:** Utilize o `pip`, que geralmente vem pré-instalado com o Python, para instalar pacotes necessários.
     ```bash
     pip --version
     ```
5. **Editor de Código/IDE:** Use um editor de código ou IDE de sua preferência, como Visual Studio Code, PyCharm ou Jupyter Notebook.

**2.2 Explicação sobre a Criação do Ambiente Local, Incluindo a Instalação do Streamlit e Outras Dependências Necessárias**

Para preparar o ambiente de desenvolvimento local para um projeto com Streamlit, siga os passos abaixo:

1. **Instalação do Python:** Se o Python ainda não estiver instalado, faça o download e instale a versão mais recente do [site oficial do Python](https://www.python.org/downloads/).
2. **Criação de um Ambiente Virtual:** Crie um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outras instalações de pacotes.
     ```bash
     python -m venv nome_do_ambiente
     ```
   - Ative o ambiente virtual:
     - No Windows:
       ```bash
       nome_do_ambiente\Scripts\activate
       ```
     - No macOS/Linux:
       ```bash
       source nome_do_ambiente/bin/activate
       ```
3. **Instalação do Streamlit:** Com o ambiente virtual ativo, instale o Streamlit utilizando o `pip`:
     ```bash
     pip install streamlit
     ```
4. **Criação do Projeto Streamlit:** Crie um diretório para o seu projeto e navegue até ele:
     ```bash
     mkdir meu_projeto_streamlit
     cd meu_projeto_streamlit
     ```
5. **Arquivo requirements.txt:** Crie um arquivo `requirements.txt` para listar todas as dependências do projeto. Isso facilita a instalação de dependências em outros ambientes.
     ```txt
     streamlit
     ```
6. **Instalação de Outras Dependências:** Se seu projeto depende de outras bibliotecas (por exemplo, pandas, numpy, scikit-learn), adicione-as ao `requirements.txt` e instale-as:
     ```bash
     pip install -r requirements.txt
     ```
7. **Criação do Script Principal do Streamlit:** Crie um arquivo Python principal, por exemplo, `app.py`, onde você irá escrever o código do Streamlit:
     ```python
     import streamlit as st

     st.title("Meu Primeiro Aplicativo Streamlit")
     st.write("Olá, mundo!")
     ```
8. **Execução do Aplicativo Streamlit:** Execute seu aplicativo Streamlit para verificar se tudo está funcionando corretamente:
     ```bash
     streamlit run app.py
     ```

---

### 3. Configuração do GitHub

**3.1 Passo a Passo para Criar um Repositório no GitHub**

Criar um repositório no GitHub é um processo simples e direto. Aqui está um guia passo a passo para ajudá-lo a começar:

1. **Criação de uma Conta no GitHub:** Se você ainda não tem uma conta no GitHub, vá até [GitHub.com](https://github.com) e crie uma conta gratuita.
2. **Login no GitHub:** Faça login na sua conta do GitHub.
3. **Criar um Novo Repositório:** Na página inicial do GitHub, clique no ícone de `+` no canto superior direito e selecione `New repository`.
4. **Configurar o Repositório:** 
   - **Nome do Repositório:** Dê um nome ao seu repositório (por exemplo, `meu_projeto_streamlit`
