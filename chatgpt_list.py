# 자료형 예제 데이터
list_example = [1, 2, 2, 3]
set_example = {1, 2, 2, 3}
dict_example = {'a': 1, 'b': 2}
tuple_example = (1, 2, 2, 3)

print("==== 타입 비교 ====")
print("list: ", type(list_example))
print("set: ", type(set_example))
print("dict: ", type(dict_example))
print("tuple: ", type(tuple_example))

print("\n==== 값 출력 ====")
print("list: ", list_example)
print("set: ", set_example)
print("dict: ", dict_example)
print("tuple: ", tuple_example)

print("\n==== 중복 허용 여부 ====")
print("list 중복 허용: ", list_example)
print("set 중복 제거: ", set_example)
print("tuple 중복 허용: ", tuple_example)

print("\n==== 순서 보장 여부 ====")
print("list 순서 유지: ", list_example)
print("set 순서 미보장(3.7부터는 구현상 유지되지만 보장 아님): ", set_example)
print("dict 순서 유지 (3.7+): ", dict_example)
print("tuple 순서 유지: ", tuple_example)

print("\n==== 변경 가능 여부 ====")
# 리스트는 변경 가능
list_example[0] = 100
print("list 변경 후: ", list_example)

# 튜플은 변경 불가능 → 오류 발생
try:
    tuple_example[0] = 100
except TypeError as e:
    print("tuple 변경 시 오류: ", e)

# set은 값 변경은 안되지만, 요소 추가/삭제는 가능
set_example.add(4)
print("set 요소 추가 후: ", set_example)

# dict 값은 변경 가능
dict_example['a'] = 100
print("dict 값 변경 후: ", dict_example)
