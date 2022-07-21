from django.db import models
from name_script import get_coin_names
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class CoinAlert(models.Model):
    coin_names = [('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Tether', 'Tether'), ('USD Coin', 'USD Coin'), ('BNB', 'BNB'), ('XRP', 'XRP'), ('Binance USD', 'Binance USD'), ('Cardano', 'Cardano'), ('Solana', 'Solana'), ('Dogecoin', 'Dogecoin'), ('Polkadot', 'Polkadot'), ('Shiba Inu', 'Shiba Inu'), ('Polygon', 'Polygon'), ('Avalanche', 'Avalanche'), ('Dai', 'Dai'), ('Lido Staked Ether', 'Lido Staked Ether'), ('TRON', 'TRON'), ('Wrapped Bitcoin', 'Wrapped Bitcoin'), ('LEO Token', 'LEO Token'), ('Litecoin', 'Litecoin'), ('FTX', 'FTX'), ('OKB', 'OKB'), ('Cronos', 'Cronos'), ('Chainlink', 'Chainlink'), ('Uniswap', 'Uniswap'), ('NEAR Protocol', 'NEAR Protocol'), ('Ethereum Classic', 'Ethereum Classic'), ('Cosmos Hub', 'Cosmos Hub'), ('Stellar', 'Stellar'), ('Monero', 'Monero'), ('Algorand', 'Algorand'), ('Bitcoin Cash', 'Bitcoin Cash'), ('Flow', 'Flow'), ('VeChain', 'VeChain'), ('ApeCoin', 'ApeCoin'), ('Theta Fuel', 'Theta Fuel'), ('Chain', 'Chain'), ('Internet Computer', 'Internet Computer'), ('The Sandbox', 'The Sandbox'), ('Decentraland', 'Decentraland'), ('Hedera', 'Hedera'), ('Tezos', 'Tezos'), ('Quant', 'Quant'), ('Filecoin', 'Filecoin'), ('Axie Infinity', 'Axie Infinity'), ('Frax', 'Frax'), ('Elrond', 'Elrond'), ('Aave', 'Aave'), ('Theta Network', 'Theta Network'), ('Helium', 'Helium'), ('TrueUSD', 'TrueUSD'), ('Bitcoin SV', 'Bitcoin SV'), ('EOS', 'EOS'), ('KuCoin', 'KuCoin'), ('cUSDC', 'cUSDC'), ('Huobi BTC', 'Huobi BTC'), ('Maker', 'Maker'), ('BitTorrent', 'BitTorrent'), ('cETH', 'cETH'), ('IOTA', 'IOTA'), ('Fantom', 'Fantom'), ('Lido DAO', 'Lido DAO'), ('The Graph', 'The Graph'), ('THORChain', 'THORChain'), ('Zcash', 'Zcash'), ('Pax Dollar', 'Pax Dollar'), ('eCash', 'eCash'), ('Klaytn', 'Klaytn'), ('Arweave', 'Arweave'), ('Tenset', 'Tenset'), ('Huobi', 'Huobi'), ('Neutrino USD', 'Neutrino USD'), ('Amp', 'Amp'), ('NEO', 'NEO'), ('cDAI', 'cDAI'), ('USDD', 'USDD'), ('Synthetix Network', 'Synthetix Network'), ('Radix', 'Radix'), ('Zilliqa', 'Zilliqa'), ('STEPN', 'STEPN'), ('Basic Attention', 'Basic Attention'), ('DeFiChain', 'DeFiChain'), ('Chiliz', 'Chiliz'), ('Waves', 'Waves'), ('Gate', 'Gate'), ('Stacks', 'Stacks'), ('BitDAO', 'BitDAO'), ('Enjin Coin', 'Enjin Coin'), ('PAX Gold', 'PAX Gold'), ('Loopring', 'Loopring'), ('Kusama', 'Kusama'), ('Dash', 'Dash'), ('ECOMI', 'ECOMI'), ('PancakeSwap', 'PancakeSwap'), ('Convex Finance', 'Convex Finance'), ('Frax Share', 'Frax Share'), ('Curve DAO', 'Curve DAO'), ('NEM', 'NEM'), ('Mina Protocol', 'Mina Protocol'), ('Celo', 'Celo')]

    class Status(models.TextChoices):
        CREATED = 'Created', _('Created')
        DELETED = 'Deleted', _('Deleted')
        TRIGGERED = 'Triggered', _('Triggered')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='alerts', null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    coin_symbol = models.CharField(choices=coin_names, default='Bitcoin', max_length=60)
    buy_price = models.IntegerField(null=False)
    alert_price = models.IntegerField(null=False)
    status = models.CharField(choices=Status.choices, max_length=15, default=Status.CREATED)
    # highlighted = models.TextField()

    def __str__(self):
        return 'Alert created by {} for {} at ${} on {}'.format(self.created_by, self.coin_symbol, self.buy_price, self.created_on)

    class Meta:
        ordering = ['created_on']

