

dictionary = \
    {
        1 : "A, E, I, O, U, L, N, S, T, R" ,
        2 : "D, G",
        3 : "B, C, M, P",
        4 : "F, H, V, W, Y",
        5 : "K", 
        8 : "J, X", 
        10 : "Q, Z",   
        1 : "А, В, Е, И, Н, О, Р, С, Т", 
        2 : "Д, К, Л, М, П, У",
        3 : "Б, Г, Ё, Ь, Я", 
        4 : "Й, Ы",
        5 : "Ж, З, Х, Ц, Ч",
        8 : "Ш, Э, Ю", 
        10 : "Ф, Щ, Ъ"
    }

text = str(input())

Summa = 0

for i in text:
    for k, v in dictionary.items():
        if i in v:
            Summa += k
print (Summa)



