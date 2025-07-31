from vncorenlp import VnCoreNLP
from typing import List, Tuple, Dict

# Change POS tag to a universal format
POS_MAP = {
    'Np':  'PROPN',  # Danh từ riêng (tên người, địa danh)
    'Nc':  'NOUN',   # Danh từ chỉ loại (cái, con, chiếc, ...)
    'Nu':  'NOUN',   # Danh từ đơn vị (lít, mét, người, ...)
    'N':   'NOUN',   # Danh từ thường

    'Ny':  'NOUN',   # Danh từ viết tắt
    'Nb':  'NOUN',   # Danh từ mượn (ngoại lai)

    'V':   'VERB',   # Động từ
    'Vb':  'VERB',   # Động từ mượn (ngoại lai)

    'A':   'ADJ',    # Tính từ
    'P':   'PRON',   # Đại từ (tôi, bạn, chúng tôi, ...)
    'R':   'ADV',    # Trạng từ (nhanh, rất, cũng, ...)
    'L':   'DET',    # Từ hạn định (những, các, một, ...)

    'M':   'NUM',    # Số từ / từ chỉ lượng
    'E':   'ADP',    # Giới từ (ở, từ, với, tại, ...)

    'C':   'SCONJ',  # Liên từ phụ thuộc (rằng, nếu, khi, ...)
    'Cc':  'CCONJ',  # Liên từ đẳng lập (và, hoặc, nhưng, ...)

    'I':   'INTJ',   # Thán từ (ôi, ồ, ái, chà, ...)
    'T':   'PART',   # Trợ từ, tình thái (đã, rồi, mà, nhé, ...)
    'Y':   'SYM',    # Ký hiệu (%, $, &, ...)
    'Z':   'X',      # Hình vị phụ thuộc (phụ tố: chẳng, chả...)

    'X':   'X',      # Không phân loại / từ đặc biệt
    'CH':  'PUNCT'   # Dấu câu (., ,, !, ?)
}

# Change dependency labels to a more descriptive format
DEP_LABEL_MAP = {
    'adv':   'Adverbial',                # Trạng ngữ
    'amod':  'Adjective modifier',       # Bổ nghĩa tính từ
    'conj':  'Conjunction',              # Liên từ
    'coord': 'Coordination',             # Từ điều phối, từ nối song song
    'dep':   'Default label',            # Nhãn phụ thuộc mặc định (không rõ)
    'det':   'Determiner',               # Từ hạn định (những, các, một, ...)
    'dir':   'Direction',                # Hướng (ra, vào, lên, xuống, ...)
    'dob':   'Direct object',            # Tân ngữ trực tiếp
    'iob':   'Indirect object',          # Tân ngữ gián tiếp
    'loc':   'Location',                 # Chỉ nơi chốn
    'mnr':   'Manner',                   # Cách thức (nhanh, từ tốn...)
    'nmod':  'Noun modifier',            # Bổ ngữ cho danh từ (tính từ, cụm giới từ, ...)
    'pmod':  'Prepositional modifier',   # Bổ ngữ của giới từ
    'pob':   'Object of a preposition',  # Tân ngữ của giới từ
    'prd':   'Predicate',                # Vị ngữ
    'prp':   'Purpose',                  # Mục đích (để làm gì)
    'punct': 'Punctuation',              # Dấu câu
    'root':  'Root',                     # Động từ chính của câu
    'sub':   'Subject',                  # Chủ ngữ
    'tmp':   'Temporal',                 # Trạng ngữ thời gian
    'vmod':  'Verb modifier'             # Bổ nghĩa động từ (thường là trạng từ)
}


class VnCoreannotator:
    _instance = None

    def __new__(cls):
        # Singleton pattern to ensure only one instance of VnCoreannotator
        if not cls._instance:
            cls._instance = super(VnCoreannotator, cls).__new__(cls)
            cls._instance.annotator = VnCoreNLP(
                r'VnCoreNLP-1.1.1.jar',
                annotators="wseg,pos,parse",
                max_heap_size='-Xmx2g'
            )
        return cls._instance

    def annotate(self, text) -> List[Dict]:
        # Annotate the text and return the parsed result
        result = self.annotator.annotate(text)
        return result['sentences'][0]
    
    def printPOS(self, text):
        # Print the POS tags and dependency labels for debugging
        tag_result = self.annotate(text)
        print("-" * 45)
        print("VNCoreNLP Tokenization and POS Tagging Result:")
        print("Original sentece: ", text)
        print("{:<15} {:<10} {:<10}".format("Token", "POS", "Parsed"))
        print("-" * 40)
        for token in tag_result:
            print("{:<15} {:<10} {:<10}".format(token['form'], POS_MAP[token['posTag']], DEP_LABEL_MAP[token['depLabel']]))


test_sentence = [
    "Tôi đang ăn cơm",
    "Tôi đã ăn bao nhiêu trái táo",
    "Cao Minh Quang đang đi học ở trường",
    "Hà Nội là thủ đô của nước nào",
    "Tôi đi học ở trường",
    "Mẹ nấu cơm ngon"
]

if __name__ == '__main__':
    annotator = VnCoreannotator()
    for sentence in test_sentence:
        print("-" * 45)
        print("Original sentence:", sentence)
        annotator.printPOS(sentence)
        print("-" * 45)