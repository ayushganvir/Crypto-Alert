# Generated by Django 4.0.6 on 2022-07-21 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinalert',
            name='coin_symbol',
            field=models.CharField(choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Tether', 'Tether'), ('USD Coin', 'USD Coin'), ('BNB', 'BNB'), ('Binance USD', 'Binance USD'), ('XRP', 'XRP'), ('Cardano', 'Cardano'), ('Solana', 'Solana'), ('Dogecoin', 'Dogecoin'), ('Polkadot', 'Polkadot'), ('Polygon', 'Polygon'), ('Shiba Inu', 'Shiba Inu'), ('Dai', 'Dai'), ('Avalanche', 'Avalanche'), ('Lido Staked Ether', 'Lido Staked Ether'), ('TRON', 'TRON'), ('Wrapped Bitcoin', 'Wrapped Bitcoin'), ('LEO Token', 'LEO Token'), ('Litecoin', 'Litecoin'), ('FTX', 'FTX'), ('OKB', 'OKB'), ('Cronos', 'Cronos'), ('Ethereum Classic', 'Ethereum Classic'), ('Chainlink', 'Chainlink'), ('Uniswap', 'Uniswap'), ('NEAR Protocol', 'NEAR Protocol'), ('Cosmos Hub', 'Cosmos Hub'), ('Stellar', 'Stellar'), ('Monero', 'Monero'), ('Algorand', 'Algorand'), ('Bitcoin Cash', 'Bitcoin Cash'), ('Chain', 'Chain'), ('Theta Fuel', 'Theta Fuel'), ('Flow', 'Flow'), ('VeChain', 'VeChain'), ('ApeCoin', 'ApeCoin'), ('The Sandbox', 'The Sandbox'), ('Internet Computer', 'Internet Computer'), ('Decentraland', 'Decentraland'), ('Hedera', 'Hedera'), ('Tezos', 'Tezos'), ('Frax', 'Frax'), ('Quant', 'Quant'), ('Filecoin', 'Filecoin'), ('Axie Infinity', 'Axie Infinity'), ('Aave', 'Aave'), ('Elrond', 'Elrond'), ('TrueUSD', 'TrueUSD'), ('Theta Network', 'Theta Network'), ('Helium', 'Helium'), ('Bitcoin SV', 'Bitcoin SV'), ('EOS', 'EOS'), ('cUSDC', 'cUSDC'), ('KuCoin', 'KuCoin'), ('Huobi BTC', 'Huobi BTC'), ('Pax Dollar', 'Pax Dollar'), ('Maker', 'Maker'), ('THORChain', 'THORChain'), ('BitTorrent', 'BitTorrent'), ('cETH', 'cETH'), ('IOTA', 'IOTA'), ('Fantom', 'Fantom'), ('The Graph', 'The Graph'), ('Zcash', 'Zcash'), ('eCash', 'eCash'), ('Lido DAO', 'Lido DAO'), ('Neutrino USD', 'Neutrino USD'), ('cDAI', 'cDAI'), ('Huobi', 'Huobi'), ('Klaytn', 'Klaytn'), ('USDD', 'USDD'), ('Tenset', 'Tenset'), ('Amp', 'Amp'), ('Arweave', 'Arweave'), ('NEO', 'NEO'), ('Synthetix Network', 'Synthetix Network'), ('Radix', 'Radix'), ('DeFiChain', 'DeFiChain'), ('Gate', 'Gate'), ('Zilliqa', 'Zilliqa'), ('STEPN', 'STEPN'), ('Basic Attention', 'Basic Attention'), ('Chiliz', 'Chiliz'), ('PAX Gold', 'PAX Gold'), ('BitDAO', 'BitDAO'), ('Enjin Coin', 'Enjin Coin'), ('Stacks', 'Stacks'), ('Waves', 'Waves'), ('Kusama', 'Kusama'), ('Loopring', 'Loopring'), ('Dash', 'Dash'), ('ECOMI', 'ECOMI'), ('PancakeSwap', 'PancakeSwap'), ('Curve DAO', 'Curve DAO'), ('Convex Finance', 'Convex Finance'), ('NEM', 'NEM'), ('Frax Share', 'Frax Share'), ('Celo', 'Celo'), ('Mina Protocol', 'Mina Protocol')], default='Bitcoin', max_length=60),
        ),
        migrations.AlterField(
            model_name='coinalert',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to=settings.AUTH_USER_MODEL),
        ),
    ]