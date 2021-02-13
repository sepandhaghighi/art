test_req = ""

with open('dev-requirements.txt', 'r') as f:
    for line in f:
        if '==' not in line:
            test_req += line

with open('test-requirements.txt', 'w') as f:
    f.write(test_req)
