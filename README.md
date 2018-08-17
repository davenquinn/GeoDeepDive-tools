# GeoDeepDive-tools

`GeoDeepDive-tools` is a Python module that assists with writing
code against the CoreNLP `sentences_nlp352`-formatted
data that are contained in the GeoDeepDive corpus.

## API

Currently, this toolkit contains a basic `Sentence` and `Word` API that allows
records to be manipulated in a "natural" manner. This assists with producing
code with a clear flow of logic.

Immediate future plans include a "phrase" construct, and potentially interfaces
to other tools.

## Installation

This code is in its early phases; as such, it is not explicitly versioned or
available on PyPI. However, the current `master` version can be easily installed
from this repository using

```
> pip install git+https://github.com/davenquinn/GeoDeepDive-tools.git
```

## Usage

```
from GDDTools import Sentence

# An object extracted from a row in the `sentences_nlp352` data table
obj = dict(
  index=0,
  words=['Hello',',','World','!'],
  lemmas=['hello',',','world','!'],
  poses=['UH',',','NN','.'],
  ners=['O','O','O','O'],
  dep_parent=[...]
  # `word_idx` array can be provided but is not used (it is redundant)
)

sentence = Sentence(obj)
print(sentence) # -> "Hello, world!"

sentence.word[0].is_noun # -> False

```

## Contributing

Contributions in the form of raised issues and pull requests are welcomed. Let
me know if you're using this tool in your code!
