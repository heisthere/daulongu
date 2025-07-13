import re


class ArticleDecomposer:
    def __init__(self, article):
        self.sentences = self.decompose(article)

    def decompose (article):
        sentence_endings = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s?')
        sentences = sentence_endings.split(article)
        return [s.strip() for s in sentences if s.strip()]

if __name__ == '__main__':
    print(ArticleDecomposer.decompose("This is a test. Some, more. Some more more! Yes? End."))

