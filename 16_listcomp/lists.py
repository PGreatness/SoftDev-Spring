UC_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
LC_LETTERS = "qwertyuiopasdfghjklzxcvbnm"
NUMBERS = "1234567890"
SPECIAL = ".?!&#,;:-_*"

def minCheck(s=''):
    upper = [ 1 for x in s if x in UC_LETTERS ] # returns list of 1s for every uppercase letter in s
    lower = [ 1 for x in s if x in LC_LETTERS ] # returns list of 1s for every lowercase letter in s
    nums = [ 1 for x in s if x in NUMBERS ] # returns list of 1s for every number in s
    errLog = [] # errors
    if len(upper) == 0:
        errLog.append(f"Too few upper case characters in {s}, found {len(upper)}")
    if len(lower) == 0:
        errLog.append(f"Too few lower case characters in {s}, found {len(lower)}")
    if len(nums) == 0:
        errLog.append(f"Too few numbers in {s}, found {len(nums)}")
    if len(errLog) > 0:
        for item in errLog:
            i = errLog.index(item) + 1 # distinguish between errs with other passwords
            print(f'ERR {i}: {item}\n')
        return -1 # failure
    print(f"Your password {s} fits the minimum threshold\n")
    return 1 # success

def passCheck(s=''):
    if minCheck(s) == -1: # minCheck(string) already checks most of the requirements
        return -1 # failure, something in minCheck didn't work
    spec = [ 1 for x in s if x in SPECIAL ] # returns list of 1s for evey special character in s
    if len(spec) == 0: # not enough special characters
        print(f"Too few special characters in {s}, found {len(spec)}")
        return -1
    score = 1 if len(s) <= 3 else 3 if len(s) <= 5 else 5 if len(s) <= 7 else 8 if len(s) <= 8 else 10 #if less than 3, 1; if less than 5, 3;
                                                                                                       #if less than 7, 5; if less than 8, 8;
                                                                                                       #if greater than or equal to 8, 10;
    result = f"Your password: {s} has recieved a score of: {score}\n"
    print(result)
    return score


# test cases

print('\n=========== MINCHECK ================\n')
minCheck('')
minCheck('123456789')
minCheck('qwertyuioplkjhgfdewazxcvbnm,')
minCheck('QWERTYUIKJHGVCDX')
minCheck('qazxswedcWERFDCX')
minCheck('.?!&#,;:-_*')
minCheck('aNoobPassword1234!@')
minCheck('qazWSD123~!')
minCheck('qA`1 ')
print('\n=========== PASSCHECK ===============\n')
passCheck('')
passCheck('123456789')
passCheck('qwertyuioplkjhgfdewazxcvbnm,')
passCheck('QWERTYUIKJHGVCDX')
passCheck('qazxswedcWERFDCX')
passCheck('.?!&#,;:-_*')
passCheck('aNoobPassword1234!&')
passCheck('qazWSD123-!')
passCheck('qA.1 ')