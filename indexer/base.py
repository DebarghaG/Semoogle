import sparknlp
from sparknlp.base import *
from sparknlp.annotator import *
from sparknlp.pretrained import PretrainedPipeline
from sparknlp.base import *
from sparknlp.annotator import *
from sparknlp.common import *
from sparknlp.embeddings import *
import sparknlp

# Start Spark Session with Spark NLP
spark = sparknlp.start()
print(spark.version)


data = [
  ("New York is the greatest city in the world", 0),
  ("The beauty of Paris is vast", 1),
  ("The Centre Pompidou is in Paris", 1)
]

df = spark.createDataFrame(data, ["text","label"])

document_assembler = DocumentAssembler().setInputCol("text").setOutputCol("document")

tokenizer = Tokenizer().setInputCols(["document"])\
  .setOutputCol("token")

word_embeddings = BertEmbeddings.pretrained('bert_base_cased', 'en')\
  .setInputCols(["document", "token"])\
  .setOutputCol("embeddings")


bert_pipeline = Pipeline().setStages(
  [
    document_assembler,
    tokenizer,
    word_embeddings
  ]
)

df_bert = bert_pipeline.fit(df).transform(df)
display(df_bert)
# Download a pre-trained pipeline
#pipeline = PretrainedPipeline('explain_document_dl', lang='en')

# Annotate your testing dataset
#result = pipeline.annotate("The Mona Lisa is a 16th century oil painting created by Leonardo. It's held at the Louvre in Paris.")

# What's in the pipeline
#print(list(result.keys()))
#Output: ['entities', 'stem', 'checked', 'lemma', 'document', 'pos', 'token', 'ner', 'embeddings', 'sentence']

# Check the results
#print(result['entities'])
#Output: ['Mona Lisa', 'Leonardo', 'Louvre', 'Paris']
