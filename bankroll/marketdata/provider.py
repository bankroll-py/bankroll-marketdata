from abc import ABC, abstractmethod
from typing import Iterable, Tuple

from bankroll.model import Cash, Instrument, Quote


class MarketDataProvider(ABC):
    # Fetches up-to-date quotes for the provided instruments.
    # May return the results in any order.
    @abstractmethod
    def fetchQuotes(
        self, instruments: Iterable[Instrument]
    ) -> Iterable[Tuple[Instrument, Quote]]:
        pass
