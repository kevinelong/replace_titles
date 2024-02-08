def replace_titles(text):
    #  TODO - Do the thing.
    return text


#TESTS
if __name__ == "__main__":
    def tst_replace_titles():
        results = replace_titles("""
This phrase talks about The Beauty and the Beast, and Cinderella, and also The Pastime Bar and Grill. 
    1. Obvious Title: Blach blah blah.
    2. Less - Obviously a good time
Take nothing at face-value.                       
""")
        print(results)
        expected ="""
This phrase talks about _The_Beauty_and_the_Beast, and _Cinderella_, and also _The_Pastime_Bar_and_Grill_. 
    1. _Obvious_Title_: Blach blah blah.
    2. _Less_ - Obviously a good time
Take nothing at face-value.                       
"""
        return(results==expected)
    print(tst_replace_titles())
