# FUNCTION SECTION ------------------------------

class TextProcessor:
    
    # Initial variables held for set up ---
   
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding
        self.text = self._read_file()

    # File reading and editor --
    def _read_file(self):
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            return file.read()

    # Single item return functions-

    def view_window(self, start_index, window_size):
        end_index = min(start_index + window_size, len(self.text))
        return self.text[start_index:end_index]

    def remove_window(self, text, start_index, window_size):
        end_index = min(start_index + window_size, len(text))
        new_text = text[:start_index] + text[end_index:]
        return new_text

    # Compounded functions ---

    def view_whole(self):
        return self.text

    def recurring_windows(self, window_size, pattern_interval):
        windows = []
        for i in range(0, len(self.text) - window_size + 1, pattern_interval):
            window_text = self.text[i:i+window_size]
            windows.append(window_text)
        return windows

    def remove_windows(self, indices, window_size):
        new_text = self.text
        removed_chars = 0  # Track the total number of characters removed
        for index in indices:
            index -= removed_chars  # Adjust the index to account for removed characters
            end_index = min(index + window_size, len(new_text))
            new_text = new_text[:index] + new_text[end_index:]
            removed_chars += window_size  # Increment removed_chars by the size of the removed window
        return new_text

    def remove_recurring_windows(self, pattern_interval, window_size):
        new_text = self.remove_windows(self.pattern_index(pattern_interval),window_size)
        return new_text

    def remove_strings(self, word):
        new_text = self.remove_windows(self.search_word(word,"array"),len(word))
        return new_text


    # Index builder

    def pattern_index(self, pattern_interval):
        indices = [i for i in range(0, len(self.text), pattern_interval)]
        return indices

    # Character selectors
    
    def count_words(self):
        words = self.text.split()
        return len(words)

    def count_characters(self):
        return len(self.text)

    def search_word(self, word, return_format):
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

# DEBUG SECTION ---------------------------------

file_path = 'PiEx.txt'  # Path to your text file

text_processor = TextProcessor(file_path)

# Get a window of text
window_text = text_processor.view_window(start_index=0, window_size=350)
print("Window of text:",window_text)
print("Length of window of text:",len(window_text))

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
#search_result = text_processor.search_word("3.141592653589793238", return_format='string')
#print("\nSearch result for 'pi chunk':", search_result)

# Delete all of a word in the text
#search_remove = text_processor.remove_strings("3.141592653589793238")
#print("\nSearch result for 'pi chunk':", search_remove)

# Get windows with recurring pattern
#windows_with_pattern = text_processor.recurring_windows(pattern_interval=50, window_size=20)
#print("\nWindows given pattern:", windows_with_pattern)

# Observe pattern index
interval = 20
window_size = 1
pattern_indexes = text_processor.pattern_index(interval)
print("\nObserved pattern indexes:",pattern_indexes)

# Get windows with recurring pattern
windows_without_pattern = text_processor.remove_recurring_windows(interval, window_size)
print("\nText without windows:", windows_without_pattern)
print("\nLength of new text", len(windows_without_pattern))
print("\nExpected difference:", len(pattern_indexes)*window_size)
print("\nActual difference:", len(text_processor.view_whole())-len(windows_without_pattern))

