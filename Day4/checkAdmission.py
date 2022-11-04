def checkAdmission(**studentMarks):
    if studentMarks['pcm'] == True:
        print('First quality matches')
        if studentMarks['phy'] >= 50 and studentMarks['chm'] >= 50 and studentMarks['math'] >=50:
            print('Yes you can')
            return True
        else:
            print('Sorry you cant take admission')
            return False
    else:
        print('PCM is not there so exit')
        return False
checkAdmission(pcm=True,phy=60,chm=70,math=80)