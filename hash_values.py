from hashlib import *

__all__ = ['get_md5', 'get_sha1']


def get_md5(string, encoding='utf-8'):
    return md5(string.encode(encoding=encoding)).hexdigest()


def get_sha1(string, encoding='utf-8', pattern=0):  # 此处0不能换成 null，因为它是一个索引而非空值。
    base = (md5,
            sha1, sha224, sha256, sha384, sha512,
            blake2b, blake2s,
            sha3_224, sha3_256, sha3_384, sha3_512,
            shake_128, shake_256,)
    choice = base[pattern % len(base)]
    return choice(string.encode(encoding=encoding)).hexdigest()


if __name__ == '__main__':
    print(get_sha1('挨打的份的规范化', pattern=-1))
