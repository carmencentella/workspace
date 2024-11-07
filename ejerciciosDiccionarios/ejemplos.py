vocales = 'aeiou'
enum_vocales = {}

for i, vocal in enumerate(vocales, start=1):
    enum_vocales[vocal] = i
print(f'{enum_vocales}')