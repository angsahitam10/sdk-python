import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    resp = await client.fetch_ping()
    print("Health OK?", resp)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
