# Copyright 2022 Injective Labs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import logging

from pyinjective.composer import Composer as ProtoMsgComposer
from pyinjective.async_client import AsyncClient
from pyinjective.transaction import Transaction
from pyinjective.constant import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    composer = ProtoMsgComposer(network=network.string())

    # initialize grpc client
    client = AsyncClient(network, insecure=False)
    await client.sync_timeout_height()

    # load account
    priv_key = PrivateKey.from_hex("f9db9bf330e23cb7839039e944adef6e9df447b90b503d5b4464c90bea9022f3")
    pub_key = priv_key.to_public_key()
    address = await pub_key.to_address().async_init_num_seq(network.lcd_endpoint)
    subaccount_id = address.get_subaccount_id(index=0)

    # prepare trade info
    market_id = "0x4ca0f92fc28be0c9761326016b5a1a2177dd6375558365116b5bdda9abc229ce"
    orders = [
        composer.OrderData(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash="0x1d3b3562af4ea7f972b77261aa956d0741d2aef1c7d54b258cb95bfbbdce5c00"
        ),
        composer.OrderData(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash="0x9c552c62970061a5cf16fd6de4bb5defc023f8fe5692628588fef7b6519eedf6"
        )
    ]

    # prepare tx msg
    msg = composer.MsgBatchCancelDerivativeOrders(
        sender=address.to_acc_bech32(),
        data=orders
    )

    # build sim tx
    tx = (
        Transaction()
        .with_messages(msg)
        .with_sequence(address.get_sequence())
        .with_account_num(address.get_number())
        .with_chain_id(network.chain_id)
    )
    sim_sign_doc = tx.get_sign_doc(pub_key)
    sim_sig = priv_key.sign(sim_sign_doc.SerializeToString())
    sim_tx_raw_bytes = tx.get_tx_data(sim_sig, pub_key)

    # simulate tx
    (sim_res, success) = await client.simulate_tx(sim_tx_raw_bytes)
    if not success:
        print(sim_res)
        return

    sim_res_msg = ProtoMsgComposer.MsgResponses(sim_res.result.data, simulation=True)
    print("simulation msg response")
    print(sim_res_msg)

    # build tx
    gas_price = 500000000
    gas_limit = sim_res.gas_info.gas_used + 20000  # add 20k for gas, fee computation
    fee = [composer.Coin(
        amount=gas_price * gas_limit,
        denom=network.fee_denom,
    )]
    tx = tx.with_gas(gas_limit).with_fee(fee).with_memo('').with_timeout_height(client.timeout_height)
    sign_doc = tx.get_sign_doc(pub_key)
    sig = priv_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = tx.get_tx_data(sig, pub_key)

    # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
    res = await client.send_tx_sync_mode(tx_raw_bytes)
    print(res)
    print("gas wanted: {}".format(gas_limit))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
