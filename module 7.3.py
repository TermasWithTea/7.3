import string


class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = list(file_name)

    def get_all_words(self):
        all_word = {}
        punctuation = string.punctuation.replace('-', '')
        for file_name in self.file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower().translate(str.maketrans('', '', punctuation))
                    words.extend(line.split())
                all_word[file.name] = words
        return all_word

    def find(self,word):
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    def count(self,word):
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
