from abc import abstractmethod
from bankroll.broker import AccountData

from .provider import MarketDataProvider

class MarketConnectedAccountData(AccountData):
    @abstractmethod
    @property
    def marketDataProvider(self) -> MarketDataProvider:
        pass