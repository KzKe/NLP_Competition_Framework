import transformers


MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10

# RoBERTa-wwm-ext-large	hfl/chinese-roberta-wwm-ext-large
# RoBERTa-wwm-ext	hfl/chinese-roberta-wwm-ext
# BERT-wwm-ext	hfl/chinese-bert-wwm-ext
# BERT_PATH = "hfl/chinese-bert-wwm-ext"
# BERT_PATH = "hfl/chinese-roberta-wwm-ext"
# BERT_PATH = "hfl/chinese-roberta-wwm-ext-large"
BERT_PATH = "../input/bert_base_uncased/"
MODEL_PATH = "model.bin"
TRAINING_FILE = "../input/imdb.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH,
    do_lower_case=True
)