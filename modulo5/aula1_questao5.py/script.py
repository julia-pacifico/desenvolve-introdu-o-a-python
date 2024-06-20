import emoji
lista={
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":smile:": "😄",
    ":angry:": "😠"
}
print("lista de emojis:")
for codigo, emoticon in lista.items():
    print(f"{codigo}{emoticon}")
frase=input("digite uma frase e ela será emojizada:")

frase_d= emoji.emojize(frase)
print("frase emojizada:")
print(frase_d)