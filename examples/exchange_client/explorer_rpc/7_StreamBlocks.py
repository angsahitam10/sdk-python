import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    stream_blocks = await client.stream_blocks()
    async for block in stream_blocks:
        print(block)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
