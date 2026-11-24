import random

# BANCO DE PALAVRAS #
palavras = [
    "Amigo", "Arroz", "Audio", "Balao", "Barco",
    "Blusa", "Bolsa", "Brisa", "Caixa", "Calor",
    "Canto", "Carro", "Carta", "Chave", "Chuva",
    "Cinza", "Clima", "Conta", "Corpo", "Dente",
    "Disco", "Festa", "Folha", "Força", "Fruta",
    "Fundo", "Gente", "Hotel", "Jovem", "Lapis",
    "Leite", "Livro", "Lugar", "Luzes", "Mente",
    "Mundo", "Navio", "Noite", "Nuvem", "Olhos",
    "Papel", "Pedra", "Peixe", "Pente", "Perna",
    "Piano", "Placa", "Plano", "Poder", "Porta",
    "Ponto", "Praia", "Prato", "Preço", "Preto",
    "Primo", "Pulso", "Quase", "Queda", "Radio",
    "Raiva", "Regra", "Reino", "Renda", "Resto",
    "Ritmo", "Rosto", "Roupa", "Sabao", "Sabor",
    "Saida", "Salto", "Saude", "Senha", "Serie",
    "Sinal", "Sitio", "Sonho", "Sorte", "Susto",
    "Tarde", "Tecla", "Tempo", "Terra", "Texto",
    "Tigre", "Tinta", "Toque", "Torre", "Troca",
    "Turma", "Uniao", "Vento", "Verde", "Verao",
    "Vidro", "Vinho", "Visao", "Vozes", "Zebra"
    ]

# PALAVRA ESCOLHIDA PELO COMPUTADOR #
palavra_escolhida = random.choice(palavras)

# TENTATIVAS MÁXIMAS #
tentativas = 6

print("-=-" *15)

largura = os.get_terminal_size().columns

texto = "TERMO EM PYTHON"
print(texto.center(largura))
print("-=-" *15)



