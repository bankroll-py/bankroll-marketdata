from abc import abstractmethod
from bankroll.broker import AccountData

from .provider import MarketDataProvider


class MarketConnectedAccountData(AccountData):
    @property
    @abstractmethod
    def marketDataProvider(self) -> MarketDataProvider:
        pass
