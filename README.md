This is an experimental reimplementation of the Valve item system on top of the Ethereum blockchain.

The system is described in the following series of blog posts under website/.

1. [Introduction: The Blockchain Backpack](website/part1.md)
2. [Extension and Blockchain Item Modification](website/part2.md)
3. [Trading with the Blockchain Backpack](website/part3.md)
4. [The Trade-offs Being Made](website/part4.md)
5. [Statistics and Stranges on the Blockchain](website/part5.md)
6. [Crates and the Quality of Randomness](website/part6.md)

The prototype itself lives under src/.

## Disclaimer

While all the code is Apache 2.0 licensed, this isn't a real project; it is proof of concept to show that such a system is possible, and a sequence of blog posts showing why it is desirable.

If you actually want to build a full version of the system I'm outlining, I suggest that you actually throw away everything I've written (except maybe the interface outlined here), and start over.

## Requirements

Assuming you're trying to build this locally (instead of just reading the code), you'll need a few things:

* [The solc compiler](https://github.com/ethereum/cpp-ethereum/wiki)
* [The pyethereum suite for the ethereum emulator](https://github.com/ethereum/pyethereum)
* [The ethertdd.py testing system](https://github.com/ethermarket/ethertdd.py)
* A Python interpreter
* Make

To run the test suite, run:

    cd src/
    make

The file for the backpack contracts is `src/Backpack.sol`. You can find the test suite in `src/backpack_tests.py`.

There's a small python script which takes the TF2 JSON schema file, and a JSON representation of a players backpack and imports the backpack's contents onto a local test chain. You can find that in `src/load_backpack.py`.
