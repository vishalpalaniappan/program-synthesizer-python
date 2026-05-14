from LoggingHelper import semanticLogger

def behavior1():
    semanticLogger.logPreParticipant('book')
    bookName = 'Harry Potter'
    semanticLogger.logPostParticipant('book')
    semanticLogger.logPostParticipant('bookName')
    semanticLogger.logPostParticipant('name4')