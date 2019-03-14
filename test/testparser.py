import parser

p = parser.Parser()

testMap = {
    "1": ["https://www.python.org", "python", 46, "Test 1 - Should be 46 but was "],
    "2": ["https://www.python.org", "the", 21, "Test 2 - Should be 21 but was "],
    "3": ["https://www.github.com", "git", 0, "Test 3 - Should be 0 but was "],
    "4": ["https://www.virtusize.com/site/", "the", 18, "Test 4 - Should be 18 but was "],
    "5": ["https://www.python.org/invalid", "huh", 0, "Test 5 - Should be 0 but was "],
}


def test_get_http():
    for key in testMap.keys():
        tc = testMap.get(key)
        url = tc[0]
        target = tc[1]
        expected = tc[2]
        errmsg = tc[3]
        result = p.parse(url, target)
        assert expected == result, (errmsg + str(result))


if __name__ == "__main__":
    test_get_http()
    print("Passed!")
