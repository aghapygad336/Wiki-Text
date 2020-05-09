from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]

import aaa

documents = []
for i in aaa.read("temp"):
    documents.append(TaggedDocument(i[0],i[1]))
    print("here")
print(documents[2])
model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)


fname = get_tmpfile("test.model")

model.save(fname)
model = Doc2Vec.load(fname)

vector = model.infer_vector(["system", "response"])
tokens = ["system", "response"]
print(model.docvecs.index_to_doctag(0))
new_vector = model.infer_vector(tokens)
sims = model.docvecs.most_similar([new_vector])
print(sims)
from gensim.test.utils import common_corpus, common_dictionary
from gensim.similarities import MatrixSimilarity
query = [(1, 2), (5, 4)]
index = MatrixSimilarity(common_corpus, num_features=len(common_dictionary))
sims = index[query]
print(index)
print(sims)