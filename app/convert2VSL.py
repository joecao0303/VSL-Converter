from app.pos_tagger import *
from typing import List, Dict


class VietnameseToVSLConverter:
    def __init__(self):
        # Initialize the VnCoreNLP annotator
        self.parser = VnCoreannotator()
        # Load the ASK and NEG words from files
        ask_words_path = 'app/Data/ASK_WORDS.txt'
        neg_words_path = 'app/Data/NEG_WORDS.txt'
        with open(ask_words_path, 'r', encoding='utf-8') as f:
            self.ASK_WORDS = set(f.read().strip().split())
        with open(neg_words_path, 'r', encoding='utf-8') as f:
            self.NEG_WORDS = set(f.read().strip().split())


    # === STEP 1: Extract sentence structure ===
    def extract_structure(self, parsed_sentence: List[Dict]) -> Dict[str, List[str]]:
        # Initialize the structure dictionary
        structure = {
            'S': [], 'V': [], 'O': [], 'NUM': [], 'TIME': [], 'ASK': [], 'NEG': [], 'OTHER': []
        }
        # Iterate through the parsed tokens and classify them
        # based on their POS tags and dependency labels
        for token in parsed_sentence:
            word = token['form']
            pos = token['posTag']
            dep = token['depLabel']
            # Classify the word based on its POS and dependency label
            if word.lower() in self.ASK_WORDS:
                structure['ASK'].append(word) # Question words
            elif word.lower() in self.NEG_WORDS:
                structure['NEG'].append(word) # Negative words
            elif dep in {'tmp', 'loc'}:
                structure['TIME'].append(word) # Time/Location
            elif pos == 'M':
                structure['NUM'].append(word) # Numbers
            elif dep == 'sub':
                structure['S'].append(word) # Subject
            elif dep in {'root', 'vmod'}:
                structure['V'].append(word) # Verb (root or modifier)
            elif dep in {'obj', 'dob', 'iob', 'nmod'}:
                structure['O'].append(word) # Objects (direct, indirect, noun modifiers)
            else:
                structure['OTHER'].append(word) # Other words

        return structure

    # === STEP 2: Reorder structure to VSL order ===
    def reorder_to_vsl(self, structure: Dict[str, List[str]]) -> List[str]:
        gloss = []
        gloss.extend(structure['TIME'])
        gloss.extend(structure['S'])
        gloss.extend(structure['O'])
        gloss.extend(structure['NUM'])
        gloss.extend(structure['V'])
        gloss.extend(structure['OTHER'])
        gloss.extend(structure['ASK'])
        gloss.extend(structure['NEG'])

        return gloss

    # === STEP 3: Convert to gloss (uppercase) ===
    def to_gloss(self, vsl_tokens: List[str]) -> str:
        return ' '.join([token.upper() for token in vsl_tokens])

    # === Wrapper function ===
    def convert(self, text: str) -> str:
        self.parser.printPOS(text)  # Print POS tags for debugging
        parsed = self.parser.annotate(text)
        structure = self.extract_structure(parsed)
        reordered = self.reorder_to_vsl(structure)
        gloss = self.to_gloss(reordered)
        gloss = gloss.replace('_', ' ')
        return gloss

# === TEST ===
test_sentence = [
    "Tôi đang ăn cơm",
    "Tôi đã ăn bao nhiêu trái táo",
    "Cao Minh Quang đang đi học ở trường",
    "Bố không ăn trái cam",
    "Tôi đi học ở trường",
    "Mẹ nấu cơm ngon"
]

if __name__ == '__main__':
    converter = VietnameseToVSLConverter()
    for sentence in test_sentence:
        print("Original:", sentence)
        print("Gloss:", converter.convert(sentence))
        print("-")
