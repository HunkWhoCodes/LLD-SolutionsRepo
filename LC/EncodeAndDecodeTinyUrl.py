# https://leetcode.com/problems/encode-and-decode-tinyurl/
# Difficulty: Medium

# This is unoptimized solution that uses a counter to generate the short code for URLs,
# TODO - Implement a better method

class Codec:
    
    def __init__(self):
        self.mapping = {}
        self.counter = 0
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.counter += 1
        shortUrl = self.base_url + str(self.counter)
        self.mapping[shortUrl] = longUrl
        return shortUrl
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.mapping[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
