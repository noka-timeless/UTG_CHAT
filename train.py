import asyncio
from rasa.cli import train

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.set_start_method("spawn", force=True)

    asyncio.run(train.train())