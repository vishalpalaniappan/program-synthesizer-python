from LoggingHelper import semanticLogger

def behavior1(book):
    semanticLogger.logPreParticipant(book)
    bookName = 'Harry Potter'
    book['name'] = 'Harry Potter'
    book['name'] = 'Harry Potter'
    semanticLogger.logPostParticipant(book)
    semanticLogger.logPostParticipant(bookName)

def behavior2(book):
    semanticLogger.logPreParticipant(book)
    sample = 1
    sample = 2 + 3
    semanticLogger.logPostParticipant(book)
    semanticLogger.logPostParticipant(sample)