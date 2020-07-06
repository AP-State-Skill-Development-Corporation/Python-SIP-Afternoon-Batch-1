def topperName(fileName):
    """Find out the name of topper"""
    fh = open(fileName,'r')
    final = []
    for student in fh:
        details = student.split()
        name = details[0]
        marks = details[1:]
        marks = list(map(int,marks))
        final.append((sum(marks),name))
    final.sort(reverse=True)
    fh.close()
    return final[0][1]

def selectedStudents(fileName,percentageNumber):
    """give the selected names for given percentage"""
    # implement logic
    return 

