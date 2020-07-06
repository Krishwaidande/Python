def displayList(listValue):
    output=''
    i=0

    for value in listValue:
        if (i != (len(listValue) - 1)):
            output+=str(value) + ', '
        else:
            output+='and ' + str(value)
        i+=1

    return output
    
def main():
    inpList=['apples', ['bananas',1], 'tofu', 'dog', 3.14, 'cats']
    print ('Actual List:')
    print(inpList)
    print(displayList(inpList))

main()
