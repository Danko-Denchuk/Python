import os
from pocketsphinx import LiveSpeech

speech = LiveSpeech(lm=False, keyphrase='rubber', kws_threshold=1e-20)

print('you said')

for phrase in speech:
    print(phrase.segments(detailed=True))
