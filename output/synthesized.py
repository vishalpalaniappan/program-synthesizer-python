from LoggingHelper import semanticLogger

def behavior1(book):
    semanticLogger.logPreParticipant(book)
    bookName = 'Harry Potter'
    book['name'] = 'Harry Potter'
    semanticLogger.logPostParticipant(book)
    semanticLogger.logPostParticipant(bookName)

def behavior2(book):
    semanticLogger.logPreParticipant(book)
    sample = 'SAMPLE_STRING'
    semanticLogger.logPostParticipant(book)
    semanticLogger.logPostParticipant(sample)