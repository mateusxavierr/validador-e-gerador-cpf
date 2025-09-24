# CPF Generator & Validator

Este é um script em **Python** que permite **gerar CPFs válidos aleatórios** ou **validar CPFs existentes**, utilizando o algoritmo oficial de cálculo dos dígitos verificadores.  

## 🚀 Funcionalidades
- Gerar um CPF válido aleatório.  
- Validar um CPF informado pelo usuário.  
- Remoção automática de pontos, traços e espaços da entrada.  
- Retorno indicando se o CPF é **válido** ou **inválido**.  

## 📌 Como funciona
1. O usuário pode **digitar um CPF** (com ou sem formatação) ou **pressionar Enter** para gerar um novo automaticamente.  
2. O programa calcula os dois dígitos verificadores usando o algoritmo oficial (módulo 11).  
3. O CPF é exibido junto com o resultado da validação.  

### Exemplo de uso
```
Digite um CPF ou pressione enter para gerar um aleatório: 123.456.789-09
0 e 9 - CPF inválido: 12345678909
```

Gerando automaticamente:
```
Digite um CPF ou pressione enter para gerar um aleatório: 
1 e 4 - CPF válido: 12345678914
```

## 🛠️ Tecnologias
- [Python 3](https://www.python.org/)  
- Módulo `random` para geração de números aleatórios.  

## 📂 Estrutura
```
cpf_generator.py   # Script principal
```

## ▶️ Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/cpf_generator.git
   ```
2. Acesse a pasta:
   ```bash
   cd cpf_generator
   ```
3. Execute o script:
   ```bash
   python3 cpf_generator.py
   ```

## 📄 Licença
Este projeto é de uso livre para estudos e práticas com Python.  
