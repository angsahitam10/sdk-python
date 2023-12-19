from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from pyinjective.constant import ADDITIONAL_CHAIN_FORMAT_DECIMALS, Denom
from pyinjective.core.token import Token


@dataclass(eq=True, frozen=True)
class SpotMarket:
    id: str
    status: str
    ticker: str
    base_token: Token
    quote_token: Token
    maker_fee_rate: Decimal
    taker_fee_rate: Decimal
    service_provider_fee: Decimal
    min_price_tick_size: Decimal
    min_quantity_tick_size: Decimal

    def quantity_to_chain_format(self, human_readable_value: Decimal) -> Decimal:
        chain_formatted_value = human_readable_value * Decimal(f"1e{self.base_token.decimals}")
        quantized_value = chain_formatted_value // self.min_quantity_tick_size * self.min_quantity_tick_size
        return quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def price_to_chain_format(self, human_readable_value: Decimal) -> Decimal:
        decimals = self.quote_token.decimals - self.base_token.decimals
        chain_formatted_value = human_readable_value * Decimal(f"1e{decimals}")
        quantized_value = (chain_formatted_value // self.min_price_tick_size) * self.min_price_tick_size
        return quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def quantity_from_chain_format(self, chain_value: Decimal) -> Decimal:
        return chain_value / Decimal(f"1e{self.base_token.decimals}")

    def price_from_chain_format(self, chain_value: Decimal) -> Decimal:
        decimals = self.base_token.decimals - self.quote_token.decimals
        return chain_value * Decimal(f"1e{decimals}")


@dataclass(eq=True, frozen=True)
class DerivativeMarket:
    id: str
    status: str
    ticker: str
    oracle_base: str
    oracle_quote: str
    oracle_type: str
    oracle_scale_factor: int
    initial_margin_ratio: Decimal
    maintenance_margin_ratio: Decimal
    quote_token: Token
    maker_fee_rate: Decimal
    taker_fee_rate: Decimal
    service_provider_fee: Decimal
    min_price_tick_size: Decimal
    min_quantity_tick_size: Decimal

    def quantity_to_chain_format(self, human_readable_value: Decimal) -> Decimal:
        # Derivative markets do not have a base market to provide the number of decimals
        chain_formatted_value = human_readable_value
        quantized_value = chain_formatted_value // self.min_quantity_tick_size * self.min_quantity_tick_size
        return quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def price_to_chain_format(self, human_readable_value: Decimal) -> Decimal:
        decimals = self.quote_token.decimals
        chain_formatted_value = human_readable_value * Decimal(f"1e{decimals}")
        quantized_value = (chain_formatted_value // self.min_price_tick_size) * self.min_price_tick_size
        return quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def margin_to_chain_format(self, human_readable_value: Decimal) -> Decimal:
        decimals = self.quote_token.decimals
        chain_formatted_value = human_readable_value * Decimal(f"1e{decimals}")
        quantized_value = (chain_formatted_value // self.min_quantity_tick_size) * self.min_quantity_tick_size
        return quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def calculate_margin_in_chain_format(
        self, human_readable_quantity: Decimal, human_readable_price: Decimal, leverage: Decimal
    ) -> Decimal:
        chain_formatted_quantity = human_readable_quantity
        chain_formatted_price = human_readable_price * Decimal(f"1e{self.quote_token.decimals}")
        margin = (chain_formatted_price * chain_formatted_quantity) / leverage
        # We are using the min_quantity_tick_size to quantize the margin because that is the way margin is validated
        # in the chain (it might be changed to a min_notional in the future)
        quantized_margin = (margin // self.min_quantity_tick_size) * self.min_quantity_tick_size
        return quantized_margin * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def quantity_from_chain_format(self, chain_value: Decimal) -> Decimal:
        return chain_value

    def price_from_chain_format(self, chain_value: Decimal) -> Decimal:
        return chain_value * Decimal(f"1e-{self.quote_token.decimals}")

    def margin_from_chain_format(self, chain_value: Decimal) -> Decimal:
        return chain_value * Decimal(f"1e-{self.quote_token.decimals}")


@dataclass(eq=True, frozen=True)
class BinaryOptionMarket:
    id: str
    status: str
    ticker: str
    oracle_symbol: str
    oracle_provider: str
    oracle_type: str
    oracle_scale_factor: int
    expiration_timestamp: int
    settlement_timestamp: int
    quote_token: Token
    maker_fee_rate: Decimal
    taker_fee_rate: Decimal
    service_provider_fee: Decimal
    min_price_tick_size: Decimal
    min_quantity_tick_size: Decimal

    def quantity_to_chain_format(self, human_readable_value: Decimal, special_denom: Optional[Denom] = None) -> Decimal:
        # Binary option markets do not have a base market to provide the number of decimals
        decimals = 0 if special_denom is None else special_denom.base
        min_quantity_tick_size = (
            self.min_quantity_tick_size if special_denom is None else special_denom.min_quantity_tick_size
        )
        chain_formatted_value = human_readable_value * Decimal(f"1e{decimals}")
        quantized_value = chain_formatted_value // min_quantity_tick_size * min_quantity_tick_size
        return quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def price_to_chain_format(self, human_readable_value: Decimal, special_denom: Optional[Denom] = None) -> Decimal:
        decimals = self.quote_token.decimals if special_denom is None else special_denom.quote
        min_price_tick_size = self.min_price_tick_size if special_denom is None else special_denom.min_price_tick_size
        chain_formatted_value = human_readable_value * Decimal(f"1e{decimals}")
        quantized_value = (chain_formatted_value // min_price_tick_size) * min_price_tick_size
        return quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def calculate_margin_in_chain_format(
        self,
        human_readable_quantity: Decimal,
        human_readable_price: Decimal,
        is_buy: bool,
        special_denom: Optional[Denom] = None,
    ) -> Decimal:
        quantity_decimals = 0 if special_denom is None else special_denom.base
        price_decimals = self.quote_token.decimals if special_denom is None else special_denom.quote
        min_quantity_tick_size = (
            self.min_quantity_tick_size if special_denom is None else special_denom.min_quantity_tick_size
        )
        price = human_readable_price if is_buy else 1 - human_readable_price
        chain_formatted_quantity = human_readable_quantity * Decimal(f"1e{quantity_decimals}")
        chain_formatted_price = price * Decimal(f"1e{price_decimals}")
        margin = chain_formatted_price * chain_formatted_quantity
        # We are using the min_quantity_tick_size to quantize the margin because that is the way margin is validated
        # in the chain (it might be changed to a min_notional in the future)
        quantized_margin = (margin // min_quantity_tick_size) * min_quantity_tick_size
        return quantized_margin * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

    def quantity_from_chain_format(self, chain_value: Decimal, special_denom: Optional[Denom] = None) -> Decimal:
        # Binary option markets do not have a base market to provide the number of decimals
        decimals = 0 if special_denom is None else special_denom.base
        return chain_value * Decimal(f"1e-{decimals}")

    def price_from_chain_format(self, chain_value: Decimal, special_denom: Optional[Denom] = None) -> Decimal:
        decimals = self.quote_token.decimals if special_denom is None else special_denom.quote
        return chain_value * Decimal(f"1e-{decimals}")
