from collections import Counter

strings = [
    "zolushnbcroverbqsouslyattbwsirfpodbjhpbzjzemhgonjjhvjxvocciqsbfbezpjbbaoeksfuhinwythrhdoqmpjntqyiuea",
    "pmwiudkifsjxcdtdxfnjqswlfrwfxgmwueiffapkthyckvnoiwybptbaejhefagyrqrfjarjiectvnwuhiqcgbhtmvxhvmsmourc",
]


vertical = []

for i in range(len(strings[0])):
    word = ""
    for j in range(len(strings)):
        word += strings[j][i]

    vertical.append(word)


# print(vertical)
print(Counter(vertical))


# 4


"""
cihogwjpsgthtqntmoruioowuvjifcgcfbghyvqayokwatecdgmcojhcmiltgtxbzodgydchhbwtbxevfzyqorietdnusnmjtyqg
rggnirtfburuxosnvqpjoqppnljwossnvtcfoyzirkisidaiiqvgzacugingxbxsubvzayrgfmitufmeqwwzyktjiwwpfclhldpv
zolushnbcroverbqsouslyattbwsirfpodbjhpbzjzemhgonjjhvjxvocciqsbfbezpjbbaoeksfuhinwythrhdoqmpjntqyiuea
pmwiudkifsjxcdtdxfnjqswlfrwfxgmwueiffapkthyckvnoiwybptbaejhefagyrqrfjarjiectvnwuhiqcgbhtmvxhvmsmourc

"""
