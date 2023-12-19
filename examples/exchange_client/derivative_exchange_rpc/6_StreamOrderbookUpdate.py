import asyncio
from decimal import Decimal

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


class PriceLevel:
    def __init__(self, price: Decimal, quantity: Decimal, timestamp: int):
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"price: {self.price} | quantity: {self.quantity} | timestamp: {self.timestamp}"


class Orderbook:
    def __init__(self, market_id: str):
        self.market_id = market_id
        self.sequence = -1
        self.levels = {"buys": {}, "sells": {}}


async def load_orderbook_snapshot(async_client: AsyncClient, orderbook: Orderbook):
    # load the snapshot
    res = await async_client.get_derivative_orderbooksV2(market_ids=[orderbook.market_id])
    for snapshot in res.orderbooks:
        if snapshot.market_id != orderbook.market_id:
            raise Exception("unexpected snapshot")

        orderbook.sequence = int(snapshot.orderbook.sequence)

        for buy in snapshot.orderbook.buys:
            orderbook.levels["buys"][buy.price] = PriceLevel(
                price=Decimal(buy.price),
                quantity=Decimal(buy.quantity),
                timestamp=buy.timestamp,
            )
        for sell in snapshot.orderbook.sells:
            orderbook.levels["sells"][sell.price] = PriceLevel(
                price=Decimal(sell.price),
                quantity=Decimal(sell.quantity),
                timestamp=sell.timestamp,
            )
        break


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    async_client = AsyncClient(network)

    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    orderbook = Orderbook(market_id=market_id)

    # start getting price levels updates
    stream = await async_client.stream_derivative_orderbook_update(market_ids=[market_id])
    first_update = None
    async for update in stream:
        first_update = update.orderbook_level_updates
        break

    # load the snapshot once we are already receiving updates, so we don't miss any
    await load_orderbook_snapshot(async_client=async_client, orderbook=orderbook)

    # start consuming updates again to process them
    apply_orderbook_update(orderbook, first_update)
    async for update in stream:
        apply_orderbook_update(orderbook, update.orderbook_level_updates)


def apply_orderbook_update(orderbook: Orderbook, updates):
    # discard old updates
    if updates.sequence <= orderbook.sequence:
        return

    print(" * * * * * * * * * * * * * * * * * * *")

    # ensure we have not missed any update
    if updates.sequence > (orderbook.sequence + 1):
        raise Exception(
            f"missing orderbook update events from stream, must restart: {updates.sequence} vs {orderbook.sequence + 1}"
        )

    print(f"updating orderbook with updates at sequence {updates.sequence}")

    # update orderbook
    orderbook.sequence = updates.sequence
    for direction, levels in {"buys": updates.buys, "sells": updates.sells}.items():
        for level in levels:
            if level.is_active:
                # upsert level
                orderbook.levels[direction][level.price] = PriceLevel(
                    price=Decimal(level.price), quantity=Decimal(level.quantity), timestamp=level.timestamp
                )
            elif level.price in orderbook.levels[direction]:
                del orderbook.levels[direction][level.price]

    # sort the level numerically
    buys = sorted(orderbook.levels["buys"].values(), key=lambda x: x.price, reverse=True)
    sells = sorted(orderbook.levels["sells"].values(), key=lambda x: x.price, reverse=True)

    # lowest sell price should be higher than the highest buy price
    if len(buys) > 0 and len(sells) > 0:
        highest_buy = buys[0].price
        lowest_sell = sells[-1].price
        print(f"Max buy: {highest_buy} - Min sell: {lowest_sell}")
        if highest_buy >= lowest_sell:
            raise Exception("crossed orderbook, must restart")

    # for the example, print the list of buys and sells orders.
    print("sells")
    for k in sells:
        print(k)
    print("=========")
    print("buys")
    for k in buys:
        print(k)
    print("====================================")


if __name__ == "__main__":
    asyncio.run(main())
