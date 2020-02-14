import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = 0
    # block_string = json.dumps(block, sort_keys=True)
    while valid_proof(last_proof, proof) is False:
        proof = random.randint(1, 1000000000000000000000)
        # print(proof)
    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """
# https://lambda-coin-test-1.herokuapp.com/api/full_chain
    old_guess = f'{last_hash}'.encode()
    old_guess_hash = hashlib.sha256(old_guess).hexdigest()
    str_var = len(old_guess_hash)-6

    new_guess = f'{proof}'.encode()
    new_guess_hash = hashlib.sha256(new_guess).hexdigest()

    # print(old_guess_hash, "Last 6 of last hash: ", str(old_guess_hash[str_var:]), '/n*********************/n', new_guess_hash, "First 6 of new hash: ", new_guess_hash[:6])
    return new_guess_hash[:6] == str(old_guess_hash[str_var:])


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        # s = requests.get(url=node + "/full_chain")
        # lbi = len(s.json()['chain'])-1
        # last_block = s.json()['chain'][lbi]
        # print("Full chain: ", s.json()['chain'])
        # print("______________Last block: ", last_block)
        data = r.json()
        # print("Last proof: ", data)
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
