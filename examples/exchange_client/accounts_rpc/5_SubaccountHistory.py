import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    subaccount = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    denom = "inj"
    transfer_types = ["withdraw", "deposit"]
    skip = 1
    limit = 15
    end_time = 1665118340224
    subacc_history = await client.get_subaccount_history(
        subaccount_id=subaccount, denom=denom, transfer_types=transfer_types, skip=skip, limit=limit, end_time=end_time
    )
    print(subacc_history)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
