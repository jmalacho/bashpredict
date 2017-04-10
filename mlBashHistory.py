import nltk
import shlex

def fileGen(path="/root/.bash_history"):
    for line in open(path):
        yield( line.strip() )


def keyByMaxValue( dct ):
  maxValue=0
  for key,value in dct.iteritems():
    if value > maxValue:
      maxKey=key
      maxValue=value
  return maxKey
##############################################################################        
class ModelPredict:
  def __init__(self):
    self.data={}
    self.model={}
    self.order=2
    self.rps="</s>"
  def chooseCorpus(self,path=""):
    self.lineList=fileGen("/root/.bash_history")

  def addNgramsFromChoice( self ):
    if self.lineList:
      for line in self.lineList:
        try:
          lexical_split=shlex.split( line )
        except ValueError:
          lexical_split=False
        if lexical_split:      
          ngrams = nltk.ngrams( lexical_split, 2, pad_left=True, pad_right=True, left_pad_symbol="<s>", right_pad_symbol=self.rps)
          for ngram in ngrams:
            self.addNgram( ngram)

  def addNgramsFromString( self, s ):
    try:
      lexical_split=shlex.split( s )
    except ValueError:
      lexical_split=False
    if lexical_split:
      ngrams = nltk.ngrams( lexical_split, 2, pad_left=True, pad_right=True, left_pad_symbol="<s>", right_pad_symbol=self.rps )
      for ngram in ngrams:
        self.addNgram( ngram )

  def addNgram(self, ngram):
    key1 = ngram[0:self.order-1]          #leading word, as tuples
    key2 = ngram[self.order-1:self.order][0]  #final/predicted word, as string
    if key2==self.rps:
      return False

    counterHash = self.data.get( key1, {} )
    count       = counterHash.get( key2, 0 )

    counterHash[key2] = count+1
    self.data[ key1 ]  = counterHash    


  def calcModel(self):
    for key, counterDict in self.data.iteritems():
      self.model[key]=keyByMaxValue( counterDict )

  def update(self):
    self.calcModel()
    return "success"
  
  def predict(self, word):
    t=type(word)
    if t==str:
       key=(word,)
    elif t==tuple:
       key=word
    else:
       raise TypeError, "predict requires a str or a tuple. Got %s" % v
    return self.model.get(key, self.rps)
  
  def status( self ):
    return len( self.data )

  def __str__(self):
    return self.model.__str__()

#for line in lineList:
#  ngrams = nltk.ngrams( shlex.split( line ), 2, pad_left=True, pad_right=True, left_pad_symbol="<s>", right_pad_symbol="</s>")
#  m.addNgramsFromGen( ngrams )

#print m


