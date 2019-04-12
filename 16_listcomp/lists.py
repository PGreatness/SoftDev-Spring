def passCheck(s=''):
    UC_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
    LC_LETTERS = "qwertyuiopasdfghjklzxcvbnm"
    NUMBERS = "1234567890"
    SPECIAL = "!@#$%^&*()_-+=<>?/;:\'\"\\|[]}{`~ "
    upper = [ 1 for x in s if x in UC_LETTERS ]
    lower = [ 1 for x in s if x in LC_LETTERS ]
    nums = [ 1 for x in s if x in NUMBERS ]
    spec = [ 1 for x in s if x in SPECIAL ]
    errLog = []
    if ' ' in s:
        errLog.append(f"Invalid character, cannot contain spaces")
    if len(upper) == 0:
        errLog.append(f"Too few upper case characters, found {len(upper)}")
    if len(lower) == 0:
        errLog.append(f"Too few lower case characters, found {len(lower)}")
    if len(spec) == 0:
        errLog.append(f"Too few special characters, found {len(spec)}")
    if len(nums) == 0:
        errLog.append(f"Too few numbers, found {len(nums)}")
    if len(errLog) > 0:
        for item in errLog:
            print('ERR:' + item + '\n')
        return -1
    score = 1 if len(s) <= 3 else 3 if len(s) <= 5 else 5 if len(s) <= 7 else 8 if len(s) <= 8 else 10
    result = f"Your password: {s} has recieved a score of: {score}\n"
    print(result)
    return score

passCheck('')
passCheck('123456789')
passCheck('qwertyuioplkjhgfdewazxcvbnm,')
passCheck('QWERTYUIKJHGVCDX')
passCheck('qazxswedcWERFDCX')
passCheck('!@#$%^&*()_')
passCheck('aNoobPassword1234!@')
passCheck('qazWSD123~!')
passCheck('qA`1 ')