greeting = "Hello world"

def replace(sourceStr, templateStr, newSubstr, findAll=False):

    if templateStr == newSubstr:
        return sourceStr

    sourceLength = len(sourceStr)
    templateLength = len(templateStr)

    i = 0

    while i < sourceLength:
        matches = False
        j = 0

        while j < templateLength:
            if sourceStr[i + j] == templateStr[j]:
                matches = True
            else:
                matches = False
                break
            j = j + 1

        if matches:
            firstPart = ''
            secondPart = ''

            k = 0

            while k < i:
                firstPart = firstPart + sourceStr[k]
                k = k + 1

            k = i + templateLength

            while k < sourceLength:
                secondPart = secondPart + sourceStr[k]
                k = k + 1

            sourceStr = firstPart + newSubstr + secondPart

            if findAll == False:
                break

        i = i + 1

    return sourceStr

print(replace("Hello world", "wo", "Wo", False))