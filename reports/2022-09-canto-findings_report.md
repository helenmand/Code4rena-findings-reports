---
sponsor: "Canto"
slug: "2022-09-canto"
date: "2023-03-31"
title: "Canto Dex Oracle contest"
findings: "https://github.com/code-423n4/2022-09-canto-findings/issues"
contest: 159
---

# Overview

## About C4

Code4rena (C4) is an open organization consisting of security researchers, auditors, developers, and individuals with domain expertise in smart contracts.

A C4 audit contest is an event in which community participants, referred to as Wardens, review, audit, or analyze smart contract logic in exchange for a bounty provided by sponsoring projects.

During the audit contest outlined in this document, C4 conducted an analysis of the Canto Dex Oracle smart contract system written in Solidity. The audit contest took place between September 7—September 8 2022.

## Wardens

70 Wardens contributed reports to the Canto Dex Oracle contest:

  1. Critical
  1. [csanuragjain](https://twitter.com/csanuragjain)
  1. [Respx](https://twitter.com/RespxR)
  1. linmiaomiao
  1. [hickuphh3](https://twitter.com/HickupH)
  1. \_\_141345\_\_
  1. sorrynotsorry
  1. [Jeiwan](https://jeiwan.net)
  1. SinceJuly
  1. [Chom](https://chom.dev)
  1. [0xSmartContract](https://twitter.com/0xSmartContract)
  1. cccz
  1. V\_B (Barichek and vlad\_bochok)
  1. [0xNazgul](https://twitter.com/0xNazgul)
  1. 0xSky
  1. CertoraInc (egjlmn1, [OriDabush](https://twitter.com/ori_dabush), ItayG, shakedwinder, and RoiEvenHaim)
  1. [Deivitto](https://twitter.com/Deivitto)
  1. [fatherOfBlocks](https://twitter.com/father0fBl0cks)
  1. [hansfriese](https://twitter.com/hansfriese)
  1. [oyc\_109](https://twitter.com/andyfeili)
  1. rbserver
  1. [rokinot](twitter.com/rokinot)
  1. [Tomo](https://tom-sol.notion.site/Who-am-I-3b4dc28e77b647eb90794735a94dd38e)
  1. 0xhunter
  1. [BipinSah](https://twitter.com/BipinSah745)
  1. [m\_Rassska](https://t.me/Road220)
  1. [prasantgupta52](https://twitter.com/prasantgupta52)
  1. [Rohan16](https://twitter.com/rohan16___)
  1. [Sm4rty](https://twitter.com/Sm4rty_)
  1. 0x040
  1. 0x1f8b
  1. 0x52
  1. 0xA5DF
  1. [a12jmx](https://twitter.com/a12jmx)
  1. ajtra
  1. ak1
  1. Bnke0x0
  1. [Bronicle](https://twitter.com/Cryptonicle1)
  1. codexploder
  1. CodingNameKiki
  1. cryptphi
  1. Diraco
  1. [Dravee](https://twitter.com/BowTiedDravee)
  1. erictee
  1. EthLedger
  1. [gogo](https://www.linkedin.com/in/georgi-nikolaev-georgiev-978253219)
  1. hake
  1. [ignacio](https://twitter.com/0xheynacho)
  1. [IgnacioB](https://twitter.com/AdonaiR6)
  1. [JansenC](https://www.linkedin.com/in/jansen-moreira/?locale&#x3D;en_US)
  1. [JC](https://twitter.com/sm4rtcontr4ct)
  1. lukris02
  1. ontofractal
  1. p\_crypt0
  1. pashov
  1. peritoflores
  1. R2
  1. [rajatbeladiya](https://twitter.com/rajat_beladiya)
  1. RaymondFam
  1. ReyAdmirado
  1. Rolezn
  1. rvierdiiev
  1. tnevler
  1. [TomJ](https://mobile.twitter.com/tomj_bb)
  1. Yiko

This contest was judged by [0xean](https://github.com/0xean).

Final report assembled by [itsmetechjay](https://twitter.com/itsmetechjay).

# Summary

The C4 analysis yielded an aggregated total of 7 unique vulnerabilities. Of these vulnerabilities, 1 received a risk rating in the category of HIGH severity and 6 received a risk rating in the category of MEDIUM severity.

Additionally, C4 analysis included 51 reports detailing issues with a risk rating of LOW severity or non-critical.

All of the issues presented here are linked back to their original finding.

# Scope

The code under review can be found within the [C4 Canto Dex Oracle contest repository](https://github.com/code-423n4/2022-09-canto), and is composed of 2 smart contracts written in the Solidity programming language and includes 2,001 lines of Solidity code.

# Severity Criteria

C4 assesses the severity of disclosed vulnerabilities based on three primary risk categories: high, medium, and low/non-critical.

High-level considerations for vulnerabilities span the following key areas when conducting assessments:

- Malicious Input Handling
- Escalation of privileges
- Arithmetic
- Gas use

For more information regarding the severity criteria referenced throughout the submission review process, please refer to the documentation provided on [the C4 website](https://code4rena.com), specifically our section on [Severity Categorization](https://docs.code4rena.com/awarding/judging-criteria/severity-categorization).

# High Risk Findings (1)
## [[H-01] Hardcoded USD pegs can be broken](https://github.com/code-423n4/2022-09-canto-findings/issues/73)
*Submitted by hickuphh3, also found by \_\_141345\_\_, Critical, linmiaomiao, and sorrynotsorry*

The prices of USDC and USDT, which (I assume) are the underlying tokens of `cUSDC` and `cUSDT`, have been hardcoded to parity. Such practices are highly discouraged because while the likelihood of either stablecoin de-pegging is low, it is not zero.

Because of the UST debacle, the [price of USDT dropped to `$0.95`](https://www.cnbc.com/2022/05/12/tether-usdt-stablecoin-drops-below-1-peg.html) before making a recovery.

### Impact

Here is an example of how [a lending protocol on Fantom was affected by such a depeg event because they hardcoded the value](\[https://cryptoslate.com/scream-protocol-losses-millions-to-stablecoin-depeg/]\(https://cryptoslate.com/scream-protocol-losses-millions-to-stablecoin-depeg/\)).

To quote philosopher George Santayana, *“Those who cannot remember the past are condemned to repeat it.”*

### Recommended Mitigation Steps

Consider using a price feed by trusted and established oracle providers like Chainlink, Band Protocol or Flux. The USDC/NOTE or USDT/NOTE price feed may be used as well, but NOTE has its own volatility concerns.


***

 
# Medium Risk Findings (6)
## [[M-01] unbounded loop length dos ](https://github.com/code-423n4/2022-09-canto-findings/issues/8)
*Submitted by 0xhunter, also found by BipinSah, fatherOfBlocks, m\_Rassska, oyc\_109, prasantgupta52, Rohan16, rokinot, Sm4rty, and Tomo*

Loops that do not have a fixed number of iterations, for example, loops that depend on storage values, have to be used carefully: Due to the block gas limit, transactions can only consume a certain amount of gas. Either explicitly or just due to normal operation, the number of iterations in a loop can grow beyond the block gas limit which can cause the complete contract to be stalled at a certain point.

By calling createPair function a pair will be pushed to `allPairs` array , an admin can call setPeriodSize function and set newPeriod for every pairs in `allpair` array , however by spamming createPair function the loop in setPeriodSize function may revert in case of hitting gas limit of the network . since there is no way to remove `allPairs` or decrease their length in setPeriodSize function , its possible to totally make it impossible to call the setPeriodSize  function.

In order to fix the issue setPeriodSize  function has to be able to become executed in multiple times in case of facing gas limit.

**[nivasan1 (Canto) disagreed wtih severity and commented](https://github.com/code-423n4/2022-09-canto-findings/issues/8#issuecomment-1241184600):**
 > Given that it is not expected for admin to change the period size in the router often, we do not consider this a high-risk vulnerability. This would also cost an infinite amount of Canto if orchestrated by a single user.

**[0xean (judge) decreased severity to Medium and commented](https://github.com/code-423n4/2022-09-canto-findings/issues/8#issuecomment-1247241501):**
 > I am not sure the frequency that this is set to be used matter, it does lead to the functionality being lost. However, I do not see it leading to a loss of user funds, so will downgrade to a medium severity. 
> 
> `This would also cost an infinite amt of Canto if orchestrated by a single user` <- I am also not sure I understand this point.  Can you explain further?  What are the transaction gas limits set on this network? 

**[nivasan1 (Canto) commented](https://github.com/code-423n4/2022-09-canto-findings/issues/8#issuecomment-1276626865):**
 > @0xean, the method mentioned requires admin privileges to call it. As such, in order for an address that isn't timelock to access this method a malicious governance proposal must be passed to call the method from timelock, or to pass governance privileges to the malicious address.
> Secondly, the malicious user would have to spend a significant amount of Canto in deploying and adding sufficient liquidity to the contracts desired.
> As such, the risk-rewards for this action makes it unclear why any user would attempt to do this. 

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-canto-findings/issues/8#issuecomment-1276874183):**
 > I don't think this is  necessarily an attack vector, simply a way that the intended logic of the contracts could fail.  If Canto is wildly successful there could be sufficient pairs that this would fail, I think Medium is a reasonable severity. 
> 



***

## [[M-02] Calculated `token0TVL` may be zero under certain scenarios](https://github.com/code-423n4/2022-09-canto-findings/issues/41)
*Submitted by hickuphh3, also found by 0xNazgul, 0xSky, CertoraInc, Deivitto, hansfriese, Jeiwan, linmiaomiao, rbserver, and SinceJuly*

```solidity
uint token0TVL = assetReserves[i] * (prices[i] / decimals);
```

Because of the brackets, the division of `prices[i] / decimals` is executed before multiplication, causing `token0TVL` to potentially be zero.

### Proof of Concept

Add the following test in `oracle.test.ts`. Note: `getPriceLP()` should have its visibility changed from internal to public as the test relies on it.

To summarise what the test is doing, a stablecoin of 24 decimals is deployed, whose address will be greater than the `note` address so that `token0 = note`. It will enter the following case:

```solidity
if (pair.stable()) { // stable pairs will be priced in terms of Note
  if (token0 == note) { //token0 is the unit, token1 will be priced with respect to this asset initially
      decimals = 10 ** (erc20(token1).decimals()); // we must normalize the price of token1 to 18 decimals
      prices = pair.sample(token1, decimals, 8, 1);
      (unitReserves, assetReserves) = pair.sampleReserves(8, 1);
```

such that the `prices`’s denomination is smaller than the stablecoin’s decimals of 24.

To see the difference in test results, apply the recommended fix after running the test once. In essence, the LP’s price will double from `999500000001499` to `1999999998838589`, which is expected since the LP token should be worth the combined value of both stablecoins.

```solidity
it.only("will have 0 token0TVL", async () => {
  // NOTE: change getPriceLP() from internal to public so that function can be called
  let tokenFactory = await ethers.getContractFactory("ERC20", dep)
  let stablecoin = await tokenFactory.deploy("STABLE","STABLE",ethers.utils.parseUnits("100000", "24"), 24)
  await stablecoin.deployed()
  // we want note to be token0
  // redeploy till it is
  while (stablecoin.address < note.address) {
      stablecoin = await tokenFactory.deploy("STABLE","STABLE",ethers.utils.parseUnits("100000", "24"), 24)
      await stablecoin.deployed()
  }
  // give token approvals to router
  let noteIn = ethers.utils.parseUnits("10000", "18")
  let stableIn = ethers.utils.parseUnits("10000", "24")
  await (await note.approve(router.address, ethers.constants.MaxUint256)).wait()
  await (await stablecoin.approve(router.address, ethers.constants.MaxUint256)).wait()

  // borrow note
  await (await comptroller._supportMarket(cUsdc.address)).wait()
  // set collateral factors for cCanto 
  await (await comptroller._setCollateralFactor(cUsdc.address, ethers.utils.parseUnits("0.9", "18"))).wait()
  // borrow note against usdc 
  await (await comptroller.enterMarkets([cUsdc.address, cNote.address])).wait()
  await (await usdc.approve(cUsdc.address, ethers.utils.parseUnits("1000"))).wait()
  // supply usdc
  await (await cUsdc.mint(ethers.utils.parseUnits("100000000", "6"))).wait()
  // borrow note
  await (await cNote.borrow(ethers.utils.parseUnits("9000000", "18"))).wait()

  // add liquidity
  await (await router.addLiquidity(
      note.address,
      stablecoin.address,
      true,
      noteIn,
      stableIn,
      0,
      0,
      dep.address,
      9999999999,
      )).wait()
  // get pair address
  let pairAddr = await factory.getPair(note.address, stablecoin.address, true)
  pair = await ethers.getContractAt("BaseV1Pair", pairAddr)

  //set period size to zero for instant observations
  await (await factory.setPeriodSize(0)).wait()

  // swap 10 times for price observations
  for(var i = 0; i < 10; i++) {
      if (i % 2) {
          //swap 0.01 note for stable
          await (await router.swapExactTokensForTokensSimple(
              ethers.utils.parseUnits("10", "18"),
              0,
              note.address,
              stablecoin.address,
              true,
              dep.address,
              9999999999999
          )).wait()
      } else {
          //swap stable for note
          await (await router.swapExactTokensForTokensSimple(
              ethers.utils.parseUnits("10", "24"),
              0,
              stablecoin.address,
              note.address,
              true,
              dep.address,
              9999999999999
          )).wait()
      }
  }
  // check lpToken price
  // Actual price calculated is 999500000001499
  // But expected price (after removing brackets) is 1999999998838589
  console.log((await router.getPriceLP(pairAddr)).toString());
});
```

### Recommended Mitigation Steps

```diff
- uint token0TVL = assetReserves[i] * (prices[i] / decimals);
+ uint token0TVL = assetReserves[i] * prices[i] / decimals;
```

**[nivasan1 (Canto) confirmed](https://github.com/code-423n4/2022-09-canto-findings/issues/41)** 

**[0xean (judge) decreased severity to Medium](https://github.com/code-423n4/2022-09-canto-findings/issues/41)** 



***

## [[M-03] Hackers can deploy token with respective name as the stable one to impersonate the stable token](https://github.com/code-423n4/2022-09-canto-findings/issues/24)
*Submitted by Chom, also found by 0xSmartContract, cccz, Jeiwan, linmiaomiao, SinceJuly, and V\_B*

Hackers can deploy tokens with respective names as the stable ones to impersonate the stable token. Then hackers can get profit from the malicious price oracle.

### Proof of Concept

            string memory symbol = ctoken.symbol();
            if (compareStrings(symbol, "cCANTO")) {
                underlying = address(wcanto);
                return getPriceNote(address(wcanto), false);
            } else {
                underlying = address(ICErc20(address(ctoken)).underlying()); // We are getting the price for a CErc20 lending market
            }
            //set price statically to 1 when the Comptroller is retrieving Price
            if (compareStrings(symbol, "cNOTE")) { // note in terms of note will always be 1 
                return 1e18; // Stable coins supported by the lending market are instantiated by governance and their price will always be 1 note
            } 
            else if (compareStrings(symbol, "cUSDT") && (msg.sender == Comptroller )) {
                uint decimals = erc20(underlying).decimals();
                return 1e18 * 1e18 / (10 ** decimals); //Scale Price as a mantissa to maintain precision in comptroller
            } 
            else if (compareStrings(symbol, "cUSDC") && (msg.sender == Comptroller)) {
                uint decimals = erc20(underlying).decimals();
                return 1e18 * 1e18 / (10 ** decimals); //Scale Price as a mantissa to maintain precision in comptroller
            }

If hackers or malicious admin deploy a non-stable token but has "cNOTE", "cUSDT", or "cUSDC" as symbols, these tokens will act as a stable token while in fact, it isn't.

### Recommended Mitigation Steps

Use fixed address whitelisting instead for example `if (address(ctoken) == cUSDC_address) ...` where `cUSDC_address` is an immutable variable set on the constructor.

**[tkkwon1998 (Canto) disputed and commented](https://github.com/code-423n4/2022-09-canto-findings/issues/24#issuecomment-1241209615):**
 > The warden is saying that malicious parties could deploy a token with the same name to impersonate other tokens, but that these tokens will use the same pricing methodology as the token it is impersonating.
> 
> However, as this is an open EVM, anyone could deploy any token name with any underlying price method. I fail to see how this would be an issue, since everything is open source and users can see what they are doing. 

**[0xean (judge) commented](https://github.com/code-423n4/2022-09-canto-findings/issues/24#issuecomment-1247244929):**
 > What is the benefit the sponsor is trying to achieve by comparing a non unique string compared to a unique address? 
> 
> While everything is open source, it does seem like this is a pretty bad design choice when compared to the alternative solutions. 

**[nivasan1 (Canto) commented](https://github.com/code-423n4/2022-09-canto-findings/issues/24#issuecomment-1274049849):**
 > @0xean, the design choice presented here prevents from having multiple dependencies in the initialization of the oracle. Furthermore, the tokens that are referenced here must be supported by governance, so to override the actual prices would require a >51% voting power. As such, even if the exploit exists it is essentially impossible. As such, we do not believe that this is a high / med -risk issue.

**[0xean (judge) decreased severity to Medium and commented](https://github.com/code-423n4/2022-09-canto-findings/issues/24#issuecomment-1276877684):**
 > Will downgrade to Medium as there are several external factors for this to become an issue. 



***

## [[M-04] Period Size not updated on creating new Pair](https://github.com/code-423n4/2022-09-canto-findings/issues/76)
*Submitted by csanuragjain*

The period size is not updated to current while creating a new pair. This means even if period size has been reduced from default value, this new pair will still point to the higher default value.

### Proof of Concept

1.  Assume Pair P1,P2 exists in BaseV1Factory with default period size as 1800

2.  Admin decides to decrease the period size to 900 using [setPeriodSize](https://github.com/code-423n4/2022-09-canto/blob/main/src/Swap/BaseV1-core.sol#L560) function

<!---->

    function setPeriodSize(uint newPeriod) external {
            require(msg.sender == admin);
            require(newPeriod <= MaxPeriod);

            for (uint i; i < allPairs.length; ) {
                BaseV1Pair(allPairs[i]).setPeriodSize(newPeriod);
                unchecked {++i;}
            }
        }

3.  This changes period size of P1, P2 to 900

4.  Admin creates a new Pair P3 using [createPair](https://github.com/code-423n4/2022-09-canto/blob/main/src/Swap/BaseV1-core.sol#L598) function

<!---->

    function createPair(address tokenA, address tokenB, bool stable) external returns (address pair) {
            require(tokenA != tokenB, "IA"); // BaseV1: IDENTICAL_ADDRESSES
            (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);
            require(token0 != address(0), "ZA"); // BaseV1: ZERO_ADDRESS
            require(getPair[token0][token1][stable] == address(0), "PE"); // BaseV1: PAIR_EXISTS - single check is sufficient
            bytes32 salt = keccak256(abi.encodePacked(token0, token1, stable)); // notice salt includes stable as well, 3 parameters
            (_temp0, _temp1, _temp) = (token0, token1, stable);
            pair = address(new BaseV1Pair{salt:salt}());
            getPair[token0][token1][stable] = pair;
            getPair[token1][token0][stable] = pair; // populate mapping in the reverse direction
            allPairs.push(pair);
            isPair[pair] = true;
            emit PairCreated(token0, token1, stable, pair, allPairs.length);
        }

5.  A new Pair is created but the period size is not updated which means P3's period size will be 1800 instead of 900 which is incorrect

### Recommended Mitigation Steps

Add a new variable which stores the updated period size. Once a pair is created, update its period size using this new variable:

    uint periodSizeUpdated=1800;

    function setPeriodSize(uint newPeriod) external {
            ...
    periodSizeUpdated=newPeriod;
        }

    function createPair(address tokenA, address tokenB, bool stable) external returns (address pair) {
    ...
    BaseV1Pair(pair).setPeriodSize(newPeriod);

    }

**[nivasan1 (Canto) confirmed](https://github.com/code-423n4/2022-09-canto-findings/issues/76)**



***

## [[M-05]  `getUnderlyingPrice()` should return `0` when errored](https://github.com/code-423n4/2022-09-canto-findings/issues/93)
*Submitted by Critical*

The `Comptroller` is expecting `oracle.getUnderlyingPrice` to return `0` for errors (Compound style returns, no revert). The current implementation will throw errors, resulting in the consumer of the oracle getting unexpected errors.

### Proof of Concept

```solidity
function getUnderlyingPrice(CToken ctoken) external override view returns(uint) {
         address underlying;
        { //manual scope to pop symbol off of stack
        string memory symbol = ctoken.symbol();
        if (compareStrings(symbol, "cCANTO")) {
            underlying = address(wcanto);
            return getPriceNote(address(wcanto), false);
        } else {
            underlying = address(ICErc20(address(ctoken)).underlying()); // We are getting the price for a CErc20 lending market
        }
        //set price statically to 1 when the Comptroller is retrieving Price
        if (compareStrings(symbol, "cNOTE")) { // note in terms of note will always be 1 
            return 1e18; // Stable coins supported by the lending market are instantiated by governance and their price will always be 1 note
        } 
        else if (compareStrings(symbol, "cUSDT") && (msg.sender == Comptroller )) {
            uint decimals = erc20(underlying).decimals();
            return 1e18 * 1e18 / (10 ** decimals); //Scale Price as a mantissa to maintain precision in comptroller
        } 
        else if (compareStrings(symbol, "cUSDC") && (msg.sender == Comptroller)) {
            uint decimals = erc20(underlying).decimals();
            return 1e18 * 1e18 / (10 ** decimals); //Scale Price as a mantissa to maintain precision in comptroller
        }
        }
        
        if (isPair(underlying)) { // this is an LP Token
            return getPriceLP(IBaseV1Pair(underlying));
        }
        // this is not an LP Token
        else {
            if (isStable[underlying]) {
                return getPriceNote(underlying, true); // value has already been scaled
            }

            return getPriceCanto(underlying) * getPriceNote(address(wcanto), false) / 1e18;
        }   
    }
```

The `Comptroller` is expecting `oracle.getUnderlyingPrice` to return `0` for errors (Compound style returns, no revert).

However, the current implementation will revert when errored:

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L549-L593>

```solidity
function getPriceLP(IBaseV1Pair pair) internal view returns(uint) {
        uint[] memory supply = pair.sampleSupply(8, 1);
        uint[] memory prices; 
        uint[] memory unitReserves; 
        uint[] memory assetReserves; 
        address token0 = pair.token0();
        address token1 = pair.token1();
        uint decimals;
```

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L271-L289>

```solidity
function sampleSupply(uint points, uint window) public view returns (uint[] memory) {
        uint[] memory _totalSupply = new uint[](points);
        
        uint lastIndex = observations.length-1;
        require(lastIndex >= points * window, "PAIR::NOT READY FOR PRICING");
        uint i = lastIndex - (points * window); // point from which to begin the sample
        uint nextIndex = 0;
        uint index = 0;
        uint timeElapsed;

        for(; i < lastIndex; i+=window) {
            nextIndex = i + window;
            timeElapsed = observations[nextIndex].timestamp - observations[i].timestamp;
            _totalSupply[index] = (observations[nextIndex].totalSupplyCumulative - observations[i].totalSupplyCumulative) / timeElapsed;
            index = index + 1;
        }

        return _totalSupply;
    }
```

### Recommended Mitigation Steps

Consider using `try catch` and return 0 when errored.

**[nivasan1 (Canto) confirmed](https://github.com/code-423n4/2022-09-canto-findings/issues/93)**


***

## [[M-06] System is Vulnerable to Downtime and has no Checks for it](https://github.com/code-423n4/2022-09-canto-findings/issues/94)
*Submitted by Respx*

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L224-L258>

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L271-L289>

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L187-L194>

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L201-L222>

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L487-L593>

### Description

There is insufficient resilience in the design for the case where there has been no call to `_update()` for a long time. Consider these possible scenarios:

1.  A denial of service attack on the blockchain has prevented transactions occurring for a significant period of time.
2.  An extreme spike in gas prices has prevented transactions occurring for a significant period of time.
3.  Some unforeseen technical error takes the blockchain down, perhaps during an upgrade or fork.

In any of these scenarios, it is possible that the price of any non-stablecoin token might be prone to serious volatility, `$CANTO` in particular.

The system has no provision for this issue.

### Impact

Consider the following attack scenario:

1.  Assume a period of network downtime, perhaps a DOS attack.
2.  Assume a large drop in the price of `$CANTO` during this time.
3.  Assume attacker is able to queue a  transaction to be executed as soon as network service resumes (perhaps through producing a block themselves or high gas pricing). This transaction uses a lending system that relies on this oracle, and that lending system calls `reserves()` to calculate the TWAP price of `$CANTO`. The values returned are out of date and far too high. The attacker is then able to borrow stablecoins against their `$CANTO` at too high a rate.

### Proof of Concept

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L224-L258>

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L271-L289>

`reserves()`, `sampleReserves()` and `sampleSupply()` make no use of `block.timestamp`. They all measure only the time duration of the observations. There is no awareness of how much time has passed since the most recent observation was made.

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L187-L194>

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L201-L222>

<https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L487-L593>

`quote()` and `sample()` have the same logic, and these functions are called in `getPriceCanto()` and `getPriceNote()`. `getPriceLP()` relies on `sampleReserves()`. They therefore have the same issue.

### Recommended Mitigation Steps

The system could track the average duration time of observations and, if any of the observations in a sample are significantly greater than this average, the system could either refuse to return a sample, or could return a warning flag to indicate that the sample data could be unreliable.

There is precedent in the system for refusing to return a sample (see [line 242 of BaseV1-core.sol](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L242)).

**[nivasan1 (Canto) disputed and commented](https://github.com/code-423n4/2022-09-canto-findings/issues/94#issuecomment-1242189189):**
 > The oracle has been designed specifically for the purpose of use in the lending market, for pairs that have seen a long period of down-time (which is highly unexpected for supported pairs) the collateral factors can be adjusted to scale the price of the asset's collateral value downwards to reflect the volatility after the long period of downtime.

**[0xean (judge) decreased severity to Medium and commented](https://github.com/code-423n4/2022-09-canto-findings/issues/94#issuecomment-1277669646):**
 > This has a high level of external factors that are required to be realized but knowing that the CANTO network has already suffered downtime, I don't think these are too far out of the realm of possibility. Downgrading to Medium. 



***



# Low Risk and Non-Critical Issues

For this contest, 51 reports were submitted by wardens detailing low risk and non-critical issues. The [report highlighted below](https://github.com/code-423n4/2022-09-canto-findings/issues/160) by **lukris02** received the top score from the judge.

*The following wardens also submitted reports: [p\_crypt0](https://github.com/code-423n4/2022-09-canto-findings/issues/176), [Dravee](https://github.com/code-423n4/2022-09-canto-findings/issues/108), [hickuphh3](https://github.com/code-423n4/2022-09-canto-findings/issues/86), [Deivitto](https://github.com/code-423n4/2022-09-canto-findings/issues/164), [ajtra](https://github.com/code-423n4/2022-09-canto-findings/issues/68), [Bnke0x0](https://github.com/code-423n4/2022-09-canto-findings/issues/40), [Rolezn](https://github.com/code-423n4/2022-09-canto-findings/issues/36), [tnevler](https://github.com/code-423n4/2022-09-canto-findings/issues/147), [fatherOfBlocks](https://github.com/code-423n4/2022-09-canto-findings/issues/57), [rvierdiiev](https://github.com/code-423n4/2022-09-canto-findings/issues/74), [rbserver](https://github.com/code-423n4/2022-09-canto-findings/issues/99), [ReyAdmirado](https://github.com/code-423n4/2022-09-canto-findings/issues/82), [0xNazgul](https://github.com/code-423n4/2022-09-canto-findings/issues/145), [erictee](https://github.com/code-423n4/2022-09-canto-findings/issues/20), [oyc\_109](https://github.com/code-423n4/2022-09-canto-findings/issues/21), [0x52](https://github.com/code-423n4/2022-09-canto-findings/issues/25), [Chom](https://github.com/code-423n4/2022-09-canto-findings/issues/128), [Tomo](https://github.com/code-423n4/2022-09-canto-findings/issues/14), [gogo](https://github.com/code-423n4/2022-09-canto-findings/issues/16), [cryptphi](https://github.com/code-423n4/2022-09-canto-findings/issues/71), [CodingNameKiki](https://github.com/code-423n4/2022-09-canto-findings/issues/26), [SinceJuly](https://github.com/code-423n4/2022-09-canto-findings/issues/87), [0x1f8b](https://github.com/code-423n4/2022-09-canto-findings/issues/56), [peritoflores](https://github.com/code-423n4/2022-09-canto-findings/issues/174), [TomJ](https://github.com/code-423n4/2022-09-canto-findings/issues/122), [0xA5DF](https://github.com/code-423n4/2022-09-canto-findings/issues/152), [codexploder](https://github.com/code-423n4/2022-09-canto-findings/issues/88), [Bronicle](https://github.com/code-423n4/2022-09-canto-findings/issues/187), [ignacio](https://github.com/code-423n4/2022-09-canto-findings/issues/129), [Jeiwan](https://github.com/code-423n4/2022-09-canto-findings/issues/44), [hansfriese](https://github.com/code-423n4/2022-09-canto-findings/issues/181), [a12jmx](https://github.com/code-423n4/2022-09-canto-findings/issues/133), [hake](https://github.com/code-423n4/2022-09-canto-findings/issues/37), [R2](https://github.com/code-423n4/2022-09-canto-findings/issues/11), [rokinot](https://github.com/code-423n4/2022-09-canto-findings/issues/43), [RaymondFam](https://github.com/code-423n4/2022-09-canto-findings/issues/89), [0xSky](https://github.com/code-423n4/2022-09-canto-findings/issues/186), [ontofractal](https://github.com/code-423n4/2022-09-canto-findings/issues/183), [pashov](https://github.com/code-423n4/2022-09-canto-findings/issues/15), [csanuragjain](https://github.com/code-423n4/2022-09-canto-findings/issues/137), [Diraco](https://github.com/code-423n4/2022-09-canto-findings/issues/131), [rajatbeladiya](https://github.com/code-423n4/2022-09-canto-findings/issues/69), [CertoraInc](https://github.com/code-423n4/2022-09-canto-findings/issues/127), [ak1](https://github.com/code-423n4/2022-09-canto-findings/issues/134), [JansenC](https://github.com/code-423n4/2022-09-canto-findings/issues/4), [Yiko](https://github.com/code-423n4/2022-09-canto-findings/issues/132), [IgnacioB](https://github.com/code-423n4/2022-09-canto-findings/issues/135), [0x040](https://github.com/code-423n4/2022-09-canto-findings/issues/136), [EthLedger](https://github.com/code-423n4/2022-09-canto-findings/issues/70), [JC](https://github.com/code-423n4/2022-09-canto-findings/issues/185).*

## Summary

| №    | Title                                                                                                                                            | Risk Rating  | Instance Count |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | -------------- |
| L&#x2011;01  | Large number of observations may cause out-of-gas error                         | Low          | 2              |
| L&#x2011;02  | Incorrect comment                                                                                                    | Low          | 1              |
| L&#x2011;03  | Misleading comment                                                                                                 | Low          | 1              |
| N&#x2011;01 | Order of Functions                                                                                                   | Non-Critical | 5              |
| N&#x2011;02 | Maximum line length exceeded                                                                            | Non-Critical | 2+             |
| N&#x2011;03 | Constants may be used                                                                                           | Non-Critical | 18             |
| N&#x2011;04 | Inconsistent comment spacing and location                                                    | Non-Critical | 1              |
| N&#x2011;05 | Loop parameter may be changed for clarity                                                    | Non-Critical | 2              |
| N&#x2011;06 | Functions without comments                                                                                | Non-Critical | 4              |
| N&#x2011;07 | Require statement may be placed before allocating memory for arrays | Non-Critical | 2              |
| N&#x2011;08  | Check zero denominator                                                                                        | Non-Critical          | 2              |
| N&#x2011;09  | Missing check for input variables                                                                      | Non-Critical          | 2              |

## [L-01] Large number of observations may cause out-of-gas error

[Loops](https://docs.soliditylang.org/en/develop/security-considerations.html#gas-limit-and-loops) that do not have a fixed number of iterations, for example, loops that depend on storage values, have to be used carefully: Due to the block gas limit, transactions can only consume a certain amount of gas. Either explicitly or just due to normal operation, the number of iterations in a loop can grow beyond the block gas limit, which can cause the complete contract to be stalled at a certain point.

### Instances

*   [`for(; i < lastIndex; i+=window) {`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L248) (function sampleReserves)
*   [`for(; i < lastIndex; i+=window) {`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L281) (function sampleSupply)

### Recommendation

Restrict the maximum number of sample observations (`points`).

## [L-02] Incorrect comment

[// note in terms of note will always be 1 ](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L498)

### Recommendation

Probably the comment should be like this "price in terms of note will always be 1".

## [L-03] Misleading comment

The comment is misleading, and there is an extra comma and an empty comment line.

### Instances

[Link:](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L229-L232)

            for (uint i = 0; i < _reserves0.length; ++i) {
                reserveAverageCumulative0 += _reserves0[i]; //normalize the reserves for TWAP LP Oracle pricing, 
                reserveAverageCumulative1 += _reserves1[i]; //
            }

### Recommendation

Change or delete comment.

## [N-01] Order of Functions

Some internal functions are between public, some external functions are between public, and some public functions are between external.

### Instances

*   [BaseV1-core.sol: 137](https://github.com/code-423n4/2022-09-canto/blob/main/src/Swap/BaseV1-core.sol#L137)
*   [BaseV1-core.sol: 224](https://github.com/code-423n4/2022-09-canto/blob/main/src/Swap/BaseV1-core.sol#L224)
*   [BaseV1-core.sol: 260](https://github.com/code-423n4/2022-09-canto/blob/main/src/Swap/BaseV1-core.sol#L260)
*   [BaseV1-core.sol: 237](https://github.com/code-423n4/2022-09-canto/blob/main/src/Swap/BaseV1-core.sol#L237)
*   [BaseV1-core.sol: 271](https://github.com/code-423n4/2022-09-canto/blob/main/src/Swap/BaseV1-core.sol#L271)

### Recommendation

According to [Style Guide](https://docs.soliditylang.org/en/v0.8.16/style-guide.html#order-of-functions), ordering helps readers identify which functions they can call and to find the constructor and fallback definitions easier.

Functions should be grouped according to their visibility and ordered:

*   constructor
*   receive function (if exists)
*   fallback function (if exists)
*   external
*   public
*   internal
*   private

## [N-02] Maximum line length exceeded

Some lines of code are too long.

### Instances

*   [`observations.push(Observation(blockTimestamp, reserve0CumulativeLast, reserve1CumulativeLast, totalSupplyCumulativeLast));`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L149)
*   [`_totalSupply[index] = (observations[nextIndex].totalSupplyCumulative - observations[i].totalSupplyCumulative) / timeElapsed;`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L284)
*   and more, if you take into account the beginning indent and / or comments.

### Recommendation

According to [Style Guide](https://docs.soliditylang.org/en/v0.8.16/style-guide.html#maximum-line-length), maximum suggested line length is 120 characters.

Make the lines shorter.

## [N-03] Constants may be used

Constants may be used instead of literal values.

### Instances

*   [`uint[] memory supply = pair.sampleSupply(8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L550)
*   [`prices = pair.sample(token1, decimals, 8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L561)
*   [`(unitReserves, assetReserves) = pair.sampleReserves(8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L562)
*   [`prices = pair.sample(token0, decimals, 8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L565)
*   [`(assetReserves, unitReserves) = pair.sampleReserves(8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L566)
*   [`prices = pair.sample(token1, decimals, 8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L571)
*   [`(unitReserves, assetReserves) = pair.sampleReserves(8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L572)
*   [`prices = pair.sample(token0, decimals, 8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L575)
*   [`(assetReserves, unitReserves) = pair.sampleReserves(8, 1);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L576)
*   [`for(uint i; i < 8; ++i) {`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L581)
*   [`return 1e18; // Stable coins supported by the lending market are instantiated by governance and their price will always be 1 note`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L499)
*   [`return 1e18 * 1e18 / (10 ** decimals); //Scale Price as a mantissa to maintain precision in comptroller`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L503)
*   [`return 1e18 * 1e18 / (10 ** decimals); //Scale Price as a mantissa to maintain precision in comptroller`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L507)
*   [`return getPriceCanto(underlying) * getPriceNote(address(wcanto), false) / 1e18;`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L520)
*   [`LpPricesCumulative += (token0TVL + token1TVL) * 1e18 / supply[i];`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L584)
*   [`return LpPrice * getPriceNote(address(wcanto), false) / 1e18; // return the price in terms of Note`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L592)
*   [`return price * 1e18 / decimals; //return the scaled price`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L533)
*   [`return price * 1e18 / decimals; // divide by decimals now to maintain precision`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L545)

### Recommendation

Define constant variables for repeated values (8 and 1e18).

## [N-04] Inconsistent comment spacing and location

Some comments are above the line of code and some next to it.

Some comments are indented between *// and the comment text*, some are not.

### Instances

*   [Link:](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L489-L490)

<!---->

    { //manual scope to pop symbol off of stack
     string memory symbol = ctoken.symbol();

*   [`underlying = address(ICErc20(address(ctoken)).underlying()); // We are getting the price for a CErc20 lending market`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L495)
*   [Link:](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L497-L499)

<!---->

    //set price statically to 1 when the Comptroller is retrieving Price
    if (compareStrings(symbol, "cNOTE")) { // note in terms of note will always be 1 
        return 1e18; // Stable coins supported by the lending market are instantiated by governance and their price will always be 1 note

*   [`return 1e18 * 1e18 / (10 ** decimals); //Scale Price as a mantissa to maintain precision in comptroller`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-periphery.sol#L503)
*   all other functions...

### Recommendation

Use consistent comment spacing and location.

## [N-05] Loop parameter may be changed for clarity

In loop are used `_reserves0.length`. It is equal to input variable `granularity`. It can be clearer and more consistent if you use an input variable in the loop.

### Instances

1.  [Link:](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L224-L229)

<!---->

        function reserves(uint granularity) external view returns(uint, uint) {
            (uint[] memory _reserves0, uint[] memory _reserves1)= sampleReserves(granularity, 1);
            uint reserveAverageCumulative0;
            uint reserveAverageCumulative1;

            for (uint i = 0; i < _reserves0.length; ++i) {

2.  [Link:](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L260-L264)

<!---->

        function totalSupplyAvg(uint granularity) external view returns(uint) {
            uint[] memory _totalSupplyAvg = sampleSupply(granularity, 1);
            uint totalSupplyCumulativeAvg;

            for (uint i = 0; i < _totalSupplyAvg.length; ++i) {

### Recommendation

1.  Change to

<!---->

        function reserves(uint granularity) external view returns(uint, uint) {
            (uint[] memory _reserves0, uint[] memory _reserves1)= sampleReserves(granularity, 1);
            uint reserveAverageCumulative0;
            uint reserveAverageCumulative1;
            
            //HERE
            for (uint i = 0; i < granularity; ++i) {

2.  Change to

<!---->

        function totalSupplyAvg(uint granularity) external view returns(uint) {
            uint[] memory _totalSupplyAvg = sampleSupply(granularity, 1);
            uint totalSupplyCumulativeAvg;

            //HERE
            for (uint i = 0; i < granularity; ++i) {

## [N-06] Functions without comments

Some functions do not have comments describing them.

### Instances

*   [`function reserves(uint granularity)`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L224)
*   [`function sampleReserves(uint points, uint window)`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L237)
*   [`function totalSupplyAvg(uint granularity)`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L260)
*   [`function sampleSupply(uint points, uint window)`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L271)

### Recommendation

Add comments.

## [N-07] Require statement may be placed before allocating memory for arrays

### Instances

1.  [Link:](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L238-L242)

<!---->

            uint[] memory _reserves0 = new uint[](points);
            uint[] memory _reserves1 = new uint[](points);
            
            uint lastIndex = observations.length-1;
            require(lastIndex >= points * window, "PAIR::NOT READY FOR PRICING");

2.  [Link:](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L272-L275)

<!---->

            uint[] memory _totalSupply = new uint[](points);
            
            uint lastIndex = observations.length-1;
            require(lastIndex >= points * window, "PAIR::NOT READY FOR PRICING");

### Recommendation

1.  Change to

<!---->

            uint lastIndex = observations.length-1;
            require(lastIndex >= points * window, "PAIR::NOT READY FOR PRICING");

            uint[] memory _reserves0 = new uint[](points);
            uint[] memory _reserves1 = new uint[](points);

2.  Change to

<!---->

            uint lastIndex = observations.length-1;
            require(lastIndex >= points * window, "PAIR::NOT READY FOR PRICING");
            
            uint[] memory _totalSupply = new uint[](points);

## [N-08] Check zero denominator

If the input parameter is equal to zero, this will cause the function call failure on division.

### Instances

*   [`return (reserveAverageCumulative0 / granularity, reserveAverageCumulative1 / granularity);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L234)
*   [`return (totalSupplyCumulativeAvg / granularity);`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L268)

### Recommendation

Add the check to prevent function call failure.

## [N-09] Missing check for input variables

If input variable `points`== 0, function will return empty array.

More critical, if input variable `window`== 0, function will return array with default values, which may lead to further incorrect calculations.

### Instances

*   [`function sampleReserves(uint points, uint window)`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L237)
*   [`function sampleSupply(uint points, uint window)`](https://github.com/code-423n4/2022-09-canto/blob/65fbb8b9de22cf8f8f3d742b38b4be41ee35c468/src/Swap/BaseV1-core.sol#L271)

### Recommendation

Add require statement or custom error - `points!= 0 && window!= 0`.

***


# Disclosures

C4 is an open organization governed by participants in the community.

C4 Contests incentivize the discovery of exploits, vulnerabilities, and bugs in smart contracts. Security researchers are rewarded at an increasing rate for finding higher-risk issues. Contest submissions are judged by a knowledgeable security researcher and solidity developer and disclosed to sponsoring developers. C4 does not conduct formal verification regarding the provided code but instead provides final verification.

C4 does not provide any guarantee or warranty regarding the security of this project. All smart contract software should be used at the sole risk and responsibility of users.
