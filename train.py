"""Small validation fixture for the ReproGuard cross-repository demo."""

BATCH_SIZE = 16
RANDOM_SEED = 2026


def train():
    return BATCH_SIZE, RANDOM_SEED
