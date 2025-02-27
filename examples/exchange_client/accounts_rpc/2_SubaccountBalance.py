import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    subaccount_id = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    denom = "inj"
    balance = await client.get_subaccount_balance(subaccount_id=subaccount_id, denom=denom)
    print(balance)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
