---
sponsor: "QuickSwap and StellaSwap"
slug: "2022-09-quickswap"
date: "2023-12-01"
title: "QuickSwap and StellaSwap contest"
findings: "https://github.com/code-423n4/2022-09-quickswap-findings/issues"
contest: 166
---

# Overview

## About C4

Code4rena (C4) is an open organization consisting of security researchers, auditors, developers, and individuals with domain expertise in smart contracts.

A C4 audit is an event in which community participants, referred to as Wardens, review, audit, or analyze smart contract logic in exchange for a bounty provided by sponsoring projects.

During the audit outlined in this document, C4 conducted an analysis of the QuickSwap and StellaSwap smart contract system written in Solidity. The audit took place between September 26—October 1 2022.

## Wardens

118 Wardens contributed reports to QuickSwap and StellaSwap:

  1. 0x52
  1. [Jeiwan](https://jeiwan.net)
  1. cccz
  1. Lambda
  1. \_\_141345\_\_
  1. rbserver
  1. [0xDecorativePineapple](https://decorativepineapple.github.io/)
  1. [Chom](https://chom.dev)
  1. imare
  1. [berndartmueller](https://twitter.com/berndartmueller)
  1. 0xbepresent
  1. [8olidity](https://twitter.com/8olidity)
  1. tonisives
  1. [0xNazgul](https://twitter.com/0xNazgul)
  1. [0xSmartContract](https://twitter.com/0xSmartContract)
  1. IllIllI
  1. brgltd
  1. CodingNameKiki
  1. [kaden](https://twitter.com/0xKaden)
  1. RockingMiles (robee and pants)
  1. Rolezn
  1. [Deivitto](https://twitter.com/Deivitto)
  1. [c3phas](https://twitter.com/c3ph_)
  1. trustindistrust
  1. ladboy233
  1. cryptonue
  1. 0xmatt
  1. Bnke0x0
  1. [Aymen0909](https://github.com/Aymen1001)
  1. ajtra
  1. [catchup](https://twitter.com/catchup22)
  1. rvierdiiev
  1. delfin454000
  1. RaymondFam
  1. [defsec](https://twitter.com/defsec_)
  1. aysha
  1. 0x1f8b
  1. slowmoses
  1. mics
  1. [oyc\_109](https://twitter.com/andyfeili)
  1. [Tomo](https://tom-sol.notion.site/Who-am-I-3b4dc28e77b647eb90794735a94dd38e)
  1. [martin](https://github.com/martin-petrov03)
  1. [fatherOfBlocks](https://twitter.com/father0fBl0cks)
  1. Shinchan ([Sm4rty](https://twitter.com/Sm4rty_), [prasantgupta52](https://twitter.com/prasantgupta52), and [Rohan16](https://twitter.com/ROHANJH56009256))
  1. V\_B (Barichek and vlad\_bochok)
  1. [JC](https://twitter.com/sm4rtcontr4ct)
  1. [gogo](https://www.linkedin.com/in/georgi-nikolaev-georgiev-978253219)
  1. bulej93
  1. rotcivegaf
  1. Mukund
  1. erictee
  1. lukris02
  1. [durianSausage](https://github.com/lyciumlee)
  1. [Ruhum](https://twitter.com/0xruhum)
  1. Aeros
  1. tnevler
  1. Waze
  1. asutorufos
  1. karanctf
  1. [natzuu](https://twitter.com/natzuu33)
  1. Olivierdem
  1. sikorico
  1. chrisdior4
  1. reassor
  1. [a12jmx](https://twitter.com/a12jmx)
  1. sorrynotsorry
  1. Matin
  1. cryptphi
  1. d3e4
  1. DimitarDimitrov
  1. [Ocean\_Sky](https://twitter.com/bluenights004)
  1. p\_crypt0
  1. pedr02b2
  1. [Satyam\_Sharma](https://twitter/@Satyam33sharma)
  1. mahdikarimi
  1. carrotsmuggler
  1. [Migue](https://twitter.com/angel_tripi)
  1. Trabajo\_de\_mates (Saintcode\_ and tay054)
  1. ReyAdmirado
  1. [ch13fd357r0y3r](https://twitter.com/ch13fd357r0y3r)
  1. minhtrng
  1. neko\_nyaa
  1. [s3cunda](s3cunda.github.io)
  1. [Trust](https://twitter.com/trust__90)
  1. ch0bu
  1. [TomJ](https://mobile.twitter.com/tomj_bb)
  1. ChristianKuri
  1. B2
  1. [zishansami](https://zishansami102.github.io/)
  1. Awesome
  1. beardofginger
  1. saian
  1. SnowMan
  1. HardlyCodeMan
  1. [m\_Rassska](https://t.me/Road220)
  1. [ret2basic](https://twitter.com/ret2basic)
  1. [dharma09](https://twitter.com/im_Dharma09)
  1. [Tomio](https://twitter.com/meidhiwirara)
  1. Saintcode\_
  1. emrekocak
  1. bobirichman
  1. Diraco
  1. francoHacker
  1. [medikko](https://twitter.com/mehmeddukov)
  1. Noah3o6
  1. peiw
  1. [0xRoxas](https://twitter.com/0xRoxas)
  1. Amithuddar
  1. [Fitraldys](https://twitter.com/fitraldys)
  1. 0x5rings
  1. gianganhnguyen
  1. shark
  1. zeesaw

This audit was judged by [0xean](https://code4rena.com/@0xean).

Final report assembled by [liveactionllama](https://twitter.com/liveactionllama).

# Summary

The C4 analysis yielded an aggregated total of 13 unique vulnerabilities. Of these vulnerabilities, 1 received a risk rating in the category of HIGH severity and 12 received a risk rating in the category of MEDIUM severity.

Additionally, C4 analysis included 72 reports detailing issues with a risk rating of LOW severity or non-critical. There were also 80 reports recommending gas optimizations.

All of the issues presented here are linked back to their original finding.

# Scope

The code under review can be found within the [C4 QuickSwap and StellaSwap repository](https://github.com/code-423n4/2022-09-quickswap), and is composed of 13 smart contracts written in the Solidity programming language and includes 1,833 lines of Solidity code.

# Severity Criteria

C4 assesses the severity of disclosed vulnerabilities based on three primary risk categories: high, medium, and low/non-critical.

High-level considerations for vulnerabilities span the following key areas when conducting assessments:

- Malicious Input Handling
- Escalation of privileges
- Arithmetic
- Gas use

For more information regarding the severity criteria referenced throughout the submission review process, please refer to the documentation provided on [the C4 website](https://code4rena.com), specifically our section on [Severity Categorization](https://docs.code4rena.com/awarding/judging-criteria/severity-categorization).

# High Risk Findings (1)
## [[H-01] Malicious users can provide liquidity on behalf of others to keep others in the liquidity cooldown](https://github.com/code-423n4/2022-09-quickswap-findings/issues/70)
*Submitted by cccz, also found by 0x52*

In the AlgebraPool contract, when the user provides liquidity via the mint function, the lastLiquidityAddTimestamp is updated to the current time.

          (_position.liquidity, _position.lastLiquidityAddTimestamp) = (
            liquidityNext,
            liquidityNext > 0 ? (liquidityDelta > 0 ? _blockTimestamp() : lastLiquidityAddTimestamp) : 0
          );

Later when the user removes the liquidity via burn function, the transaction will revert if the current time is less than lastLiquidityAddTimestamp + \_liquidityCooldown.

          if (liquidityDelta < 0) {
            uint32 _liquidityCooldown = liquidityCooldown;
            if (_liquidityCooldown > 0) {
              require((_blockTimestamp() - lastLiquidityAddTimestamp) >= _liquidityCooldown);
            }
          }

liquidityCooldown is max 1 day.<br>
However, in the mint function, users can provide liquidity on behalf of other users, which also means that malicious users can keep other users on liquidity cooldown forever by providing a little bit of liquidity on behalf of other users, thus preventing other users from removing liquidity.

```
  function mint(vladyan18
    address sender,
    address recipient,  // @audit: users can provide liquidity on behalf of other users
    int24 bottomTick,
    int24 topTick,
    uint128 liquidityDesired,
    bytes calldata data
  )
...
      (, int256 amount0Int, int256 amount1Int) = _updatePositionTicksAndFees(recipient, bottomTick, topTick, int256(liquidityActual).toInt128());

```

### Proof of Concept

[AlgebraPool.sol#L226-L231](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L226-L231)<br>
[AlgebraPool.sol#L513-L523](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L513-L523)<br>

### Recommended Mitigation Steps

Consider allowing users to provide liquidity only for themselves, or setting liquidityCooldown to 0.

**[vladyan18 (QuickSwap & StellaSwap) confirmed](https://github.com/code-423n4/2022-09-quickswap-findings/issues/70)**

**[sameepsi (QuickSwap & StellaSwap) disagreed with severity and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/70#issuecomment-1266436575):**
 > This is a valid issue but the severity should be medium. This can be easily mitigated by simply setting up cool down period to 0.

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/70#issuecomment-1267015318):**
 > See comment on [issue #83](https://github.com/code-423n4/2022-09-quickswap-findings/issues/83#issuecomment-1264731071).
> 
> Issue is valid and leads to locking of funds, High severity is warranted.  Turning cool down to 0 would work, but has other consequences for JIT liquidity. 



***
 
# Medium Risk Findings (12)
## [[M-01] Flashloan users can be forced to pay higher fees than expected](https://github.com/code-423n4/2022-09-quickswap-findings/issues/112)
*Submitted by 0x52*

[AlgebraPool.sol#L891-L949](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L891-L949)<br>

The first swap of the block sets the fee that will apply to all other actions during that block, including the fee that will be applied to flashloans. If a swap occurs in the same block before the flashloan, the fee taken from the flashloan will be different than expected potentially much different. This could be used by an adversary to force a flashloan user to pay higher fees. They would frontrun the flashloan call with a swap that would push the fees higher. This is dependent on the current state of the swap beforehand but liquidity providers would have a strong incentive to monitor the pool to maximize their profits.

### Recommended Mitigation Steps

Using the swap fee as the flashloan fee seems counterintuitive to me. It doesn't cause any impermanent loss to the liquidity providers, which is what the dynamic fee is designed to offset. There are two possible solutions to this. The first solution would be to allow the flashloan user to specify a max fee they will pay. The other solution, which I believe makes more sense, is to just use a flat fee on flashloans. This provides more consistent outcomes for flashloan users, making the product more attractive.

**[IliaAzhel (QuickSwap & StellaSwap) acknowledged and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/112#issuecomment-1267327842):**
 > Indeed, the flashloan fee may depend on previous transactions in the block. However, fee can not only increase, but also decrease.



***

## [[M-02] Undercounted liquidity leads to increased `volumePerLiquidityInBlock` and incorrect adaptive fee](https://github.com/code-423n4/2022-09-quickswap-findings/issues/136)
*Submitted by Jeiwan*

Undercounted liquidity leads to incorrect trading volume reporting and affects the adaptive fee calculation. In most cases (when the majority of liquidity in a pool is concentrated around the current price) trading volume is overstated, which results in lowered swap fees.

### Proof of Concept

According to [the Tech Paper](https://algebra.finance/static/Algerbra%20Tech%20Paper-15411d15f8653a81d5f7f574bfe655ad.pdf),
trading volume is one of the three indicators that are used to compute the adaptive swap fee:

> To find the optimal commission amount, depending on the nature of the asset's behavior, the following indicators are monitored:
> 1.  Volatility
> 2.  Liquidity
> 3.  Trading Volume

Further in the paper, it's shown how trading volume per liquidity is calculated:
$$I_t = \frac{\widetilde{L}\_t}{L_t}$$

Where $\widetilde{L}\_t = \sqrt{V\_1 \* V\_2}$ is the average trading volume of assets 1 and 2; $L_t$ is the liquidity that was used during a trade.

In Uniswap V3 (on which Algebra Finance is based), [liquidity is concentrated in discrete price ranges](https://uniswap.org/whitepaper-v3.pdf)–this
can clearly be seen on [the official analytics dashboard](https://info.uniswap.org/#/pools/0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8). During swapping, the current price moves within a price range and, when there's not enough liquidity in the price range to satisfy the swap, jumps to adjacent liquidity positions.
In the case of big swaps and narrow liquidity positions, the current price can traverse over multiple intermediary liquidity positions before the swap is fulfilled and end up in a different price range. In such situation, the liquidity required to fulfil the swap is made of:

1.  liquidity of the initial price range;
2.  liquidity of the intermediary price ranges;
3.  liquidity of the final price range the price has stopped at.

According to the Tech Paper, it's expected that $L_t$ takes into account the liquidity in the initial and final price ranges, as well as liquidity of the intermediary price ranges (since this is the liquidity required to make the swap).
However, in the code, it only counts the liquidity of the final price range (`calculateVolumePerLiquidity` is called after the main swap loop): [AlgebraPool.sol#L880](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L880).

By the time the `calculateVolumePerLiquidity` function is called, `currentLiquidity` is the liquidity that's
available at the new price (the price after a swap), which includes only the price ranges that include the new price. During a swap, `currentLiquidity` is [updated multiple times](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L856)
whenever new liquidity is added or removed while the price is traversing over liquidity positions. The liquidity of the
initial price range and all the intermediary price ranges is not counted by `calculateVolumePerLiquidity`.

The idea of volume per liquidity calculation is somewhat similar to swap fees calculation: swap fees are also calculated on the liquidity engaged in a swap. In the code, swap fees are calculated in the [movePriceTowardsTarget](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/PriceMovementMath.sol#L150) function, which is [called inside the main swap loop](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L789) and which receives [currentLiquidity](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L795) multiple times as the price moves from one price range to another and liquidity gets added and removed. Thus, swap fees are always calculated on the entire liquidity required for a swap while the trading volume computation counts only the price ranges that include the new price after a swap is done.

### Recommended Mitigation Steps

Calculated volume per liquidity on the entire liquidity required for a swap. Use the swap fee amount calculation as a reference.

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/136#issuecomment-1267024609):**
 > Would like the sponsor to weigh in on this one prior to judging.

**[vladyan18 (QuickSwap & StellaSwap) acknowledged, but disagreed with severity and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/136#issuecomment-1267237503):**
 > Thank you!
> 
> Indeed, the calculation taking into account intermediate liquidity would be more correct according to the technical paper, although more expensive in terms of gas. The main purpose of this metric when calculating the adaptive commission is to reduce the commission when there is low activity in the pool. In case of sufficient activity, i.e. the ratio of volumes to liquidity, this metric does not affect the fee. 
> 
> In the current implementation, large volumes will have a stronger impact on fees after swaps ending in "thin" liquidity. And less strongly when getting into more "thick" liquidity. Imo, this behavior is consistent with the purpose of the metric.
> 
> So, in my opinion, this is an issue because it does not exactly match the technical paper, but rather a QA or a medium.

**[0xean (judge) decreased severity to Medium and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/136#issuecomment-1270475991):**
 > Downgrading to M, as this is more a "leak of value" type issue. 
> 
> > 2 — Med: Assets not at direct risk, but the function of the protocol or its availability could be impacted, or leak value with a hypothetical attack path with stated assumptions, but external requirements.



***

## [[M-03] Swapping can be impaired when `activeIncentive` is set](https://github.com/code-423n4/2022-09-quickswap-findings/issues/138)
*Submitted by Jeiwan*

In situations when calls to `AlgebraVirtualPool` fail, swapping would fail as well until the issues with `AlgebraVirtualPool` are resolved or `activeIncentive` is unset.

#### Proof of Concept

During swapping, external calls are made to a `AlgebraVirtualPool` contract when an `activeIncentive` address is set:

*   [AlgebraPool.sol#L753](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L753)
*   [AlgebraPool.sol#L833](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L833)

Either of these calls can fail, which will result in a failed swap. In the case when `AlgebraVirtualPool` fails consistently (due to a misconfiguration or a bug in the contract), swapping would be not possible until the issues in the `AlgebraVirtualPool` contract are resolved or until `activeIncentive` is unset.

### Recommended Mitigation Steps

Short term, handle reverts in the external calls to `AlgebraVirtualPool`. Long term, consider using the pull pattern to synchronize changes: instead of pushing changes to `AlgebraVirtualPool` from `AlgebraPool`, pull necessary data from `AlgebraPool` by calling it from `AlgebraVirtualPool` when needed.

**[vladyan18 (QuickSwap & StellaSwap) acknowledged](https://github.com/code-423n4/2022-09-quickswap-findings/issues/138)**



***

## [[M-04] `safeTransfer` function does not check for existence of ERC20 token contract](https://github.com/code-423n4/2022-09-quickswap-findings/issues/86)
*Submitted by 0xSmartContract, also found by 0xDecorativePineapple, berndartmueller, brgltd, Jeiwan, kaden, and rbserver*

[TransferHelper.sol#L21](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TransferHelper.sol#L21)<br>

The `safeTransfer` function does not check for the existence of the ERC20 token contract , `TransferHelper.sol` performs a transfer with a low-level call without confirming the contract's existence

```js
function safeTransfer(
    address token,
    address to,
    uint256 value
  ) internal {
    (bool success, bytes memory data) = token.call(abi.encodeWithSelector(IERC20Minimal.transfer.selector, to, value));
    require(success && (data.length == 0 || abi.decode(data, (bool))), 'TF');
  }

```

The low-level functions call, delegatecall and staticcall return true as their first return value if the account called is non-existent, as part of the design of the EVM. Account existence must be checked prior to calling if needed.

It allows malicious people to pair with a qualified token like ETH with [dubious] tokens that they can destroy later, and most importantly, to run the safeTransfer function even if the token contract is later destroyed.

### Proof of Concept

1 Alice creates a pair of A and B Tokens (For exampleETH - TestToken Pair).<br>
The creator and only owner of TestToken is Alice.

2 Next, Alice destroys the TestToken with a Selfdestruct based on onlyowner privilege.

3 Bob, unaware of this, deposits ETH into the pool to trade from the ETH-TestToken pair, but cannot receive any tokens because `safeTransfer` does not check for the existence of the contract.

### Recommended Mitigation Steps

Have the SafeTransfer function check the existence of the contract before every transaction.

**[0xean (judge) decreased severity to Medium and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/86#issuecomment-1264738710):**
 > This is technically correct but requires some pretty explicit external requirements that cannot be easily fixed by a permission-less protocol.
> 
> Mainly that if someone creates a pool with an ERC20 that can be self destructed, that pool's paired asset is going to be locked in some form as well.
> 
> I am going to downgrade to M due to the external factors required for this to occur.  The recommended fix could ensure more assets don't become locked as a result of the self destruct. 

**[sameepsi (QuickSwap & StellaSwap) disputed and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/86#issuecomment-1266445479):**
 > Tokens that are destructible are non-standard tokens. We cannot add support for all types of non-standard tokens in the protocol. This protocol is intended to work fine with standard tokens.

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/86#issuecomment-1266996633):**
 > Going to leave as Medium. I understand the sponsor's point here, but also believe there is a fix that would at least reduce some of the risk here. I do agree it is certainly an edge case. 



***

## [[M-05] `exp()` function is not accurate when `x/g` is not small](https://github.com/code-423n4/2022-09-quickswap-findings/issues/202)
*Submitted by \_\_141345\_\_*

[AdaptiveFee.sol#L70-L108](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/AdaptiveFee.sol#L70-L108)<br>

The evaluation of `exp` function will be inaccurate, and further affect the accuracy of `sigmoid()` function, eventually affecting fee calculation.<br>
Also the calculation takes quite a lot of gas to calculate to 8th term.

### Proof of Concept

`x/g` takes value between 0 to 6, but taylor expansion maintains good approximation only near 0. When `x/g` is close to 5, the error is around 7% for `exp()` and 7% for`sigmoid()` respectively. When `x/g` is close to 6, the error could go up to 15% for `exp()` and 18% for `sigmoid()`.

```solidity
// src/core/contracts/libraries/AdaptiveFee.sol
  function exp(
    uint256 x,
    uint16 g,
    uint256 gHighestDegree
  ) internal pure returns (uint256 res) {
    // calculating:
    // g**8 + x * g**7 + (x**2 * g**6) / 2 + (x**3 * g**5) / 6 + (x**4 * g**4) / 24 + (x**5 * g**3) / 120 + (x**6 * g^2) / 720 + x**7 * g / 5040 + x**8 / 40320

    // x**8 < 152 bits (19*8) and g**8 < 128 bits (8*16)
    // so each summand < 152 bits and res < 155 bits
    uint256 xLowestDegree = x;
    res = gHighestDegree; // g**8

    gHighestDegree /= g; // g**7
    res += xLowestDegree * gHighestDegree;

    gHighestDegree /= g; // g**6
    xLowestDegree *= x; // x**2
    res += (xLowestDegree * gHighestDegree) / 2;

    gHighestDegree /= g; // g**5
    xLowestDegree *= x; // x**3
    res += (xLowestDegree * gHighestDegree) / 6;

    gHighestDegree /= g; // g**4
    xLowestDegree *= x; // x**4
    res += (xLowestDegree * gHighestDegree) / 24;

    gHighestDegree /= g; // g**3
    xLowestDegree *= x; // x**5
    res += (xLowestDegree * gHighestDegree) / 120;

    gHighestDegree /= g; // g**2
    xLowestDegree *= x; // x**6
    res += (xLowestDegree * gHighestDegree) / 720;

    xLowestDegree *= x; // x**7
    res += (xLowestDegree * g) / 5040 + (xLowestDegree * x) / (40320);
  }
```

### Recommended Mitigation Steps

The value of `exp(1)`, `exp(2)`, `exp(3)`, `exp(4)`, `exp(5)`, `exp(6)` can be pre-calculated and saved to constants, then be used as denominator or multiplier.

For example, to calculate `exp(3.48)`, what we can do is calculate `exp(0.48)`, and then multiply by `exp(3)`.

When the power is less than 0.5, taylor expansion up to `x^3` can give good accuracy. `exp(0.5)` and corresponding `sigmoid()` has maximum error in the order of 2e-4 to 1e-4.

**[vladyan18 (QuickSwap & StellaSwap) acknowledged and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/202#issuecomment-1267196099):**
 > Thank you!
> 
> Indeed, the Taylor series converges fast enough only close to zero. Tests and practice show that the current degree of accuracy is satisfactory and retains the main property - monotonous growth from volatility. However, the recommendations for gas optimization and accuracy improvement are really good.

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/202#issuecomment-1267798965):**
 > I am going to award this one based on the quality of the report and level of detail. While the error tolerance may be acceptable to the sponsor, I think the warden does a great job of demonstrating their point.



***

## [[M-06] Vault set to the zero-address will break swaps and flash loans in all deployed pools](https://github.com/code-423n4/2022-09-quickswap-findings/issues/210)
*Submitted by berndartmueller, also found by 0xbepresent, 8olidity, and tonisives*

Collected community fees from each swap and flash loan are immediately sent to the defined `AlgebraFactor.vaultAddress` address. Contrary to the used pull pattern in Uniswap V3.

Having fees (ERC-20 tokens) immediately sent to the vault within each swap and flash loan, opens up potential issues if the vault address is set to the zero address.

The following `AlgebraPool` functions are affected:

*   `swap`,
*   `swapSupportingFeeOnInputTokens`, and
*   `flash`

### Impact

If the `AlgebraFactor.vaultAddress` address is set to `address(0)`, **all** Algebra pools deployed by this factory contract will have their swap and flash loan functionality affected in a either completely broken way (transactions will revert due to ERC-20 token transfers to the zero address) or fees are sent (effectively burned) to the zero address. In the end, it will depend on the ERC-20 token implementation if it reverts or simply burns the fees.

### Proof of Concept

[AlgebraFactory.setVaultAddress](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraFactory.sol#L91-L95)

`AlgebraFactory.setVaultAddress` is used by the owner of the `AlgebraFactory` to set the vault address.

```solidity
function setVaultAddress(address _vaultAddress) external override onlyOwner {
  require(vaultAddress != _vaultAddress);
  emit VaultAddress(_vaultAddress);
  vaultAddress = _vaultAddress;
}
```

[AlgebraPool.sol#L918](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L918)

```solidity
function flash(
  address recipient,
  uint256 amount0,
  uint256 amount1,
  bytes calldata data
) external override lock {
  [...]

  address vault = IAlgebraFactory(factory).vaultAddress();

  uint256 paid0 = balanceToken0();
  require(balance0Before.add(fee0) <= paid0, 'F0');
  paid0 -= balance0Before;

  if (paid0 > 0) {
    uint8 _communityFeeToken0 = globalState.communityFeeToken0;
    uint256 fees0;
    if (_communityFeeToken0 > 0) {
      fees0 = (paid0 * _communityFeeToken0) / Constants.COMMUNITY_FEE_DENOMINATOR;
      TransferHelper.safeTransfer(token0, vault, fees0); // @audit-info `vault` is used as the recipient of community fees
    }
    totalFeeGrowth0Token += FullMath.mulDiv(paid0 - fees0, Constants.Q128, _liquidity);
  }

  uint256 paid1 = balanceToken1();
  require(balance1Before.add(fee1) <= paid1, 'F1');
  paid1 -= balance1Before;

  if (paid1 > 0) {
    uint8 _communityFeeToken1 = globalState.communityFeeToken1;
    uint256 fees1;
    if (_communityFeeToken1 > 0) {
      fees1 = (paid1 * _communityFeeToken1) / Constants.COMMUNITY_FEE_DENOMINATOR;
      TransferHelper.safeTransfer(token1, vault, fees1); // @audit-info `vault` is used as the recipient of community fees
    }
    totalFeeGrowth1Token += FullMath.mulDiv(paid1 - fees1, Constants.Q128, _liquidity);
  }

  emit Flash(msg.sender, recipient, amount0, amount1, paid0, paid1);
}
```

[AlgebraPool.\_payCommunityFee](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L546-L549)

This function is called from within the `AlgebraPool.swap` and `AlgebraPool.swapSupportingFeeOnInputTokens` functions.

```solidity
function _payCommunityFee(address token, uint256 amount) private {
  address vault = IAlgebraFactory(factory).vaultAddress();
  TransferHelper.safeTransfer(token, vault, amount);
}
```

### Recommended mitigation steps

Either

*   consider adding a check if `vault == address(0)` in `AlgebraPool._payCommunityFee` and in `AlgebraPool.flash`,
*   prevent setting `vault` to `address(0)` in `AlgebraFactory.setVaultAddress`, or
*   use a pull pattern to collect community (protocol) fees

**[vladyan18 (QuickSwap & StellaSwap) confirmed](https://github.com/code-423n4/2022-09-quickswap-findings/issues/210)**

**[IliaAzhel (QuickSwap & StellaSwap) disagreed with severity](https://github.com/code-423n4/2022-09-quickswap-findings/issues/210)**

**[0xean (judge) decreased severity to Medium and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/210#issuecomment-1267076163):**
 > Downgrading to Medium, requires an admin to set the failure state. 



***

## [[M-07] Incompatibility with Rebasing/Deflationary/Inflationary tokens](https://github.com/code-423n4/2022-09-quickswap-findings/issues/213)
*Submitted by 0xDecorativePineapple, also found by rbserver*

The Algebra protocol does not appear to support rebasing/deflationary/inflationary tokens whose balance changes during transfers or over time. The necessary checks include at least verifying the amount of tokens transferred to contracts before and after the actual transfer to infer any fees/interest.

#### Proof of Concept

[AlgebraPool.sol#L479](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L479)<br>
[AlgebraPool.sol#L548](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L548)<br>
[AlgebraPool.sol#L906](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L906)<br>

### Recommended Mitigation Steps

*   Make sure token vault accounts for any rebasing/inflation/deflation
*   Add support in contracts for such tokens before accepting user-supplied tokens
*   Consider to check before/after balance on the vault

**[sameepsi (QuickSwap & StellaSwap) acknowledged](https://github.com/code-423n4/2022-09-quickswap-findings/issues/213)**



***

## [[M-08] AlgebraPool: `swapSupportingFeeOnInputTokens` loses exact output functionality](https://github.com/code-423n4/2022-09-quickswap-findings/issues/225)
*Submitted by 0x52*

[AlgebraPool.sol#L626-L673](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L626-L673)<br>

Exact output functionality does not exist for fee on transfer tokens.

### Proof of Concept

    require((amountRequired = int256(balanceToken0().sub(balance0Before))) > 0, 'IIA');

Exact output swaps are signaled by setting `amountRequired` to a negative number. When calling `AlgebraPool#swapSupportingFeeOnInputTokens` amount required is set to the difference in token balances before and after which will always be positive. Since `amountRequired` can't be negative, the exact output functionality is impossible to use for those tokens.

### Recommended Mitigation Steps

Fee on transfer tokens are messy and there is no standard implementation to query the fee from the token contract. Ultimately support for these tokens should be added through either user inputs (i.e. allowing high slippage) or a specialized router.

**[vladyan18 (QuickSwap & StellaSwap) acknowledged](https://github.com/code-423n4/2022-09-quickswap-findings/issues/225)**



***

## [[M-09] It is possible that, after swapping, extra input token amount is transferred from user to pool but pool does not give user output token amount that corresponds to the extra input token amount](https://github.com/code-423n4/2022-09-quickswap-findings/issues/255)
*Submitted by rbserver, also found by imare and Lambda*

When calling the `swap` function below, the following `_swapCallback` function is further called for calling the `algebraSwapCallback` function in the callee contract, which is `msg.sender`; such contract could be implemented by a third party especially for non-technical users. There is no guarantee that such contract will not send more input token amount than required to the pool. When this happens, the output token amount corresponding to the extra input token amount will not be transferred from the pool to the recipient after the swap. As a result, the user sends extra input token amount to the pool but does not receive any output token amount corresponding to the extra input token amount. Disputes between the user and protocol can occur because of this.

[AlgebraPool.sol#L580-L586](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L580-L586)

```solidity
  function _swapCallback(
    int256 amount0,
    int256 amount1,
    bytes calldata data
  ) private {
    IAlgebraSwapCallback(msg.sender).algebraSwapCallback(amount0, amount1, data);
  }
```

[AlgebraPool.sol#L589-L623](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L589-L623)

```solidity
  function swap(
    address recipient,
    bool zeroToOne,
    int256 amountRequired,
    uint160 limitSqrtPrice,
    bytes calldata data
  ) external override returns (int256 amount0, int256 amount1) {
    uint160 currentPrice;
    int24 currentTick;
    uint128 currentLiquidity;
    uint256 communityFee;
    // function _calculateSwapAndLock locks globalState.unlocked and does not release
    (amount0, amount1, currentPrice, currentTick, currentLiquidity, communityFee) = _calculateSwapAndLock(zeroToOne, amountRequired, limitSqrtPrice);

    if (zeroToOne) {
      if (amount1 < 0) TransferHelper.safeTransfer(token1, recipient, uint256(-amount1)); // transfer to recipient

      uint256 balance0Before = balanceToken0();
      _swapCallback(amount0, amount1, data); // callback to get tokens from the caller
      require(balance0Before.add(uint256(amount0)) <= balanceToken0(), 'IIA');
    } else {
      if (amount0 < 0) TransferHelper.safeTransfer(token0, recipient, uint256(-amount0)); // transfer to recipient

      uint256 balance1Before = balanceToken1();
      _swapCallback(amount0, amount1, data); // callback to get tokens from the caller
      require(balance1Before.add(uint256(amount1)) <= balanceToken1(), 'IIA');
    }

    if (communityFee > 0) {
      _payCommunityFee(zeroToOne ? token0 : token1, communityFee);
    }

    emit Swap(msg.sender, recipient, amount0, amount1, currentPrice, currentLiquidity, currentTick);
    globalState.unlocked = true; // release after lock in _calculateSwapAndLock
  }
```

### Proof of Concept

First, in `src\core\contracts\test\`, please add the following test callee contract.

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity =0.7.6;

import '../interfaces/IERC20Minimal.sol';
import '../libraries/SafeCast.sol';
import '../interfaces/callback/IAlgebraMintCallback.sol';
import '../interfaces/callback/IAlgebraSwapCallback.sol';
import '../interfaces/IAlgebraPool.sol';

contract TestCalleeForSendingExtraTokenAmount is IAlgebraMintCallback, IAlgebraSwapCallback {
  using SafeCast for uint256;

  function swapExact0For1(
    address pool,
    uint256 amount0In,
    address recipient,
    uint160 limitSqrtPrice
  ) external {
    IAlgebraPool(pool).swap(recipient, true, amount0In.toInt256(), limitSqrtPrice, abi.encode(msg.sender));
  }

  event SwapCallback(int256 amount0Delta, int256 amount1Delta);

  function algebraSwapCallback(
    int256 amount0Delta,
    int256 amount1Delta,
    bytes calldata data
  ) external override {
    address sender = abi.decode(data, (address));

    emit SwapCallback(amount0Delta, amount1Delta);

    // simulate a situation where extra token amount is sent to the pool
    if (amount0Delta > 0) {
      IERC20Minimal(IAlgebraPool(msg.sender).token0()).transferFrom(sender, msg.sender, uint256(amount0Delta) + 1e9);
    } else if (amount1Delta > 0) {
      IERC20Minimal(IAlgebraPool(msg.sender).token1()).transferFrom(sender, msg.sender, uint256(amount1Delta) + 1e9);
    } else {
      assert(amount0Delta == 0 && amount1Delta == 0);
    }
  }

  event MintResult(uint256 amount0Owed, uint256 amount1Owed, uint256 resultLiquidity);

  function mint(
    address pool,
    address recipient,
    int24 bottomTick,
    int24 topTick,
    uint128 amount
  )
    external
    returns (
      uint256 amount0Owed,
      uint256 amount1Owed,
      uint256 resultLiquidity
    )
  {
    (amount0Owed, amount1Owed, resultLiquidity) = IAlgebraPool(pool).mint(msg.sender, recipient, bottomTick, topTick, amount, abi.encode(msg.sender));
    emit MintResult(amount0Owed, amount1Owed, resultLiquidity);
  }

  event MintCallback(uint256 amount0Owed, uint256 amount1Owed);

  function algebraMintCallback(
    uint256 amount0Owed,
    uint256 amount1Owed,
    bytes calldata data
  ) external override {
    address sender = abi.decode(data, (address));

    if (amount0Owed > 0) IERC20Minimal(IAlgebraPool(msg.sender).token0()).transferFrom(sender, msg.sender, amount0Owed);
    if (amount1Owed > 0) IERC20Minimal(IAlgebraPool(msg.sender).token1()).transferFrom(sender, msg.sender, amount1Owed);

    emit MintCallback(amount0Owed, amount1Owed);
  }
}
```

Then, please add the following test in the `AlgebraPool` `describe` block in `src\core\test\AlgebraPool.spec.ts`. This test will pass to demonstrate the described scenario.

```typescript
describe('POC', () => {
    it('It is possible that, after swapping, extra input token amount is transferred from user to pool but pool does not give user output token amount that corresponds to the extra input token amount', async () => {
        /** set up contracts */
        const PoolDeployerFactory = await ethers.getContractFactory('AlgebraPoolDeployer');
        const poolDeployer = await PoolDeployerFactory.deploy();
  
        const FactoryFactory = await ethers.getContractFactory('AlgebraFactory');
        const factory = await FactoryFactory.deploy(poolDeployer.address, vaultAddress);
  
        const TokenFactory = await ethers.getContractFactory('TestERC20');
        const token0 = await TokenFactory.deploy(BigNumber.from(2).pow(255));
        const token1 = await TokenFactory.deploy(BigNumber.from(2).pow(255));
      
        const calleeContractFactory = await ethers.getContractFactory('TestCalleeForSendingExtraTokenAmount');
        const swapTargetCallee = await calleeContractFactory.deploy();
  
        const MockTimeAlgebraPoolDeployerFactory = await ethers.getContractFactory('MockTimeAlgebraPoolDeployer')
        const mockTimePoolDeployer = await MockTimeAlgebraPoolDeployerFactory.deploy();
        const tx = await mockTimePoolDeployer.deployMock(
          factory.address,
          token0.address,
          token1.address
        )
        const receipt = await tx.wait()
        const poolAddress = receipt.events?.[1].args?.pool;
  
        const MockTimeAlgebraPoolFactory = await ethers.getContractFactory('MockTimeAlgebraPool');
        const pool = MockTimeAlgebraPoolFactory.attach(poolAddress);
  
        await pool.initialize(encodePriceSqrt(1, 1));
  
        await token0.approve(swapTargetCallee.address, constants.MaxUint256);
        await token1.approve(swapTargetCallee.address, constants.MaxUint256);
        await swapTargetCallee.mint(pool.address, wallet.address, minTick, maxTick, expandTo18Decimals(1));
        /** */
  
        // set up user
        const user = other;
        await token0.connect(user).mint(user.address, expandTo18Decimals(1));
        await token0.connect(user).approve(swapTargetCallee.address, constants.MaxUint256);
  
        const token0BalancePoolBefore = await token0.balanceOf(pool.address);
        const token0BalanceUserBefore = await token0.balanceOf(user.address);
  
        const token1BalancePoolBefore = await token1.balanceOf(pool.address);
        const token1BalanceUserBefore = await token1.balanceOf(user.address);
  
        // amountIn and amountOut are the expected token amounts to be in and out after the upcoming swap
        const amountIn = expandTo18Decimals(1).div(1000000000);
        const amountOut = -999899999;
  
        await expect(
          // the TestCalleeForSendingExtraTokenAmount contract's algebraSwapCallback function simulates a situation where extra token0 amount is transferred from user to pool
          swapTargetCallee.connect(user).swapExact0For1(pool.address, amountIn, user.address, MIN_SQRT_RATIO.add(1))
        ).to.be.emit(swapTargetCallee, 'SwapCallback').withArgs(amountIn, amountOut);
  
        // after the swap, pool has received the extra token0 amount that was transferred from user
        const token0BalancePoolAfter = await token0.balanceOf(pool.address);
        const token0BalanceUserAfter = await token0.balanceOf(user.address);
        expect(token0BalancePoolAfter).to.be.gt(token0BalancePoolBefore.add(amountIn));
        expect(token0BalanceUserAfter).to.be.lt(token0BalanceUserBefore.sub(amountIn));
  
        // yet, pool does not give user the token1 amount that corresponds to the extra token0 amount
        const token1BalancePoolAfter = await token1.balanceOf(pool.address);
        const token1BalanceUserAfter = await token1.balanceOf(user.address);
        expect(token1BalancePoolAfter).to.be.eq(token1BalancePoolBefore.add(amountOut));
        expect(token1BalanceUserAfter).to.be.eq(token1BalanceUserBefore.sub(amountOut));
    })
})
```

### Tools Used

VSCode

### Recommended Mitigation Steps

[AlgebraPool.sol#L608](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L608) can be updated to the following code.

```solidity
      require(balance0Before.add(uint256(amount0)) == balanceToken0(), 'IIA');
```

Also, [AlgebraPool.sol#L614](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L614) can be updated to the following code.

```solidity
      require(balance1Before.add(uint256(amount1)) == balanceToken1(), 'IIA');
```

**[debych (Quickswap & Stellaswap) confirmed](https://github.com/code-423n4/2022-09-quickswap-findings/issues/255)**

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/255#issuecomment-1270563895):**
 > Going to award as Medium due to sponsor confirming. I think this is more reasonably a QA issue since it assumes a bad integration. Will mark other similar issues as dupe. 



***

## [[M-10] A "FrontRunning attack" can be made to the `initialize` function](https://github.com/code-423n4/2022-09-quickswap-findings/issues/84)
*Submitted by 0xSmartContract, also found by 0xDecorativePineapple, 0xmatt, 0xNazgul, berndartmueller, brgltd, catchup, ch13fd357r0y3r, cryptonue, Jeiwan, ladboy233, minhtrng, neko\_nyaa, rbserver, rvierdiiev, s3cunda, and Trust*

[AlgebraPool.sol#L193-L206](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L193-L206)<br>

The initialize function in `AlgebraPool.sol#L193-L206` is a very important function and sets the liquidity price at the beginning of the pool.

Performs some checks (For example, if the price is not 0).

However it is unprotected against running from the front, and a bot listening to Mempool will run from the front and cause its pool to start at too high or too low of a price.

It is very important that this function is not enabled for FrontRunning operation.

```js
function initialize(uint160 initialPrice) external override {
    require(globalState.price == 0, 'AI');
    // getTickAtSqrtRatio checks validity of initialPrice inside
    int24 tick = TickMath.getTickAtSqrtRatio(initialPrice);

    uint32 timestamp = _blockTimestamp();
    IDataStorageOperator(dataStorageOperator).initialize(timestamp, tick);

    globalState.price = initialPrice;
    globalState.unlocked = true;
    globalState.tick = tick;

    emit Initialize(initialPrice, tick);
  }

```

### Proof of Concept

1- Alice starts a new pool in Algebra and triggers the price determination transaction with `initialize`.<br>
2- Bob listens to the mempool with the following code, which is a minimal example, and sees at what price the `initialize` function is triggered with the `initialPrice` argument, and starts the pool at the price he wants by pre-executing it and makes Alice deposit the wrong amount at the wrong price.

```js
mempool.js
 var customWsProvider = new ethers.providers.WebSocketProvider(url);
 customWsProvider.on("pending", (tx) => { 
 let pendingTx = await connect.provider.getTransaction(txHash);
        if (pendingTx) {
            // filter pendingTx.data
            if (pendingTx.data.indexOf("0xf637731d") !== -1) {      //  func. signature : f637731d  =>  initialize(uint160) 
               console.log(pendingTx);
            }
        }
```

### Recommended Mitigation Steps

Add a `modifier` that ensures that only the authorized person, that is, the first liquidator to the pool, initiates the `initialize` function.

Or, divide the process of determining the price of the pool into parts, first print the price amounts to the state variable, and then make the `initialize` run before this price can be changed.

**[0xean (judge) decreased severity to Medium and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/84#issuecomment-1264733697):**
 > Downgrading to Medium. Alice shouldn't be relying on this initial price to determine the "fair" market price. When there is very limited liquidity the price is extremely easy to move along the x*y=k curve in any case so even after the initialized call is made someone could manipulate the pools pricing very easily when liquidity is low.

**[sameepsi (QuickSwap & StellaSwap) disputed and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/84#issuecomment-1266443768):**
 > I don't think it's a bug. Even if someone sets the wrong price initially then it will be arbitraged. That's how AMMs work by design.

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/84#issuecomment-1267000678):**
 > Going to leave as Medium - even if for nothing else as to warn users in the future to not trust on-chain pricing for new pools or pools with low liquidity.



***

## [[M-11] Biased estimator for volatility used](https://github.com/code-423n4/2022-09-quickswap-findings/issues/47)
*Submitted by Lambda*

[DataStorage.sol#L53](https://github.com/code-423n4/2022-09-quickswap/blob/2ead456d3603d8a4d839cf88f1e41c102b5d040f/src/core/contracts/libraries/DataStorage.sol#L53)<br>

The system calculates the volatility over a time period like this:

$$ \delta(t)=\frac{1}{T} \sum\_{\tau \in\[t-T, t]}(P(\tau)-\bar{P}(\tau))^{2} $$

However, while this estimator is consistent (it converges in probability as the number of samples goes to infinity), it is biased and the produced estimates for finite sample sizes will be generally too low. This will result in fees that are lower than they should be (because the volatility is underestimated) and therefore hurt users.

### Recommended Mitigation Steps

Apply [Bessel's correction](https://en.wikipedia.org/wiki/Bessel%27s_correction) to get an unbiased estimate, i.e.:

$$ \delta(t)=\frac{1}{T - 1} \sum\_{\tau \in\[t-T, t]}(P(\tau)-\bar{P}(\tau))^{2} $$

**[vladyan18 (QuickSwap & StellaSwap) acknowledged and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/47#issuecomment-1265640164):**
 > I believe the current sample size which is 1 day (86 400 seconds) makes Bessel's correction redundant. 
> 
> However, it can play a role in special situations, like here: [DataStorage.sol#L354](https://github.com/code-423n4/2022-09-quickswap/blob/2ead456d3603d8a4d839cf88f1e41c102b5d040f/src/core/contracts/libraries/DataStorage.sol#L354).



***

## [[M-12] Missing slippage control system. Users may lose a lot of funds due to front-running MEV bots.](https://github.com/code-423n4/2022-09-quickswap-findings/issues/284)
*Submitted by Chom, also found by Jeiwan*

[AlgebraPool.sol#L416-L485](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L416-L485)<br>
[AlgebraPool.sol#L589-L623](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L589-L623)<br>
[AlgebraPool.sol#L626-L673](https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L626-L673)<br>

Missing slippage control system. Users may lose a lot of funds due to front-running MEV bots. It has `liquidityDesired` or `amountRequired` but these parameters are only used in output amount calculation. It isn't used to prevent the output amounts from dropping below a threshold. So, MEV bots can front-run to profit from dropping the output amount of user swap.

See warden's [original report](https://github.com/code-423n4/2022-09-quickswap-findings/issues/284) for full PoC and Recommended Mitigation Steps.

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/284#issuecomment-1264766893):**
 > Given the lack of periphery contracts that would handle slippage for minting LP tokens, there doesn't appear to be any mechanism to ensure that during `mint` or `burn` there isn't greater than expected slippage. Will wait for the sponsor to comment on this to confirm my understanding. 
> 
> If correct, this should be a High severity finding as it does lead to a loss of funds from sandwich attacks.

**[vladyan18 (QuickSwap & StellaSwap) acknowledged and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/284#issuecomment-1265521305):**
 > Contracts are initially made taking into account the use of appropriate periphery. Accordingly, slippage control is in the area of responsibility of the periphery.

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/284#issuecomment-1265621037):**
 > Given that this wasn't made explicit in the README and the scope of the contracts that are being audited is what was provided to the wardens, I believe the wardens issue to be valid.

**[sameepsi (QuickSwap & StellaSwap) disagreed with severity and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/284#issuecomment-1266485106):**
 > Yes, it's handled in the periphery contracts. But, I will consider it to be a medium risk given we did not update the README file.

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/284#issuecomment-1267005883):**
 > The issue is not that the README wasn't updated. The issue is that the contracts that were submitted for audit contain a vulnerability. The wardens spent time and energy to find that vulnerability and it should be awarded. It is good to know you already have a mitigation plan in place, but at the time of the wardens doing their work, they had no way of knowing that. 

**[0xean (judge) decreased severity to Medium and commented](https://github.com/code-423n4/2022-09-quickswap-findings/issues/284#issuecomment-1283944159):**
 > After more discussions during QA, it was made clear that I missed the fact the the call from an EOA would revert. So a contract must be the caller here, which makes it less likely that this becomes an issue. While I do think the sponsors should have been more explicit in the readme, this brings down potential for this to be a problem considerably.
> 
> Given that it was not documented and an integrating contract would have to know that it needed to handle slippage will downgrade to Medium.  



***

# Low Risk and Non-Critical Issues

For this audit, 72 reports were submitted by wardens detailing low risk and non-critical issues. The [report highlighted below](https://github.com/code-423n4/2022-09-quickswap-findings/issues/245) by **0xNazgul** received the top score from the judge.

*The following wardens also submitted reports: [CodingNameKiki](https://github.com/code-423n4/2022-09-quickswap-findings/issues/300), [IllIllI](https://github.com/code-423n4/2022-09-quickswap-findings/issues/279), [Deivitto](https://github.com/code-423n4/2022-09-quickswap-findings/issues/313), [0xSmartContract](https://github.com/code-423n4/2022-09-quickswap-findings/issues/180), [Rolezn](https://github.com/code-423n4/2022-09-quickswap-findings/issues/16), [brgltd](https://github.com/code-423n4/2022-09-quickswap-findings/issues/321), [RockingMiles](https://github.com/code-423n4/2022-09-quickswap-findings/issues/2), [Bnke0x0](https://github.com/code-423n4/2022-09-quickswap-findings/issues/18), [Aymen0909](https://github.com/code-423n4/2022-09-quickswap-findings/issues/269), [rbserver](https://github.com/code-423n4/2022-09-quickswap-findings/issues/270), [delfin454000](https://github.com/code-423n4/2022-09-quickswap-findings/issues/234), [RaymondFam](https://github.com/code-423n4/2022-09-quickswap-findings/issues/25), [defsec](https://github.com/code-423n4/2022-09-quickswap-findings/issues/264), [aysha](https://github.com/code-423n4/2022-09-quickswap-findings/issues/217), [\_\_141345\_\_](https://github.com/code-423n4/2022-09-quickswap-findings/issues/198), [mics](https://github.com/code-423n4/2022-09-quickswap-findings/issues/163), [oyc\_109](https://github.com/code-423n4/2022-09-quickswap-findings/issues/27), [trustindistrust](https://github.com/code-423n4/2022-09-quickswap-findings/issues/120), [cccz](https://github.com/code-423n4/2022-09-quickswap-findings/issues/69), [fatherOfBlocks](https://github.com/code-423n4/2022-09-quickswap-findings/issues/58), [sikorico](https://github.com/code-423n4/2022-09-quickswap-findings/issues/166), [slowmoses](https://github.com/code-423n4/2022-09-quickswap-findings/issues/147), [chrisdior4](https://github.com/code-423n4/2022-09-quickswap-findings/issues/19), [Shinchan](https://github.com/code-423n4/2022-09-quickswap-findings/issues/281), [V\_B](https://github.com/code-423n4/2022-09-quickswap-findings/issues/314), [kaden](https://github.com/code-423n4/2022-09-quickswap-findings/issues/107), [reassor](https://github.com/code-423n4/2022-09-quickswap-findings/issues/113), [0x52](https://github.com/code-423n4/2022-09-quickswap-findings/issues/232), [0x1f8b](https://github.com/code-423n4/2022-09-quickswap-findings/issues/51), [JC](https://github.com/code-423n4/2022-09-quickswap-findings/issues/308), [martin](https://github.com/code-423n4/2022-09-quickswap-findings/issues/91), [Tomo](https://github.com/code-423n4/2022-09-quickswap-findings/issues/66), [Jeiwan](https://github.com/code-423n4/2022-09-quickswap-findings/issues/139), [Chom](https://github.com/code-423n4/2022-09-quickswap-findings/issues/280), [Mukund](https://github.com/code-423n4/2022-09-quickswap-findings/issues/6), [a12jmx](https://github.com/code-423n4/2022-09-quickswap-findings/issues/302), [bulej93](https://github.com/code-423n4/2022-09-quickswap-findings/issues/242), [gogo](https://github.com/code-423n4/2022-09-quickswap-findings/issues/287), [ladboy233](https://github.com/code-423n4/2022-09-quickswap-findings/issues/53), [rotcivegaf](https://github.com/code-423n4/2022-09-quickswap-findings/issues/99), [ajtra](https://github.com/code-423n4/2022-09-quickswap-findings/issues/195), [lukris02](https://github.com/code-423n4/2022-09-quickswap-findings/issues/256), [sorrynotsorry](https://github.com/code-423n4/2022-09-quickswap-findings/issues/178), [cryptonue](https://github.com/code-423n4/2022-09-quickswap-findings/issues/275), [erictee](https://github.com/code-423n4/2022-09-quickswap-findings/issues/130), [catchup](https://github.com/code-423n4/2022-09-quickswap-findings/issues/145), [0xDecorativePineapple](https://github.com/code-423n4/2022-09-quickswap-findings/issues/219), [Matin](https://github.com/code-423n4/2022-09-quickswap-findings/issues/222), [Ruhum](https://github.com/code-423n4/2022-09-quickswap-findings/issues/79), [0xmatt](https://github.com/code-423n4/2022-09-quickswap-findings/issues/176), [Aeros](https://github.com/code-423n4/2022-09-quickswap-findings/issues/293), [asutorufos](https://github.com/code-423n4/2022-09-quickswap-findings/issues/173), [cryptphi](https://github.com/code-423n4/2022-09-quickswap-findings/issues/179), [d3e4](https://github.com/code-423n4/2022-09-quickswap-findings/issues/324), [DimitarDimitrov](https://github.com/code-423n4/2022-09-quickswap-findings/issues/189), [Ocean\_Sky](https://github.com/code-423n4/2022-09-quickswap-findings/issues/214), [p\_crypt0](https://github.com/code-423n4/2022-09-quickswap-findings/issues/315), [pedr02b2](https://github.com/code-423n4/2022-09-quickswap-findings/issues/119), [Satyam\_Sharma](https://github.com/code-423n4/2022-09-quickswap-findings/issues/149), [tnevler](https://github.com/code-423n4/2022-09-quickswap-findings/issues/236), [Waze](https://github.com/code-423n4/2022-09-quickswap-findings/issues/212), [durianSausage](https://github.com/code-423n4/2022-09-quickswap-findings/issues/74), [karanctf](https://github.com/code-423n4/2022-09-quickswap-findings/issues/127), [Lambda](https://github.com/code-423n4/2022-09-quickswap-findings/issues/43), [mahdikarimi](https://github.com/code-423n4/2022-09-quickswap-findings/issues/24), [rvierdiiev](https://github.com/code-423n4/2022-09-quickswap-findings/issues/55), [natzuu](https://github.com/code-423n4/2022-09-quickswap-findings/issues/320), [carrotsmuggler](https://github.com/code-423n4/2022-09-quickswap-findings/issues/124), [Migue](https://github.com/code-423n4/2022-09-quickswap-findings/issues/81), [Olivierdem](https://github.com/code-423n4/2022-09-quickswap-findings/issues/239), and [Trabajo\_de\_mates](https://github.com/code-423n4/2022-09-quickswap-findings/issues/42).*

## [N-01] Missing Equivalence Checks in Setters

### Context
[`AlgebraPool.sol#L952`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L952), [`AlgebraPool.sol#L959`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L959), [`AlgebraPool.sol#L967`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L967)

### Description
Setter functions are missing checks to validate if the new value being set is the same as the current value already set in the contract. Such checks will showcase mismatches between on-chain and off-chain states.

### Recommendation
This may hinder detecting discrepancies between on-chain and off-chain states leading to flawed assumptions of on-chain state and protocol behavior.

## [N-02] Missing Zero-address Validation

### Context
[`AlgebraPoolFactory.sol#L77`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraFactory.sol#L77), [`AlgebraPoolFactory.sol#L84`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraFactory.sol#L84), [`AlgebraPoolFactory.sol#L91`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraFactory.sol#L91), [`AlgebraPool.sol#L959`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L959), [`DataStorageOperator.sol#L31`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/DataStorageOperator.sol#L31), [`PoolImmutables.sol#L29`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/base/PoolImmutables.sol#L29)

### Description
Lack of zero-address validation on address parameters may lead to transaction reverts, waste gas, require resubmission of transactions and may even force contract redeployments in certain cases within the protocol.

### Recommendation
Consider adding explicit zero-address validation on input parameters of address type.

## [N-03] Missing Events In Initialize Functions

### Context
[`DataStorage.sol#L364`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L364)

### Description
None of the initialize functions emit emit init-specific events. They all however have the initializer modifier (from Initializable) so that they can be called only once. Off-chain monitoring of calls to these critical functions is not possible.

### Recommendation
It is recommended to emit events in your initialization functions.

## [N-04] Missing Visibility

### Context
[`DataStorageOperator.sol#L15-L16`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/DataStorageOperator.sol#L15-L16)

### Description
It's best practice to explicitly mark visibility of state variables.

### Recommendation
Consider adding the missing visibility to the state variables.

## [N-05] Line Length

### Context
[`AlgebraPoolFactory.sol#L112`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraFactory.sol#L112), [`AlgebraPool.sol#L221`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L221), [`AlgebraPool.sol#L287`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L287), [`AlgebraPool.sol#L297`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L297), [`AlgebraPool.sol#L345`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L345), [`AlgebraPool.sol#L352`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L352), [`AlgebraPool.sol#L355`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L355), [`AlgebraPool.sol#L383`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L383), [`AlgebraPool.sol#L392`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L392), [`AlgebraPool.sol#L472`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L472), [`AlgebraPool.sol#L529`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L529), [`AlgebraPool.sol#L558`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L558), [`AlgebraPool.sol#L577`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L577), [`AlgebraPool.sol#L601`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L601), [`AlgebraPool.sol#L654`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L654), [`AlgebraPool.sol#L680`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L680), [`AlgebraPool.sol#L802`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L802), [`AlgebraPool.sol#L805`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L805), [`AlgebraPool.sol#L814`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L814), [`AlgebraPool.sol#L872-L873`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L872-L873), [`AlgebraPool.sol#L876`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L876), [`AlgebraPool.sol#L880`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L880), [`DataStorageOperator.sol#L45`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/DataStorageOperator.sol#L45), [`DataStorageOperator.sol#L78`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/DataStorageOperator.sol#L78), [`AdaptiveFee.sol#L38`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/AdaptiveFee.sol#L38), [`AdaptiveFee.sol#L76`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/AdaptiveFee.sol#L76), [`DataStorage.sol#L56-L57`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.solL56-L57), [`DataStorage.sol#L80-L81`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L80-L81), [`DataStorage.sol#L133`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L133), [`DataStorage.sol#L156`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L156), [`DataStorage.sol#L223`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L223), [`DataStorage.sol#L231`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L231), [`DataStorage.sol#L251`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L251), [`DataStorage.sol#L253`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L253), [`DataStorage.sol#L255`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L255), [`DataStorage.sol#L265`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L265), [`DataStorage.sol#L274-L276`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L274-L276), [`DataStorage.sol#L360`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L360), [`DataStorage.sol#L376`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L376), [`DataStorage.sol#L408`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L408), [`DataStorage.sol#L414`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L414), [`DataStorage.sol#L417`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L417), [`PriceMovementMath.sol#L64`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/PriceMovementMath.sol#L64), [`PriceMovementMath.sol#L70`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/PriceMovementMath.sol#L70), [`PriceMovementMath.sol#L80`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/PriceMovementMath.sol#L80), [`PriceMovementMath.sol#L126`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/PriceMovementMath.sol#L126), [`PriceMovementMath.sol#L153`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/PriceMovementMath.sol#L153), [`PriceMovementMath.sol#L176`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/PriceMovementMath.sol#L176), [`TickManager.sol#L25`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TickManager.sol#L25), [`TickManager.sol#L37-L38`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TickManager.sol#L37-L38), [`TickManager.sol#L70`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TickManager.sol#L70), [`TickManager.sol#L128`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TickManager.sol#L128), [`TickTable.sol#L33-L39`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TickTable.sol#L33-L39), [`TokenDeltaMath.sol#L53`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TokenDeltaMath.sol#L53)

### Description
Max line length must be no more than 120 but many lines are extended past this length.

### Recommendation
Consider cutting down the line length below 120.

## [N-06] Function && Variable Naming Convention

### Context
[`AlgebraPoolFactory.sol#L116`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraFactory.sol#L116), [`AlgebraPoolFactory.sol#L122`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraFactory.sol#L122), [`AlgebraPool.sol#L70`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L70), [`AlgebraPool.sol#L74`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L74), [`AlgebraPool.sol#L403`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L403), [`AlgebraPoolDeployer.sol#L18-L19`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPoolDeployer.sol#L18-L19), [`DataStorageOperator.sol#L23-L24`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/DataStorageOperator.sol#L23-L24), [`DataStorageOperator.sol#L115`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/DataStorageOperator.sol#L115), [`Constants.sol#L5-L17`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/Constants.sol#L5-L17), [`DataStorage.sol#L13`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L13), [`DataStorage.sol#L32`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L32), [`DataStorage.sol#L49-L50`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L49-L50), [`DataStorage.sol#L66`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L66), [`DataStorage.sol#L94`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L94), [`DataStorage.sol#L105`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L105), [`DataStorage.sol#L148`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L148), [`TickTable.sol#L121`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TickTable.sol#L121), [`PoolState.sol#L27`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/base/PoolState.sol#L27)

### Description
The linked variables do not conform to the standard naming convention of Solidity whereby functions and variable names(local and state) utilize the `mixedCase` format unless variables are declared as `constant` in which case they utilize the `UPPER_CASE_WITH_UNDERSCORES` format. Private variables and functions should lead with an `_underscore`.

### Recommendation
Consider naming conventions utilized by the linked statements are adjusted to reflect the correct type of declaration according to the [Solidity style guide](https://docs.soliditylang.org/en/latest/style-guide.html).

## [N-07] Code Structure Deviates From Best-Practice

### Context
[`AlgebraPool.sol#L79`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L79), [`AlgebraPool.sol#L96`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L96), [`AlgebraPool.sol#L262`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L262), [`AlgebraPool.sol#L675`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L657), [`AlgebraPool.sol#L692`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/AlgebraPool.sol#L692), [`DataStorageOperator.sol#L18`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/DataStorageOperator.sol#L18), [`DataStorage.sol#L14`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/DataStorage.sol#L14), [`TickManager.sol#L78`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TickManager.sol#L78), [`TickTable.sol#L68`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/TickTable.sol#L68), [`PoolImmutables.sol#L29`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/base/PoolImmutables.sol#L29)

### Description
The best-practice layout for a contract should follow the following order: state variables, events, modifiers, constructor and functions. Function ordering helps readers identify which functions they can call and find constructor and fallback functions easier.  Functions should be grouped according to their visibility and ordered as: constructor, receive function (if exists), fallback function (if exists), external, public, internal, private. Functions should then further be ordered with view functions coming after the non-view labeled ones.

### Recommendation
Consider adopting recommended best-practice for code structure and layout.

## [N-08] Use Underscores for Number Literals

### Context
[`DataStorageOperator.sol#L15-16`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/DataStorageOperator.sol#L15-L16), [`Constants.sol#L17`](https://github.com/code-423n4/2022-09-quickswap/blob/main/src/core/contracts/libraries/Constants.sol#L17)

### Description
There are multiple occasions where certain numbers have been hardcoded, either in variables or in the code itself. Large numbers can become hard to read.

### Recommendation
Consider using underscores for number literals to improve its readability.

## [N-09] Unclear Revert Messages

### Context
[`All Contracts`](https://github.com/code-423n4/2022-09-quickswap/tree/main/src/core/contracts)

### Description
All revert messages across every contract are unclear which can lead to confusion. Unclear revert messages may cause misunderstandings on reverted transactions.

### Recommendation
Consider making revert messages more clear.

## [N-10] Older Version Pragma

### Context
[`All Contracts`](https://github.com/code-423n4/2022-09-quickswap/tree/main/src/core/contracts)

### Description
Using very old versions of Solidity prevents benefits of bug fixes and newer security checks. Using the latest versions might make contracts susceptible to undiscovered compiler bugs.

### Recommendation
Consider using the most recent version.

## [N-11] Missing or Incomplete NatSpec

### Context
[`All Contracts`](https://github.com/code-423n4/2022-09-quickswap/tree/main/src/core/contracts)

### Description
Some functions are missing @notice/@dev NatSpec comments for the function, @param for all/some of their parameters and @return for return values. Given that NatSpec is an important part of code documentation, this affects code comprehension, auditability and usability.

### Recommendation
Consider adding in full NatSpec comments for all functions to have complete code documentation for future use.



***

# Gas Optimizations

For this audit, 80 reports were submitted by wardens detailing gas optimizations. The [report highlighted below](https://github.com/code-423n4/2022-09-quickswap-findings/issues/278) by **IllIllI** received the top score from the judge.

*The following wardens also submitted reports: [c3phas](https://github.com/code-423n4/2022-09-quickswap-findings/issues/327), [RockingMiles](https://github.com/code-423n4/2022-09-quickswap-findings/issues/3), [trustindistrust](https://github.com/code-423n4/2022-09-quickswap-findings/issues/123), [0xSmartContract](https://github.com/code-423n4/2022-09-quickswap-findings/issues/182), [ReyAdmirado](https://github.com/code-423n4/2022-09-quickswap-findings/issues/206), [0xNazgul](https://github.com/code-423n4/2022-09-quickswap-findings/issues/244), [ajtra](https://github.com/code-423n4/2022-09-quickswap-findings/issues/191), [0xbepresent](https://github.com/code-423n4/2022-09-quickswap-findings/issues/283), [imare](https://github.com/code-423n4/2022-09-quickswap-findings/issues/194), [ch0bu](https://github.com/code-423n4/2022-09-quickswap-findings/issues/231), [0x1f8b](https://github.com/code-423n4/2022-09-quickswap-findings/issues/49), [rbserver](https://github.com/code-423n4/2022-09-quickswap-findings/issues/268), [slowmoses](https://github.com/code-423n4/2022-09-quickswap-findings/issues/146), [Tomo](https://github.com/code-423n4/2022-09-quickswap-findings/issues/65), [TomJ](https://github.com/code-423n4/2022-09-quickswap-findings/issues/230), [martin](https://github.com/code-423n4/2022-09-quickswap-findings/issues/90), [ChristianKuri](https://github.com/code-423n4/2022-09-quickswap-findings/issues/30), [B2](https://github.com/code-423n4/2022-09-quickswap-findings/issues/88), [zishansami](https://github.com/code-423n4/2022-09-quickswap-findings/issues/71), [kaden](https://github.com/code-423n4/2022-09-quickswap-findings/issues/108), [Awesome](https://github.com/code-423n4/2022-09-quickswap-findings/issues/122), [beardofginger](https://github.com/code-423n4/2022-09-quickswap-findings/issues/115), [brgltd](https://github.com/code-423n4/2022-09-quickswap-findings/issues/323), [RaymondFam](https://github.com/code-423n4/2022-09-quickswap-findings/issues/22), [saian](https://github.com/code-423n4/2022-09-quickswap-findings/issues/253), [SnowMan](https://github.com/code-423n4/2022-09-quickswap-findings/issues/171), [\_\_141345\_\_](https://github.com/code-423n4/2022-09-quickswap-findings/issues/199), [Bnke0x0](https://github.com/code-423n4/2022-09-quickswap-findings/issues/13), [oyc\_109](https://github.com/code-423n4/2022-09-quickswap-findings/issues/26), [Shinchan](https://github.com/code-423n4/2022-09-quickswap-findings/issues/274), [JC](https://github.com/code-423n4/2022-09-quickswap-findings/issues/306), [defsec](https://github.com/code-423n4/2022-09-quickswap-findings/issues/265), [HardlyCodeMan](https://github.com/code-423n4/2022-09-quickswap-findings/issues/92), [erictee](https://github.com/code-423n4/2022-09-quickswap-findings/issues/129), [Rolezn](https://github.com/code-423n4/2022-09-quickswap-findings/issues/17), [CodingNameKiki](https://github.com/code-423n4/2022-09-quickswap-findings/issues/301), [m\_Rassska](https://github.com/code-423n4/2022-09-quickswap-findings/issues/247), [ret2basic](https://github.com/code-423n4/2022-09-quickswap-findings/issues/72), [Deivitto](https://github.com/code-423n4/2022-09-quickswap-findings/issues/290), [Aymen0909](https://github.com/code-423n4/2022-09-quickswap-findings/issues/258), [gogo](https://github.com/code-423n4/2022-09-quickswap-findings/issues/286), [durianSausage](https://github.com/code-423n4/2022-09-quickswap-findings/issues/73), [V\_B](https://github.com/code-423n4/2022-09-quickswap-findings/issues/312), [dharma09](https://github.com/code-423n4/2022-09-quickswap-findings/issues/12), [aysha](https://github.com/code-423n4/2022-09-quickswap-findings/issues/218), [Tomio](https://github.com/code-423n4/2022-09-quickswap-findings/issues/291), [Saintcode\_](https://github.com/code-423n4/2022-09-quickswap-findings/issues/39), [emrekocak](https://github.com/code-423n4/2022-09-quickswap-findings/issues/20), [Ruhum](https://github.com/code-423n4/2022-09-quickswap-findings/issues/80), [Aeros](https://github.com/code-423n4/2022-09-quickswap-findings/issues/294), [bobirichman](https://github.com/code-423n4/2022-09-quickswap-findings/issues/161), [cryptonue](https://github.com/code-423n4/2022-09-quickswap-findings/issues/262), [delfin454000](https://github.com/code-423n4/2022-09-quickswap-findings/issues/233), [Diraco](https://github.com/code-423n4/2022-09-quickswap-findings/issues/140), [francoHacker](https://github.com/code-423n4/2022-09-quickswap-findings/issues/82), [karanctf](https://github.com/code-423n4/2022-09-quickswap-findings/issues/125), [medikko](https://github.com/code-423n4/2022-09-quickswap-findings/issues/326), [Noah3o6](https://github.com/code-423n4/2022-09-quickswap-findings/issues/153), [peiw](https://github.com/code-423n4/2022-09-quickswap-findings/issues/100), [0xRoxas](https://github.com/code-423n4/2022-09-quickswap-findings/issues/121), [Amithuddar](https://github.com/code-423n4/2022-09-quickswap-findings/issues/289), [bulej93](https://github.com/code-423n4/2022-09-quickswap-findings/issues/246), [Fitraldys](https://github.com/code-423n4/2022-09-quickswap-findings/issues/288), [lukris02](https://github.com/code-423n4/2022-09-quickswap-findings/issues/241), [mics](https://github.com/code-423n4/2022-09-quickswap-findings/issues/164), [rotcivegaf](https://github.com/code-423n4/2022-09-quickswap-findings/issues/98), [tnevler](https://github.com/code-423n4/2022-09-quickswap-findings/issues/235), [Waze](https://github.com/code-423n4/2022-09-quickswap-findings/issues/209), [0x5rings](https://github.com/code-423n4/2022-09-quickswap-findings/issues/190), [gianganhnguyen](https://github.com/code-423n4/2022-09-quickswap-findings/issues/67), [shark](https://github.com/code-423n4/2022-09-quickswap-findings/issues/64), [asutorufos](https://github.com/code-423n4/2022-09-quickswap-findings/issues/329), [fatherOfBlocks](https://github.com/code-423n4/2022-09-quickswap-findings/issues/57), [natzuu](https://github.com/code-423n4/2022-09-quickswap-findings/issues/318), [Olivierdem](https://github.com/code-423n4/2022-09-quickswap-findings/issues/238), [0xmatt](https://github.com/code-423n4/2022-09-quickswap-findings/issues/174), [ladboy233](https://github.com/code-423n4/2022-09-quickswap-findings/issues/52), [Mukund](https://github.com/code-423n4/2022-09-quickswap-findings/issues/14), and [zeesaw](https://github.com/code-423n4/2022-09-quickswap-findings/issues/48).*

## Gas Optimizations Summary

|        | Issue                                                                                          | Instances | Total Gas Saved |
| ------ | :--------------------------------------------------------------------------------------------- | :-------: | :-------------: |
| [G‑01] | State variables only set in the constructor should be declared `immutable`                     |     2     |       4194      |
| [G‑02] | Using `calldata` instead of `memory` for read-only arguments in `external` functions saves gas |     1     |       120       |
| [G‑03] | Using `storage` instead of `memory` for structs/arrays saves gas                               |     1     |       4200      |
| [G‑04] | Avoid contract existence checks by using low level calls                                       |     24    |       2400      |
| [G‑05] | State variables should be cached in stack variables rather than re-reading them from storage   |     7     |       679       |
| [G‑06] | `internal` functions only called once can be inlined to save gas                               |     2     |        40       |
| [G‑07] | `<array>.length` should not be looked up in every loop of a `for`-loop                         |     1     |        3        |
| [G‑08] | Use a more recent version of solidity                                                          |     13    |        -        |
| [G‑09] | Using `> 0` costs more gas than `!= 0` when used on a `uint` in a `require()` statement        |     6     |        36       |
| [G‑10] | `>=` costs less gas than `>`                                                                   |     2     |        6        |
| [G‑11] | `++i` costs less gas than `i++`, especially when it's used in `for`-loops (`--i`/`i--` too)    |     1     |        5        |
| [G‑12] | Splitting `require()` statements that use `&&` saves gas                                       |     6     |        18       |
| [G‑13] | Using `private` rather than `public` for constants, saves gas                                  |     1     |        -        |
| [G‑14] | Division by two should use bit shifting                                                        |     1     |        20       |
| [G‑15] | Use custom errors rather than `revert()`/`require()` strings to save gas                       |     32    |        -        |
| [G‑16] | Functions guaranteed to revert when called by normal users can be marked `payable`             |     17    |       357       |

Total: 117 instances over 16 issues with **12078 gas** saved

Gas totals use lower bounds of ranges and count two iterations of each `for`-loop. All values above are runtime, not deployment, values; deployment values are listed in the individual issue descriptions

## [G‑01] State variables only set in the constructor should be declared `immutable`

Avoids a Gsset (**20000 gas**) in the constructor, and replaces the first access in each transaction (Gcoldsload - **2100 gas**) and each access thereafter (Gwarmacces - **100 gas**) with a `PUSH32` (**3 gas**).

While `string`s are not value types, and therefore cannot be `immutable`/`constant` if not hard-coded outside of the constructor, the same behavior can be achieved by making the current contract `abstract` with `virtual` functions for the `string` accessors, and having a child contract override the functions with the hard-coded implementation-specific values.

*There are 2 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraPoolDeployer.sol

/// @audit owner (access)
27:       require(msg.sender == owner);

/// @audit owner (constructor)
32:       owner = msg.sender;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPoolDeployer.sol#L27>

## [G‑02] Using `calldata` instead of `memory` for read-only arguments in `external` functions saves gas

When a function with a `memory` array is called externally, the `abi.decode()` step has to use a for-loop to copy each index of the `calldata` to the `memory` index. **Each iteration of this for-loop costs at least 60 gas** (i.e. `60 * <mem_array>.length`). Using `calldata` directly, obliviates the need for such a loop in the contract code and runtime execution. Note that even if an interface defines a function as having `memory` arguments, it's still valid for implementation contracs to use `calldata` arguments instead.

If the array is passed to an `internal` function which passes the array to another internal function where the array is modified and therefore `memory` is used in the `external` call, it's still more gass-efficient to use `calldata` when the `external` function uses modifiers, since the modifiers may prevent the internal functions from being called. Structs have the same overhead as an array of length one

Note that I've also flagged instances where the function is `public` but can be marked as `external` since it's not called by the contract, and cases where a constructor is involved

*There is 1 instance of this issue:*

```solidity
File: src/core/contracts/DataStorageOperator.sol

/// @audit secondsAgos
88      function getTimepoints(
89        uint32 time,
90        uint32[] memory secondsAgos,
91        int24 tick,
92        uint16 index,
93        uint128 liquidity
94      )
95        external
96        view
97        override
98        onlyPool
99        returns (
100         int56[] memory tickCumulatives,
101         uint160[] memory secondsPerLiquidityCumulatives,
102         uint112[] memory volatilityCumulatives,
103:        uint256[] memory volumePerAvgLiquiditys

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/DataStorageOperator.sol#L88-L103>

## [G‑03] Using `storage` instead of `memory` for structs/arrays saves gas

When fetching data from a storage location, assigning the data to a `memory` variable causes all fields of the struct/array to be read from storage, which incurs a Gcoldsload (**2100 gas**) for *each* field of the struct/array. If the fields are read from the new memory variable, they incur an additional `MLOAD` rather than a cheap stack read. Instead of declearing the variable with the `memory` keyword, declaring the variable with the `storage` keyword and caching any fields that need to be re-read in stack variables, will be much cheaper, only incuring the Gcoldsload for the fields actually read. The only time it makes sense to read the whole struct/array into a `memory` variable, is if the full struct/array is being returned by the function, is being passed to a function that requires `memory`, or if the array/struct is being read from another `memory` array/struct

*There is 1 instance of this issue:*

```solidity
File: src/core/contracts/libraries/DataStorage.sol

397:      Timepoint memory last = _last;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/DataStorage.sol#L397>

## [G‑04] Avoid contract existence checks by using low level calls

Prior to 0.8.10 the compiler inserted extra code, including `EXTCODESIZE` (**100 gas**), to check for contract existence for external function calls. In more recent solidity versions, the compiler will not insert these checks if the external call has a return value. Similar behavior can be achieved in earlier versions by using low-level calls, since low level calls never check for contract existence

*There are 24 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraFactory.sol

/// @audit deploy()
69:       pool = IAlgebraPoolDeployer(poolDeployer).deploy(address(dataStorage), address(this), token0, token1);

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraFactory.sol#L69>

```solidity
File: src/core/contracts/AlgebraPool.sol

/// @audit owner()
55:       require(msg.sender == IAlgebraFactory(factory).owner());

/// @audit balanceOf()
71:       return IERC20Minimal(token0).balanceOf(address(this));

/// @audit balanceOf()
75:       return IERC20Minimal(token1).balanceOf(address(this));

/// @audit timepoints()
93:       return IDataStorageOperator(dataStorageOperator).timepoints(index);

/// @audit getTimepoints()
183:        IDataStorageOperator(dataStorageOperator).getTimepoints(

/// @audit algebraMintCallback()
453:        IAlgebraMintCallback(msg.sender).algebraMintCallback(amount0, amount1, data);

/// @audit getFee()
542:      newFee = IDataStorageOperator(dataStorageOperator).getFee(_time, _tick, _index, _liquidity);

/// @audit vaultAddress()
547:      address vault = IAlgebraFactory(factory).vaultAddress();

/// @audit write()
558:      return IDataStorageOperator(dataStorageOperator).write(timepointIndex, blockTimestamp, tick, liquidity, volumePerLiquidityInBlock);

/// @audit getSingleTimepoint()
577:      return IDataStorageOperator(dataStorageOperator).getSingleTimepoint(blockTimestamp, secondsAgo, startTick, timepointIndex, liquidityStart);

/// @audit algebraSwapCallback()
585:      IAlgebraSwapCallback(msg.sender).algebraSwapCallback(amount0, amount1, data);

/// @audit increaseCumulative()
753:          IAlgebraVirtualPool.Status _status = IAlgebraVirtualPool(activeIncentive).increaseCumulative(blockTimestamp);

/// @audit cross()
833:              IAlgebraVirtualPool(activeIncentive).cross(step.nextTick, zeroToOne);

/// @audit calculateVolumePerLiquidity()
880:        cache.volumePerLiquidityInBlock + IDataStorageOperator(dataStorageOperator).calculateVolumePerLiquidity(currentLiquidity, amount0, amount1)

/// @audit algebraFlashCallback()
916:      IAlgebraFlashCallback(msg.sender).algebraFlashCallback(fee0, fee1, data);

/// @audit vaultAddress()
918:      address vault = IAlgebraFactory(factory).vaultAddress();

/// @audit farmingAddress()
960:      require(msg.sender == IAlgebraFactory(factory).farmingAddress());

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L55>

```solidity
File: src/core/contracts/base/PoolImmutables.sol

/// @audit parameters()
30:       (dataStorageOperator, factory, token0, token1) = IAlgebraPoolDeployer(deployer).parameters();

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/base/PoolImmutables.sol#L30>

```solidity
File: src/core/contracts/DataStorageOperator.sol

/// @audit owner()
43:       require(msg.sender == factory || msg.sender == IAlgebraFactory(factory).owner());

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/DataStorageOperator.sol#L43>

```solidity
File: src/core/contracts/libraries/TokenDeltaMath.sol

/// @audit toInt256()
67:         ? getToken0Delta(priceLower, priceUpper, uint128(liquidity), true).toInt256()

/// @audit toInt256()
68:         : -getToken0Delta(priceLower, priceUpper, uint128(-liquidity), false).toInt256();

/// @audit toInt256()
82:         ? getToken1Delta(priceLower, priceUpper, uint128(liquidity), true).toInt256()

/// @audit toInt256()
83:         : -getToken1Delta(priceLower, priceUpper, uint128(-liquidity), false).toInt256();

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/TokenDeltaMath.sol#L67>

## [G‑05] State variables should be cached in stack variables rather than re-reading them from storage

The instances below point to the second+ access of a state variable within a function. Caching of a state variable replaces each Gwarmaccess (**100 gas**) with a much cheaper stack read. Other less obvious fixes/optimizations include having local memory caches of state variable structs, or having local caches of state variable contracts/addresses.

*There are 7 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraPool.sol

/// @audit totalFeeGrowth0Token on line 740
/// @audit totalFeeGrowth1Token on line 744
829:              cache.totalFeeGrowthB = zeroToOne ? totalFeeGrowth1Token : totalFeeGrowth0Token;

/// @audit liquidity on line 297
354:          uint128 liquidityBefore = liquidity;

/// @audit liquidity on line 736
/// @audit volumePerLiquidityInBlock on line 736
878:      (liquidity, volumePerLiquidityInBlock) = (

/// @audit activeIncentive on line 752
753:          IAlgebraVirtualPool.Status _status = IAlgebraVirtualPool(activeIncentive).increaseCumulative(blockTimestamp);

/// @audit activeIncentive on line 755
833:              IAlgebraVirtualPool(activeIncentive).cross(step.nextTick, zeroToOne);

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L829>

## [G‑06] `internal` functions only called once can be inlined to save gas

Not inlining costs **20 to 40 gas** because of two extra `JUMP` instructions and additional stack operations needed for function calls.

*There are 2 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraFactory.sol

122:    function computeAddress(address token0, address token1) internal view returns (address pool) {

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraFactory.sol#L122>

```solidity
File: src/core/contracts/AlgebraPool.sol

215     function _recalculatePosition(
216       Position storage _position,
217       int128 liquidityDelta,
218       uint256 innerFeeGrowth0Token,
219:      uint256 innerFeeGrowth1Token

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L215-L219>

## [G‑07] `<array>.length` should not be looked up in every loop of a `for`-loop

The overheads outlined below are *PER LOOP*, excluding the first loop

*   storage arrays incur a Gwarmaccess (**100 gas**)
*   memory arrays use `MLOAD` (**3 gas**)
*   calldata arrays use `CALLDATALOAD` (**3 gas**)

Caching the length changes each of these to a `DUP<N>` (**3 gas**), and gets rid of the extra `DUP<N>` needed to store the stack offset

*There is 1 instance of this issue:*

```solidity
File: src/core/contracts/libraries/DataStorage.sol

307:      for (uint256 i = 0; i < secondsAgos.length; i++) {

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/DataStorage.sol#L307>

## [G‑08] Use a more recent version of solidity

Use a solidity version of at least 0.8.0 to get overflow protection without `SafeMath`<br>
Use a solidity version of at least 0.8.2 to get simple compiler automatic inlining<br>
Use a solidity version of at least 0.8.3 to get better struct packing and cheaper multiple storage reads<br>
Use a solidity version of at least 0.8.4 to get custom errors, which are cheaper at deployment than `revert()/require()` strings<br>
Use a solidity version of at least 0.8.10 to have external calls skip contract existence checks if the external call has a return value<br>

*There are 13 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraFactory.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraFactory.sol#L2>

```solidity
File: src/core/contracts/AlgebraPoolDeployer.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPoolDeployer.sol#L2>

```solidity
File: src/core/contracts/AlgebraPool.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L2>

```solidity
File: src/core/contracts/base/PoolImmutables.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/base/PoolImmutables.sol#L2>

```solidity
File: src/core/contracts/base/PoolState.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/base/PoolState.sol#L2>

```solidity
File: src/core/contracts/DataStorageOperator.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/DataStorageOperator.sol#L2>

```solidity
File: src/core/contracts/libraries/AdaptiveFee.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/AdaptiveFee.sol#L2>

```solidity
File: src/core/contracts/libraries/Constants.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/Constants.sol#L2>

```solidity
File: src/core/contracts/libraries/DataStorage.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/DataStorage.sol#L2>

```solidity
File: src/core/contracts/libraries/PriceMovementMath.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/PriceMovementMath.sol#L2>

```solidity
File: src/core/contracts/libraries/TickManager.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/TickManager.sol#L2>

```solidity
File: src/core/contracts/libraries/TickTable.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/TickTable.sol#L2>

```solidity
File: src/core/contracts/libraries/TokenDeltaMath.sol

2:    pragma solidity =0.7.6;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/TokenDeltaMath.sol#L2>

## [G‑09] Using `> 0` costs more gas than `!= 0` when used on a `uint` in a `require()` statement

This change saves **[6 gas](https://aws1.discourse-cdn.com/business6/uploads/zeppelin/original/2X/3/363a367d6d68851f27d2679d10706cd16d788b96.png)** per instance. The optimization works until solidity version [0.8.13](https://gist.github.com/IllIllI000/bf2c3120f24a69e489f12b3213c06c94) where there is a regression in gas costs.

*There are 6 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraPool.sol

224:        require(currentLiquidity > 0, 'NP'); // Do not recalculate the empty ranges

434:      require(liquidityDesired > 0, 'IL');

469:      require(liquidityActual > 0, 'IIL2');

898:      require(_liquidity > 0, 'L');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L224>

```solidity
File: src/core/contracts/libraries/PriceMovementMath.sol

52:       require(price > 0);

53:       require(liquidity > 0);

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/PriceMovementMath.sol#L52>

## [G‑10] `>=` costs less gas than `>`

The compiler uses opcodes `GT` and `ISZERO` for solidity code that uses `>`, but only requires `LT` for `>=`, [which saves **3 gas**](https://gist.github.com/IllIllI000/3dc79d25acccfa16dee4e83ffdc6ffde)

*There are 2 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraPool.sol

498:      amount0 = amount0Requested > positionFees0 ? positionFees0 : amount0Requested;

499:      amount1 = amount1Requested > positionFees1 ? positionFees1 : amount1Requested;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L498>

## [G‑11] `++i` costs less gas than `i++`, especially when it's used in `for`-loops (`--i`/`i--` too)

Saves **5 gas per loop**

*There is 1 instance of this issue:*

```solidity
File: src/core/contracts/libraries/DataStorage.sol

307:      for (uint256 i = 0; i < secondsAgos.length; i++) {

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/DataStorage.sol#L307>

## [G‑12] Splitting `require()` statements that use `&&` saves gas

See [this issue](https://github.com/code-423n4/2022-01-xdefi-findings/issues/128) which describes the fact that there is a larger deployment gas cost, but with enough runtime calls, the change ends up being cheaper by **3 gas**

*There are 6 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraFactory.sol

110:      require(gamma1 != 0 && gamma2 != 0 && volumeGamma != 0, 'Gammas must be > 0');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraFactory.sol#L110>

```solidity
File: src/core/contracts/AlgebraPool.sol

739:          require(limitSqrtPrice < currentPrice && limitSqrtPrice > TickMath.MIN_SQRT_RATIO, 'SPL');

743:          require(limitSqrtPrice > currentPrice && limitSqrtPrice < TickMath.MAX_SQRT_RATIO, 'SPL');

953:      require((communityFee0 <= Constants.MAX_COMMUNITY_FEE) && (communityFee1 <= Constants.MAX_COMMUNITY_FEE));

968:      require(newLiquidityCooldown <= Constants.MAX_LIQUIDITY_COOLDOWN && liquidityCooldown != newLiquidityCooldown);

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L739>

```solidity
File: src/core/contracts/DataStorageOperator.sol

46:       require(_feeConfig.gamma1 != 0 && _feeConfig.gamma2 != 0 && _feeConfig.volumeGamma != 0, 'Gammas must be > 0');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/DataStorageOperator.sol#L46>

## [G‑13] Using `private` rather than `public` for constants, saves gas

If needed, the values can be read from the verified contract source code, or if there are multiple values there can be a single getter function that [returns a tuple](https://github.com/code-423n4/2022-08-frax/blob/90f55a9ce4e25bceed3a74290b854341d8de6afa/src/contracts/FraxlendPair.sol#L156-L178) of the values of all currently-public constants. Saves **3406-3606 gas** in deployment gas due to the compiler not having to create non-payable getter functions for deployment calldata, not having to store the bytes of the value outside of where it's used, and not adding another entry to the method ID table

*There is 1 instance of this issue:*

```solidity
File: src/core/contracts/libraries/DataStorage.sol

12:     uint32 public constant WINDOW = 1 days;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/DataStorage.sol#L12>

## [G‑14] Division by two should use bit shifting

`<x> / 2` is the same as `<x> >> 1`. While the compiler uses the `SHR` opcode to accomplish both, the version that uses division incurs an overhead of [**20 gas**](https://gist.github.com/IllIllI000/ec0e4e6c4f52a6bca158f137a3afd4ff) due to `JUMP`s to and from a compiler utility function that introduces checks which can be avoided by using `unchecked {}` around the division by two

*There is 1 instance of this issue:*

```solidity
File: src/core/contracts/libraries/AdaptiveFee.sol

88:       res += (xLowestDegree * gHighestDegree) / 2;

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/AdaptiveFee.sol#L88>

## [G‑15] Use custom errors rather than `revert()`/`require()` strings to save gas

Custom errors are available from solidity version 0.8.4. Custom errors save [**\~50 gas**](https://gist.github.com/IllIllI000/ad1bd0d29a0101b25e57c293b4b0c746) each time they're hit by [avoiding having to allocate and store the revert string](https://blog.soliditylang.org/2021/04/21/custom-errors/#errors-in-depth). Not defining the strings also save deployment gas

*There are 32 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraFactory.sol

109:      require(uint256(alpha1) + uint256(alpha2) + uint256(baseFee) <= type(uint16).max, 'Max fee exceeded');

110:      require(gamma1 != 0 && gamma2 != 0 && volumeGamma != 0, 'Gammas must be > 0');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraFactory.sol#L109>

```solidity
File: src/core/contracts/AlgebraPool.sol

60:       require(topTick < TickMath.MAX_TICK + 1, 'TUM');

61:       require(topTick > bottomTick, 'TLU');

62:       require(bottomTick > TickMath.MIN_TICK - 1, 'TLM');

194:      require(globalState.price == 0, 'AI');

224:        require(currentLiquidity > 0, 'NP'); // Do not recalculate the empty ranges

434:      require(liquidityDesired > 0, 'IL');

454:        if (amount0 > 0) require((receivedAmount0 = balanceToken0() - receivedAmount0) > 0, 'IIAM');

455:        if (amount1 > 0) require((receivedAmount1 = balanceToken1() - receivedAmount1) > 0, 'IIAM');

469:      require(liquidityActual > 0, 'IIL2');

474:        require((amount0 = uint256(amount0Int)) <= receivedAmount0, 'IIAM2');

475:        require((amount1 = uint256(amount1Int)) <= receivedAmount1, 'IIAM2');

608:        require(balance0Before.add(uint256(amount0)) <= balanceToken0(), 'IIA');

614:        require(balance1Before.add(uint256(amount1)) <= balanceToken1(), 'IIA');

636:      require(globalState.unlocked, 'LOK');

641:        require((amountRequired = int256(balanceToken0().sub(balance0Before))) > 0, 'IIA');

645:        require((amountRequired = int256(balanceToken1().sub(balance1Before))) > 0, 'IIA');

731:        require(unlocked, 'LOK');

733:        require(amountRequired != 0, 'AS');

739:          require(limitSqrtPrice < currentPrice && limitSqrtPrice > TickMath.MIN_SQRT_RATIO, 'SPL');

743:          require(limitSqrtPrice > currentPrice && limitSqrtPrice < TickMath.MAX_SQRT_RATIO, 'SPL');

898:      require(_liquidity > 0, 'L');

921:      require(balance0Before.add(fee0) <= paid0, 'F0');

935:      require(balance1Before.add(fee1) <= paid1, 'F1');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L60>

```solidity
File: src/core/contracts/base/PoolState.sol

41:       require(globalState.unlocked, 'LOK');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/base/PoolState.sol#L41>

```solidity
File: src/core/contracts/DataStorageOperator.sol

27:       require(msg.sender == pool, 'only pool can call this');

45:       require(uint256(_feeConfig.alpha1) + uint256(_feeConfig.alpha2) + uint256(_feeConfig.baseFee) <= type(uint16).max, 'Max fee exceeded');

46:       require(_feeConfig.gamma1 != 0 && _feeConfig.gamma2 != 0 && _feeConfig.volumeGamma != 0, 'Gammas must be > 0');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/DataStorageOperator.sol#L27>

```solidity
File: src/core/contracts/libraries/DataStorage.sol

238:      require(lteConsideringOverflow(self[oldestIndex].blockTimestamp, target, time), 'OLD');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/DataStorage.sol#L238>

```solidity
File: src/core/contracts/libraries/TickManager.sol

96:       require(liquidityTotalAfter < Constants.MAX_LIQUIDITY_PER_TICK + 1, 'LO');

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/TickManager.sol#L96>

```solidity
File: src/core/contracts/libraries/TickTable.sol

15:       require(tick % Constants.TICK_SPACING == 0, 'tick is not spaced'); // ensure that the tick is spaced

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/libraries/TickTable.sol#L15>

## [G‑16] Functions guaranteed to revert when called by normal users can be marked `payable`

If a function modifier such as `onlyOwner` is used, the function will revert if a normal user tries to pay the function. Marking the function as `payable` will lower the gas cost for legitimate callers because the compiler will not include checks for whether a payment was provided. The extra opcodes avoided are
`CALLVALUE`(2),`DUP1`(3),`ISZERO`(3),`PUSH2`(3),`JUMPI`(10),`PUSH1`(3),`DUP1`(3),`REVERT`(0),`JUMPDEST`(1),`POP`(2), which costs an average of about **21 gas per call** to the function, in addition to the extra deployment cost

*There are 17 instances of this issue:*

```solidity
File: src/core/contracts/AlgebraFactory.sol

77:     function setOwner(address _owner) external override onlyOwner {

84:     function setFarmingAddress(address _farmingAddress) external override onlyOwner {

91:     function setVaultAddress(address _vaultAddress) external override onlyOwner {

98      function setBaseFeeConfiguration(
99        uint16 alpha1,
100       uint16 alpha2,
101       uint32 beta1,
102       uint32 beta2,
103       uint16 gamma1,
104       uint16 gamma2,
105       uint32 volumeBeta,
106       uint16 volumeGamma,
107       uint16 baseFee
108:    ) external override onlyOwner {

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraFactory.sol#L77>

```solidity
File: src/core/contracts/AlgebraPoolDeployer.sol

36:     function setFactory(address _factory) external override onlyOwner {

44      function deploy(
45        address dataStorage,
46        address _factory,
47        address token0,
48        address token1
49:     ) external override onlyFactory returns (address pool) {

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPoolDeployer.sol#L36>

```solidity
File: src/core/contracts/AlgebraPool.sol

103     function getInnerCumulatives(int24 bottomTick, int24 topTick)
104       external
105       view
106       override
107       onlyValidTicks(bottomTick, topTick)
108       returns (
109         int56 innerTickCumulative,
110         uint160 innerSecondsSpentPerLiquidity,
111:        uint32 innerSecondsSpent

416     function mint(
417       address sender,
418       address recipient,
419       int24 bottomTick,
420       int24 topTick,
421       uint128 liquidityDesired,
422       bytes calldata data
423     )
424       external
425       override
426       lock
427       onlyValidTicks(bottomTick, topTick)
428       returns (
429         uint256 amount0,
430         uint256 amount1,
431:        uint128 liquidityActual

513     function burn(
514       int24 bottomTick,
515       int24 topTick,
516       uint128 amount
517:    ) external override lock onlyValidTicks(bottomTick, topTick) returns (uint256 amount0, uint256 amount1) {

952:    function setCommunityFee(uint8 communityFee0, uint8 communityFee1) external override lock onlyFactoryOwner {

967:    function setLiquidityCooldown(uint32 newLiquidityCooldown) external override onlyFactoryOwner {

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/AlgebraPool.sol#L103-L111>

```solidity
File: src/core/contracts/DataStorageOperator.sol

37:     function initialize(uint32 time, int24 tick) external override onlyPool {

53      function getSingleTimepoint(
54        uint32 time,
55        uint32 secondsAgo,
56        int24 tick,
57        uint16 index,
58        uint128 liquidity
59      )
60        external
61        view
62        override
63        onlyPool
64        returns (
65          int56 tickCumulative,
66          uint160 secondsPerLiquidityCumulative,
67          uint112 volatilityCumulative,
68:         uint256 volumePerAvgLiquidity

88      function getTimepoints(
89        uint32 time,
90        uint32[] memory secondsAgos,
91        int24 tick,
92        uint16 index,
93        uint128 liquidity
94      )
95        external
96        view
97        override
98        onlyPool
99        returns (
100         int56[] memory tickCumulatives,
101         uint160[] memory secondsPerLiquidityCumulatives,
102         uint112[] memory volatilityCumulatives,
103:        uint256[] memory volumePerAvgLiquiditys

110     function getAverages(
111       uint32 time,
112       int24 tick,
113       uint16 index,
114       uint128 liquidity
115:    ) external view override onlyPool returns (uint112 TWVolatilityAverage, uint256 TWVolumePerLiqAverage) {

120     function write(
121       uint16 index,
122       uint32 blockTimestamp,
123       int24 tick,
124       uint128 liquidity,
125       uint128 volumePerLiquidity
126:    ) external override onlyPool returns (uint16 indexUpdated) {

150     function getFee(
151       uint32 _time,
152       int24 _tick,
153       uint16 _index,
154       uint128 _liquidity
155:    ) external view override onlyPool returns (uint16 fee) {

```

<https://github.com/code-423n4/2022-09-quickswap/blob/15ea643c85ed936a92d2676a7aabf739b210af39/src/core/contracts/DataStorageOperator.sol#L37>



***

# Disclosures

C4 is an open organization governed by participants in the community.

C4 Audits incentivize the discovery of exploits, vulnerabilities, and bugs in smart contracts. Security researchers are rewarded at an increasing rate for finding higher-risk issues. Audit submissions are judged by a knowledgeable security researcher and solidity developer and disclosed to sponsoring developers. C4 does not conduct formal verification regarding the provided code but instead provides final verification.

C4 does not provide any guarantee or warranty regarding the security of this project. All smart contract software should be used at the sole risk and responsibility of users.
