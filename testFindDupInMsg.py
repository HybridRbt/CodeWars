__author__ = 'JeredYang'

import findDupInMsg as fdi

def testDIM():
    # paragraph = 'This is a test. this test is fun.'
    # print fdi.find_secret_message(paragraph)
    paragraph = 'asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv asdf.'
    print fdi.find_secret_message(paragraph)

testDIM()