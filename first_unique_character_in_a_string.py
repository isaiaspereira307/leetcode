def first_unique_character_in_a_string(s: str):
    m = [0] * 26
    for char in s:
        m[ord(char) - ord('a')] += 1

    for i, char in enumerate(s):
        if m[ord(char) - ord('a')] == 1:
            return i

    return -1
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
import pytest 
 
@pytest.mark.benchmark(
        group="funcoes",
        timer=time.process_time,
        disable_gc=True
)
def test_minha_funcao(benchmark):
    resultado = benchmark(minha_funcao)

    assert(resultado("leetcode"), 0)
    assert(first_unique_character_in_a_string("loveleetcode"), 2)
    assert(first_unique_character_in_a_string("aabb"), -1)

if __name__=="__main__":
    pytest.main(args=["-v", "--benchmark-group-by=group"])

