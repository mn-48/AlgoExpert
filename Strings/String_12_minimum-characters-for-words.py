# O(n*l)  Time | O(c) Space
def minimumCharactersForWords(words):
    # একটি অক্ষর গণনার জন্য ডিকশনারি তৈরি করুন
    character_count = {}
    
    # প্রতিটি শব্দের জন্য
    for word in words:
        # শব্দের প্রতিটি অক্ষর গণনা করুন
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1
            # সর্বোচ্চ গণনা আপডেট করুন
            character_count[char] = max(character_count.get(char, 0), word_count[char])
    
    # ফলাফল অ্যারে তৈরি করুন
    result = []
    for char, count in character_count.items():
        for _ in range(count):
            result.append(char)
    
    return result