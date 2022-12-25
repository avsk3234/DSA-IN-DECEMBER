class TrieNode:	
	# Trie node class
	def __init__(self):
		self.children = [None for _ in range(26)]
		# isEndOfWord is True if node represent the end of the word
		self.isEndOfWord = False
