import pytest
import time

from backend.blockchain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS
from backend.util.hex_to_binary import hex_to_binary

# Use to calculate mine_rate into seconds to use for sleep delay
DELAY = MINE_RATE / SECONDS


def test_mine_block():
    # Set up a block
    last_block = Block.genesis()
    data = "test-data"
    block = Block.mine_block(last_block, data)

    # Confirm block is instance of Block, has correct data, and last_lash
    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash


def test_mine_block_leading_zeros():
    # Set up a block
    last_block = Block.genesis()
    data = "test-data"
    block = Block.mine_block(last_block, data)

    # Check that the block hash has the correct number of leading zeros
    assert hex_to_binary(block.hash)[0 : block.difficulty] == "0" * block.difficulty


def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)

    # Loop through the const genesis, and compare genesis data with the const data
    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) == value


def test_quickly_mined_block():
    # Mimic mined blocks that trigger a difficulty raise due to fast mining
    last_block = Block.mine_block(Block.genesis(), "foo")
    mined_block = Block.mine_block(last_block, "bar")

    assert mined_block.difficulty == last_block.difficulty + 1


def test_slowly_mined_block():
    # Mimic mined blocks that trigger a difficulty lower due to slow mining
    last_block = Block.mine_block(Block.genesis(), "foo")

    # Create a delay in between mining blocks
    time.sleep(DELAY)

    mined_block = Block.mine_block(last_block, "bar")

    assert mined_block.difficulty == last_block.difficulty - 1


def test_mine_block_difficulty_limits_at_1():
    # Create a mined block with lowest possible difficulty (1)
    last_block = Block(time.time_ns(), "test_last_hash", "test_hash", "test-data", 1, 0)

    time.sleep(DELAY)
    mined_block = Block.mine_block(last_block, "bar")

    assert mined_block.difficulty == 1


@pytest.fixture
def last_block():
    return Block.genesis()


@pytest.fixture
def block(last_block):
    return Block.mine_block(last_block, "test_data")


def test_is_valid_block(last_block, block):
    # The test will pass as long is it does not raise an exception
    Block.is_valid_block(last_block, block)


def test_is_valid_block_bad_last_hash(last_block, block):
    # Edit the last_hash data to manually trigger bad data
    block.last_hash = "evil_last_hash"

    # Expecting an exception to be thrown with exact match for exception message
    with pytest.raises(Exception, match="last_hash must be correct"):
        Block.is_valid_block(last_block, block)


def test_is_valid_block_bad_proof_of_work(last_block, block):
    # Edit the hash to manually trigger bad data
    block.hash = "fff"

    # Expecting an exception to be thrown with exact match for exception message
    with pytest.raises(Exception, match="proof of work requirement was not met"):
        Block.is_valid_block(last_block, block)


def test_is_valid_block_jumped_difficulty(last_block, block):
    jumped_difficulty = 10
    block.difficulty = jumped_difficulty
    # Set the hash to have correct amount of leading zeros with the increased difficulty
    block.hash = f'{"0" * jumped_difficulty}111abc'

    # Expecting an exception to be thrown with exact match for exception message
    with pytest.raises(Exception, match="difficulty must only adjust by 1"):
        Block.is_valid_block(last_block, block)


def test_is_valid_block_bad_block_hash(last_block, block):
    # Change the hash in a sneak way adding leading zeros to trick proof of work requirement
    block.hash = "00000000000000000000bbbabc"

    # Expecting an exception to be thrown with exact match for exception message
    with pytest.raises(Exception, match="block hash must be correct"):
        Block.is_valid_block(last_block, block)
