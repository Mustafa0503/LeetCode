class WordDictionary:

    def __init__(self, endOfWord: bool = False):
        self.children: dict = defaultdict(WordDictionary)
        self.endOfWord: bool = endOfWord
        

    def addWord(self, word: str) -> None:
        curr = self

        for char in word:
            curr = curr.children[char]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self

        for idx, char in enumerate(word):
            if char == ".":
                for child in curr.children.values():
                    if child.search(word[idx+1:]):
                        return True
            
            if char not in curr.children:
                return False
                
            curr = curr.children[char]

        return curr.endOfWord