from abc import ABC, abstractmethod
from typing import Iterable, Tuple

from rx.core.typing import Observable

from bankroll.model import Cash, Instrument, Quote


class MarketDataProvider(ABC):
    # Fetches up-to-date quotes for the provided instruments.
    # May return the results in any order.
    @abstractmethod
    def fetchQuotes(
        self, instruments: Iterable[Instrument]
    ) -> Iterable[Tuple[Instrument, Quote]]:
        pass


class StreamingMarketDataProvider(MarketDataProvider):
    # Subscribes to streaming quotes for the provided instruments.
    @abstractmethod
    def subscribeToQuotes(
        self, instruments: Iterable[Instrument]
    ) -> Observable[Tuple[Instrument, Quote]]:
        pass
