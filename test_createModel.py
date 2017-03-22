#try:
import mlBashHistory
#except:
#     import mlBashHistory

def test_createModel():
  m=mlBashHistory.ModelPredict()
  m.chooseCorpus("/root/.bash_history")
  m.addNgramsFromChoice()
  m.calcModel()
  return m

def test_predict():
  m=test_createModel()
  print m
  print " Testing predictions"
  print "- cat " + m.predict("cat")
  print "- vim " + m.predict("vim")
  print "- pytest " + m.predict("pytest")

