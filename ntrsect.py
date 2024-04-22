class TextProcessor:
   
   
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding
        self.text = self._read_file()

    def _read_file(self):
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            return file.read()

    def view_window(self, start_index, window_size):
        end_index = min(start_index + window_size, len(self.text))
        return self.text[start_index:end_index]

    def remove_window(self, start_index, window_size):
        end_index = min(start_index + window_size, len(self.text))
        new_text = self.text[:start_index] + self.text[end_index:]
        return new_text

    def recurring_pattern(self, pattern_interval):
        selected_text = [self.text[i] for i in range(len(self.text)) if i % pattern_interval == 0]
        return selected_text

    def remove_pattern(self, pattern_interval):
        new_text = ''.join([self.text[i] for i in range(len(self.text)) if (i + 1) % pattern_interval != 0])
        return new_text

    def recurring_windows(self, window_size, pattern_interval):
        windows = []
        for i in range(0, len(self.text) - window_size + 1, pattern_interval):
            window_text = self.text[i:i+window_size]
            windows.append(window_text)
        return windows

    def remove_recurring_windows(self, indices, window_size):
        new_text = self.text
        for index in indices:
            new_text = self.remove_window(index, window_size)
        return new_text

    # Character selectors
    
    def count_words(self):
        words = self.text.split()
        return len(words)

    def count_characters(self):
        return len(self.text)

    def search_word(self, word, return_format='string'):
        indices = [i for i in range(len(self.text)) if self.text.startswith(word, i)]
        if not indices:
            return False
        if return_format == 'array':
            return indices
        elif return_format == 'string':
            result = "\n".join([f"Instance {i+1}: Index ({idx})" for i, idx in enumerate(indices)])
            return result
        else:
            return "Invalid return format"

# Example usage:
file_path = 'PiEx.txt'  # Path to your text file

text_processor = TextProcessor(file_path)

# Get a window of text
window_text = text_processor.view_window(start_index=0, window_size=350)
print("Window of text:")
print(window_text)

# Delete a window of text
#new_text = text_processor.remove_window(start_index=50, window_size=100)
#print("\nText after deleting window:")
#print(new_text)

# Count words in the text
#word_count = text_processor.count_words()
#print("\nWord count:", word_count)

#Count characters in the text
#char_count = text_processor.count_characters()
#print("Character count:", char_count)

# Search for a word in the text
#search_result = text_processor.search_string("111")
#print("\nSearch result for 'pi chunk':", search_result)

# Search for a word in the text
#search_result = text_processor.search_string("111")
#print("\nSearch result for 'pi chunk':", search_result)

# Get windows with recurring pattern
#windows_with_pattern = text_processor.recurring_windows(pattern_interval=50, window_size=20)
#print("\nWindows given pattern:", windows_with_pattern)

# Get windows with recurring pattern
windows_with_pattern = text_processor.remove_recurring_windows(pattern_interval=50, window_size=20)
print("\nText without windows:", windows_with_pattern)


