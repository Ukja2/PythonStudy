def count_words(s):
    if s == "": #입력받은 문자열이 아무것도 없을 때 단어 0개를 출력
        return 0
    
    word = 0 # 단어 개수를 세는 변수
    switch = False # 단어를 구별하는 스위치 변수

    for i in s: # 입력받은 문자열의 단어에 대해 순차적으로 접근
        if i != " ": # 만약 i번째 문자가 공백이 아닐때
            if not switch: # 현재 switch의 반대일때 즉 swtich가 false면 실행 true면 실행x
                word += 1 #단어개수 1개 증가
                switch = True #스위치 true로 전환
        else: 
            switch = False #공백이 발생할 때 switch를 false로 전환
            
    return word

#switch를 false로 설정해놓음으로서 첫 문자 시작시 단어개수를 한 번 세고, 이후에는 True를 유지하다 공백 발생 시 switch를 false로 변환함으로서
#다음 단어가 시작되면 단어 개수가 1 증가한다.
