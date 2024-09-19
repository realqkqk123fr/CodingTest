while True:
    try:
        line = input()
        if line == "":
            break  # 빈 문자열 입력 시 종료
        print(line)
    except EOFError:
        break
        