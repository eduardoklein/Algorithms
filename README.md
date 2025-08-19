# Project Algorithms

Este projeto contém desafios de algoritmos desenvolvidos durante o curso da Trybe. O objetivo é implementar e testar funções para problemas clássicos de lógica e manipulação de dados.

## Estrutura do Projeto

```
challenges/
    challenge_anagrams.py
    challenge_encrypt_message.py
    challenge_find_the_duplicate.py
    challenge_palindromes_iterative.py
    challenge_palindromes_recursive.py
    challenge_study_schedule.py
tests/
    __init__.py
    complexities.py
    generators.py
    encrypt/
        __init__.py
        test_encrypt.py
```

## Instalação

1. Clone o repositório:
   ```sh
   git clone <url-do-repositório>
   cd Algorithms
   ```
2. Instale as dependências:
   ```sh
   pip install -r dev-requirements.txt
   ```

## Como executar os testes

Execute os testes com o pytest:

```sh
pytest
```

## Descrição dos desafios

- **challenge_anagrams.py**: Verifica se duas palavras são anagramas.
- **challenge_encrypt_message.py**: Implementa uma função para criptografar mensagens com base em uma chave.
- **challenge_find_the_duplicate.py**: Encontra elementos duplicados em uma lista de inteiros.
- **challenge_palindromes_iterative.py**: Verifica se uma palavra é palíndromo (iterativo).
- **challenge_palindromes_recursive.py**: Verifica se uma palavra é palíndromo (recursivo).
- **challenge_study_schedule.py**: Calcula quantas pessoas estavam presentes em um determinado horário.

## Autoria dos arquivos

- **Desenvolvidos por mim**:

  - challenges/challenge_anagrams.py
  - challenges/challenge_encrypt_message.py
  - challenges/challenge_find_the_duplicate.py
  - challenges/challenge_palindromes_iterative.py
  - challenges/challenge_palindromes_recursive.py
  - challenges/challenge_study_schedule.py

- **Desenvolvidos pela Trybe**:

  - tests/complexities.py
  - tests/generators.py

- **Arquivos de configuração e outros**:
  - README.md
  - .gitignore
  - requirements.txt
  - dev-requirements.txt
  - setup.py
  - setup.cfg
  - pyproject.toml

Este projeto foi desenvolvido como parte do curso da Trybe.
