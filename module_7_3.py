class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(char, ' ')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                result[name] = words.index(word.lower())
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word.lower())
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
