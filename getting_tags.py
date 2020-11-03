
with open('Html.txt','r') as f:
    lines=f.readlines()
    br=0
    lines=[i.rstrip('\n') for i in lines]
    for i in range(len(lines)):
        print(f'{str(i).rjust(5)}    {lines[i]}')
    searchby=int(input('To Search by text Enter 1,Else Enter 2'))
    if  searchby== 1:
        input_=input('Enter tag')
        required_=input('Enter required tag')
        for i in range(len(lines)):
            if lines[i] == f'<{input_}>':
                for j in range(i+1,len(lines)):
                    if lines[j] == f'</{input_}>' :
                        br=1
                        break
                    if not lines[j].startswith('</'):
                        print(lines[j])
            if br == 1:
                break
    elif searchby == 2 :
        input_=int(input('Enter line'))
        required_=input('Enter tag')
        for i in range(len(lines)):
            if lines[i] == lines[input_]:
                out="</"+lines[input_][1:-1]+">"
                for j in range(i,len(lines)):
                    if lines[j] == out :
                        br=1
                        break
                    if lines[j].startswith(f'<{required_}'):
                        print(lines[j])
            if br == 1:
                break