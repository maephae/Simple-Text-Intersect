class TextProcessor:
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding
        self.text = self._read_file()

    def _read_file(self):
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            return file.read()

    def get_window_of_text(self, start_index, window_size):
        end_index = min(start_index + window_size, len(self.text))
        return self.text[start_index:end_index]

    def delete_window_of_text(self, start_index, window_size):
        end_index = min(start_index + window_size, len(self.text))
        new_text = self.text[:start_index] + self.text[end_index:]
        return new_text

    def remove_pattern(self, pattern_interval):
        new_text = ''.join([self.text[i] for i in range(len(self.text)) if (i + 1) % pattern_interval != 0])
        return new_text

    def recurring_windows(self, window_size, pattern_interval):
        windows = []
        for i in range(0, len(self.text) - window_size + 1, pattern_interval):
            window_text = self.text[i:i+window_size]
            windows.append(window_text)
        return windows

    def count_words(self):
        words = self.text.split()
        return len(words)

    def count_characters(self):
        return len(self.text)

    def search_word(self, word):
        return word in self.text

# Example usage:
file_path = 'PiEx.txt'  # Path to your text file

text_processor = TextProcessor(file_path)

# Get a window of text
#window_text = text_processor.get_window_of_text(start_index=0, window_size=1950)
#print("Window of text:")
#print(window_text)

# Delete a window of text
#new_text = text_processor.delete_window_of_text(start_index=50, window_size=100)
#print("\nText after deleting window:")
#print(new_text)

# Count words in the text
#word_count = text_processor.count_words()
#print("\nWord count:", word_count)

# Search for a word in the text
#search_result = text_processor.search_word("python")
#print("\nSearch result for 'python':", search_result)

# Get windows with recurring pattern
#windows_with_pattern = text_processor.recurring_windows(window_size=2000, pattern_interval=2000)
#print("\nWindows with recurring pattern:", windows_with_pattern)

    
